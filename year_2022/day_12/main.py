import networkx as nx

# parse and create digraph for all possible movement within a tile
# use shortest paths algorithm from starting point to exit
# use bellman ford for negative weights if needed


with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

height = len(input_text)
width = len(input_text[0])
coordinates_parse = list(reversed(input_text))
graph = nx.DiGraph()

S_coord = None
E_coord = None

for y in range(height):
    for x in range(width):
        current_char = coordinates_parse[y][x]
        coord = (x,y)
        graph.add_node(coord, char = current_char)

for current_coord in graph.nodes:
    x, y = current_coord
    current_char = graph.nodes[current_coord]['char']

    adjacent_coords = [
        (x+1,y),
        (x-1,y),
        (x,y+1),
        (x,y-1)
    ]

    for adj_coord in adjacent_coords:                               
        if adj_coord not in graph.nodes:
            continue
        if current_char == 'S':                     
            graph.add_edge(current_coord, adj_coord, weight=0)      # edges lead away from S
            S_coord = current_coord
            continue
        if current_char == 'E':
            E_coord = current_coord
            continue
        
        adj_char = graph.nodes[adj_coord]['char']
        current_elevation = ord(current_char)
        adj_elevation = None
        if adj_char == 'E':                                         # E always has highest elevation
            adj_elevation = ord('z')
        else: 
            adj_elevation = ord(adj_char)
        cost = adj_elevation - current_elevation

        if cost <= 1:                                               # adde edge if the elevation difference is 1 or less
            graph.add_edge(current_coord, adj_coord, weight=cost)


unweighted_shortest_path = nx.shortest_path(graph, source=S_coord, target=E_coord)
print('part1', len(unweighted_shortest_path)-1)       

starting_coords = []
possible_paths_length = []

for coord in graph.nodes:
    if graph.nodes[coord]['char'] == 'a':
        starting_coords.append(coord)

for starting_coord in starting_coords:
    if not nx.has_path(graph, source=starting_coord, target=E_coord):
        continue
    unweighted_shortest_path = nx.shortest_path(graph, source=starting_coord, target=E_coord)
    possible_paths_length.append(len(unweighted_shortest_path)-1)

print('part2', min(possible_paths_length))



            





