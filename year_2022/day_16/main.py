from parse import parse
import networkx as nx
from pyvis.network import Network

def visualize(nx_graph):
    nt = Network(directed=True)
    # populates the nodes and edges data structures
    nt.from_nx(nx_graph)
    nt.show('nx.html')

with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

time_limit = 30
tunnel = nx.DiGraph()

for line in input_text:
    line = line.replace('tunnel leads to valve', 'tunnels lead to valves') # for parsing purposes
    source, rate, dest_list = parse('Valve {} has flow rate={}; tunnels lead to valves {}', line)
    rate = int(rate)
    print(source, rate, dest_list)
    dest_list = dest_list.split(', ')
    for dest in dest_list:
        tunnel.add_edge(source, dest, traversed=False)
        tunnel.nodes[source]['rate'] = rate

nx.set_node_attributes(tunnel, False, 'open')           # initializes the attribute for all nodes

current_location = 'AA'
previous_location = 'AA'                                # make sure to never backtrack
tunnel.nodes['AA']['open'] = True                       # assumes the first valve is already open (for loop convenience)
pressure = 0
for t in range(time_limit):                             # perform greedy graph algorithm
    for nodes in tunnel.nodes:                          # calculating released pressure first
        if tunnel.nodes[nodes]['open'] == True:
            pressure += tunnel.nodes[nodes]['rate']

    adj_edges = list(tunnel.edges(current_location))
    highest_weight = 0

    if tunnel.nodes[current_location]['open'] == True:  # if current tunnel is already open, move along



