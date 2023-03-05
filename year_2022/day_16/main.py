from parse import parse
import networkx as nx
from pyvis.network import Network

'''
priority:
    if current valve is closed:
        check all adjacent closed valves
        if there is an adjacent closed valve:
            check if moving 

'''

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
    # print(source, rate, dest_list)
    dest_list = dest_list.split(', ')
    for dest in dest_list:
        tunnel.add_edge(source, dest, traversed=False)
        tunnel.nodes[source]['rate'] = rate
nx.set_node_attributes(tunnel, False, 'open')           # initializes the attribute for all nodes

path_list = ['AA']
pressure_released = 0
current_location = 'AA'
next_location = None

for node in tunnel.nodes:
    if tunnel.nodes[node]['rate'] == 0:
        tunnel.nodes[node]['open'] = True


# make a tree of all possible timelines

# this greedy algorithm does not guarantee optimal solution, but an approximate one
# must implement a bfs tree to search all possible timelines

time_remaining = time_limit
while time_remaining > 0:
    pressure_release_potential = 0
    for next_node in tunnel.nodes:
        if current_location == next_node or tunnel.nodes[next_node]['open'] == True:
            continue
        cost = nx.shortest_path_length(tunnel, source=current_location, target=next_node) + 1
        pressure_release_potential_temp = (time_remaining - cost) * tunnel.nodes[next_node]['rate']

        print('time remaining {}, current node {}, possible next node {}, cost {}, potential release {}'.format(time_remaining, current_location, next_node, cost, pressure_release_potential_temp))

        if (pressure_release_potential_temp > pressure_release_potential):
            pressure_release_potential = pressure_release_potential_temp
            next_location = next_node
    
    time_remaining -= cost
    if time_remaining < 0:
        break

    if current_location == next_location:
        break

    path_list.append(next_location)
    tunnel.nodes[next_location]['open'] = True
    pressure_released += pressure_release_potential
    current_location = next_location

print(path_list)
print(pressure_released)
        
