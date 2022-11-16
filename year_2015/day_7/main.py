'''
solution is a digraph
each node (logic gate) has the following attributes:
    title (name of its output variable)
    operation (and, or, xor, not, etc)
each edge (wire) has the following attributes:
    title (name of the variable)
    value (only 1 value)

parsing algorithm:
    go through line by line
    create all nodes first 
    connect edges and apply attributes as needed
    

graph algorithm:
    construct the entire circuit graph
    find the root (the starting point) node
    perform BFS and update edge values, node inputs and node outputs 
    find the output of the wire a

pyvis:
    label displays always
    title is for mouse hover text
'''
import networkx as nx
import pyvis as Network

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

digital_circuit = nx.digraph()

for line in input_text:
    input, output_node = line.split(' -> ')[0], line.split(' -> ')[1]

    if input.isdigit():         # if this is a straight wire assign, it also must be the root
        digital_circuit.add_node('input', title='input', operation='assign')
        digital_circuit.add_node(output_node)

