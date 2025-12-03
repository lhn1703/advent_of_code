from parse import *
import networkx as nx
from copy import deepcopy

# make sure to & 0xffff for 16 bit
def parse_string(input_string: str):
	str_list = parse('{} -> {}', input_string)
	in1 = in2 = operation = out = wire_val = None

	lhs = str_list[0]
	rhs = str_list[1]

	out = rhs.strip()

	if lhs.isdigit(): # if first part only contains numbers then it is a wire
		wire_val = int(lhs.strip()) & 0xffff
		operation = 'WIRE'
	elif 'AND' in lhs or 'OR' in lhs:
		lhs_str = parse('{} {} {}', lhs)
		in1 = lhs_str[0]
		operation = lhs_str[1]
		in2 = lhs_str[2]
	elif 'LSHIFT' in lhs or 'RSHIFT' in lhs:
		lhs = lhs.split()
		in1 = lhs[0]
		operation = str(lhs[1]) + ' ' + str(lhs[2])
	elif 'NOT' in lhs:
		lhs = lhs.split()
		operation = str(lhs[0])
		in1 = lhs[1]
	elif lhs.islower() and rhs.islower(): # special exception for weird wires
		operation = 'WIRE'
		in1 = lhs
	else:
		raise Exception('--ERROR-- unsupported string: ', input_string)
	
	return in1, in2, operation, out, wire_val
	
def perform_logic(circuit: nx.DiGraph, node): # recursive function 
	operation = circuit.nodes[node]['operation']
	edge_list = list(circuit.out_edges(node))

	# special case if the there is a value harded coded as one of the nodes
	if node.isdigit():
		circuit.nodes[node]['operation'] = 'WIRE'
		circuit.nodes[node]['value'] = int(node) & 0xffff
		return
	
	if operation == 'WIRE': 
		if len(edge_list) == 0: # base case hitting the leaf node
			return
		elif len(edge_list) == 1: # weird exception case where there is 2 wires connected to eachother
			edge = edge_list[0]
			u,v = edge
			if circuit.nodes[v]['value'] == None:
				perform_logic(circuit, v)
				assert circuit.nodes[v]['value'] != None
				circuit.nodes[node]['value'] = circuit.nodes[v]['value']

	elif 'SHIFT' in operation or 'NOT' in operation:
		assert len(edge_list) == 1
		edge = edge_list[0]
		u,v = edge

		if circuit.nodes[v]['value'] == None:
			perform_logic(circuit, v)
		assert circuit.nodes[v]['value'] != None

		computed_value = None
		if 'SHIFT' in operation:
			shift_op = operation.split()[0]
			operand = int(operation.split()[1])
			if shift_op == 'LSHIFT':
				computed_value = circuit.nodes[v]['value'] << operand
			elif shift_op == 'RSHIFT':
				computed_value = circuit.nodes[v]['value'] >> operand
			else:
				raise Exception("Invalid operation", operation)
		elif operation == 'NOT':
			computed_value = ~circuit.nodes[v]['value']
		circuit.nodes[node]['value'] = computed_value & 0xffff # 16 bit integer mask
	elif operation == 'AND' or operation == 'OR':
		assert len(edge_list) == 2
		edge0, edge1 = edge_list[0], edge_list[1]
		u0, v0 = edge0
		u1, v1 = edge1

		if circuit.nodes[v0]['value'] == None:
			perform_logic(circuit, v0)
		assert circuit.nodes[v0]['value'] != None

		if circuit.nodes[v1]['value'] == None:
			perform_logic(circuit, v1)
		assert circuit.nodes[v1]['value'] != None

		computed_value = None
		if operation == 'AND':
			computed_value = circuit.nodes[v0]['value'] & circuit.nodes[v1]['value']
		elif operation == 'OR':
			computed_value = circuit.nodes[v0]['value'] | circuit.nodes[v1]['value']
		circuit.nodes[node]['value'] = computed_value & 0xffff # 16 bit integer mask

def main():
	### PART 1
	# creating circuit graph
	circuit = nx.DiGraph()
	with open('input.txt', 'r') as ifile:
		for line in ifile:
			in1, in2, operation, out, wire_val = parse_string(line)
			# out == current node
			# the inputs are leaf nodes, outputs are root nodes since they require leaf node data to get value
			# if the circuit does not have current output gate, add it
			if not circuit.has_node(out): 			
				circuit.add_node(out, operation=operation, value=wire_val)

			if operation == 'WIRE': # if output is a wire
				if wire_val == None: # edge case of double wires
					circuit.add_edge(out, in1)
				pass
			elif 'SHIFT' in operation or 'NOT' in operation:
				if not circuit.has_node(in1): # create empty input node if not exist
					circuit.add_node(in1, operation=None, value=None)
				circuit.add_edge(out, in1)
			elif operation == 'AND' or operation == 'OR':
				if not circuit.has_node(in1): # create empty input node1 if not exist
					circuit.add_node(in1, operation=None, value=None)
				circuit.add_edge(out, in1)
				if not circuit.has_node(in2): # create empty input node2 if not exist
					circuit.add_node(in2, operation=None, value=None)
				circuit.add_edge(out, in2)
			else:
				print('unsuported string:', line)
				raise Exception()
			
			# update current output node
			
			circuit.nodes[out]['value'] = wire_val
			circuit.nodes[out]['operation'] = operation

	circuit2 = deepcopy(circuit)

	aoc_node = 'a'
	perform_logic(circuit, aoc_node)
	print('part 1:', aoc_node, circuit.nodes[aoc_node])

	# hardcode value of wire b to the output of a from part 1
	circuit2.nodes['b']['value'] = circuit.nodes['a']['value']

	perform_logic(circuit2, aoc_node)
	print('part 2:', aoc_node, circuit2.nodes[aoc_node])



if __name__ == "__main__":
	main()

