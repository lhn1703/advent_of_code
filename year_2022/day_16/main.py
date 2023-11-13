from parse import parse
import argparse
import networkx as nx
from copy import deepcopy

parser = argparse.ArgumentParser(description='AOC')
parser.add_argument('-i','--input', help='input text file', required=True)
args = parser.parse_args()
input_file = args.input

with open(input_file, 'r') as input_file:
    input_text = input_file.read().splitlines()

time_limit = 30
time_to_open = 1
tunnel = nx.DiGraph()
timeline = nx.DiGraph()

valve_rate = {}

for line in input_text:
    line = line.replace('tunnel leads to valve', 'tunnels lead to valves') # for parsing purposes
    source, rate, dest_list = parse('Valve {} has flow rate={}; tunnels lead to valves {}', line)
    rate = int(rate)

    valve_rate[source] = rate

    # print(source, rate, dest_list)
    dest_list = dest_list.split(', ')
    for dest in dest_list:
        tunnel.add_edge(source, dest, traversed=False)
        tunnel.nodes[source]['rate'] = rate
nx.set_node_attributes(tunnel, False, 'open')           # initializes the attribute for all nodes

for node in tunnel.nodes:                               # if a valve has 0, treat it as already opened
    if tunnel.nodes[node]['rate'] == 0:
        tunnel.nodes[node]['open'] = True

# creating distance matrix between valves
shortest_path_dict = {}
for src in tunnel.nodes:
    shortest_path_dict[src] = {}
    for dst in tunnel.nodes:
        shortest_path_dict[src][dst] = nx.shortest_path_length(tunnel, source=src, target=dst)

def get_closed_valves():
    closed_valves = set()
    for node in tunnel.nodes:
        if tunnel.nodes[node]['open'] == False:
            closed_valves.add(node)
    return closed_valves

initial_closed_valves = get_closed_valves()

# https://www.reddit.com/r/adventofcode/comments/zo21au/comment/j0nz8df/?utm_source=share&utm_medium=web2x&context=3 
bfs_queue = []
possible_board_states = []

board_state = {
    'position': 'AA',
    'time_remaining': time_limit,
    'pressure_released': 0,
    'remaining_valves': initial_closed_valves
}

bfs_queue.append(board_state)
possible_board_states.append(board_state)
while bfs_queue != []:
    current_board_state = bfs_queue.pop(0)
    current_position = current_board_state['position']
    time_remaining = current_board_state['time_remaining']
    pressure_released = current_board_state['pressure_released']
    remaining_valves = current_board_state['remaining_valves']

    for next_valve in remaining_valves:
        time_cost = shortest_path_dict[current_position][next_valve] + time_to_open
        potential_pressure_released = (time_remaining - time_cost) *  valve_rate[next_valve]
        if potential_pressure_released < 0:             # if time cost is more than time remaining, then cannot open this valve
            continue

        new_position = next_valve
        new_time_remaining = time_remaining - time_cost
        new_pressure_released = pressure_released + potential_pressure_released
        new_remaining_valves = deepcopy(remaining_valves)
        new_remaining_valves.remove(new_position)

        new_board_state = {
            'position': new_position,
            'time_remaining': new_time_remaining,
            'pressure_released': new_pressure_released,
            'remaining_valves': new_remaining_valves
        }

        bfs_queue.append(new_board_state)
        possible_board_states.append(new_board_state)

pressure = 0
for board_state in possible_board_states:
    # print(board_state)
    if board_state['pressure_released'] > pressure:
        pressure = board_state['pressure_released']
print(pressure)

