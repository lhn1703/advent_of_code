'''
solution is a digraph
each node (logic gate) has the following attributes:
    title (name of the output variable)
    operation (and, or, xor, not, etc)
    output value (only 1 value)
each edge (wire) has the following attributes:
    title (name of the variable)
    wire value (only 1 value)

parsing algorithm:
    go through line by line
    create all nodes first with empty attributes 
    connect edges and apply attributes as needed
    

graph algorithm:
    construct the entire circuit graph
    find the root (the starting point) node
    perform BFS and update edge values: evaluate node inputs and node outputs 

pyvis:
    label displays always
    title is for mouse hover text
'''
import networkx as nx
from pyvis.network import Network

def parse_line(line):
    input = line.split(' -> ')[0]           # input can be a literal, wire, or combination
    input_1= None
    input_2 = None
    output = line.split(' -> ')[1]          # output will always be a wire
    operation = None

    

    if input.isdigit():
        input_1 = int(input)
        operation = 'ASSIGN'
    elif 'AND' in input or 'OR' in input:
        input_1 = input.split()[0]
        operation = input.split()[1]
        input_2 = input.split()[2]
    elif 'NOT' in input:
        operation = input.split()[0]
        input_1 = input.split()[1]
    elif 'SHIFT' in input:
        input_1 = input.split()[0]
        operation = input.split()[1]
    else:
        raise Exception('{} is not a valid line'.format(line))
    return input_1, input_2, operation, output

with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

digital_circuit = nx.DiGraph()

# # first pass to create all nodes
# # all nodes will be added with this since all output variables must eventually be driven by a defined value
# for line in input_text:
#     input_1, input_2, operation, output = parse_line(line)
#     digital_circuit.add_node(output, label=output, operation=operation, output_value=None)

# # assigning the edges
# for line in input_text:
#     input_1, input_2, operation, output = parse_line(line)
    
#     if operation == 'ASSIGN':                       # this node must be a source node if it only drives an input literal
#         digital_circuit.nodes[output]['output_value'] = input_1     # special case because of assign
#     elif operation == 'AND' or operation == 'OR':
#         digital_circuit.add_edge(input_1, output, wire_value=None, title=input_1)
#         digital_circuit.add_edge(input_2, output, wire_value=None, title=input_2)
#     else:
#         digital_circuit.add_edge(input_1, output, wire_value=None, title=input_1)

digital_circuit.add_node(0)
digital_circuit.add_node(1)
digital_circuit.add_node(2)
digital_circuit.add_node(3)

digital_circuit.add_edge(0,2)
digital_circuit.add_edge(1,2)
digital_circuit.add_edge(2,3)

pyvis_network = Network('500px', '500px', directed=True)
pyvis_network.from_nx(digital_circuit)
html_content = pyvis_network.generate_html('circuit.html')