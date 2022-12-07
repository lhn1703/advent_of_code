import networkx as nx
from pyvis.network import Network

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

filesystem = nx.DiGraph()
filesystem.add_node('/', size=0, is_folder = True, label='/')                # root directory

current_folder = '/'
pwd = current_folder

for line in input_text:
    if '/' in line or '$ ls' in line:     # skips the first instruction; ls isn't useful if '$' is used to differentiate input and output
        continue

    if '$ cd' in line:
        cd_dest = line.split()[2]    # folder names aren't unique
        if cd_dest == '..':
            pwd = list(filesystem.predecessors(pwd))[0]       # each subfolder can only have 1 parent folder
        else:
            if current_folder == '/':        # edge case
                pwd += cd_dest
            else:
                pwd += '/' + cd_dest
    else:
        new_dir = pwd + line.split()[1]
        if 'dir ' in line:
            filesystem.add_node(new_dir, size=0, is_folder = True, label=line.split()[1])          # compute folder size later
            filesystem.add_edge(pwd, new_dir)
        else:
            filesystem.add_node(new_dir, size=int(line.split()[0]), is_folder = False, label=line.split()[1])       # record all known file sizes
            filesystem.add_edge(pwd, new_dir)                    # files are folders with size attribute


dfs_tree = nx.dfs_successors(filesystem, '/')                                       # dictionary of dfs           
leaf_folder_list = list(reversed(dfs_tree.keys()))

for folder in leaf_folder_list:
    size = 0
    folder_contents = dfs_tree[folder]
    for item in folder_contents:
        size += filesystem.nodes[item]['size']
    filesystem.nodes[folder]['size'] = size

sum = 0
for node in filesystem.nodes:
    if filesystem.nodes[node]['size'] <= 100000 and filesystem.nodes[node]['is_folder'] == True:
        sum += filesystem.nodes[node]['size']

print('part1:', sum)


total_disk_space = 70000000
available_disk_space = total_disk_space - filesystem.nodes['/']['size']
required_disk_space = 30000000
potential_delete_sizes = []

for node in filesystem.nodes:
    if (available_disk_space + filesystem.nodes[node]['size']) >= required_disk_space and filesystem.nodes[node]['is_folder'] == True:
        potential_delete_sizes.append(filesystem.nodes[node]['size'])

print('part2:', min(potential_delete_sizes))


filename = 'file.html'
pyvis_network = Network()
pyvis_network.from_nx(filesystem, default_node_size=2)
html_content = pyvis_network.show(filename)

# with open(filename, 'w') as output_file:
#     output_file.write(html_content)


