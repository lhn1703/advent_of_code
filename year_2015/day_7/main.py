'''
solution is a digraph
each node (logic gate) has the following attributes:
    title (name)
    input list
    output list
    operation (and, or, xor, not, etc)
each edge (wire) has the following attributes:
    title (name)
    value (only 1 value)

algorithm:
    construct the entire circuit graph
    find the root (the starting point) node
    perform BFS and update edge values, node inputs and node outputs 
    find the output of the wire a
'''
import networkx as nx
import pyvis as Network

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

digital_circuit = nx.digraph()
