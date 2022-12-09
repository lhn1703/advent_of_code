with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

grid_size = len(input_text)

class Tree:
    def __init__(self, height = None, visible = None) -> None:
        self.height = height
        self. visible = visible

class Forest:
    def __init__(self) -> None:
        self.map = {}

forest = Forest()

x = 0
y = 0
for line in input_text:
    for char in line:
        tree_height = int(char)
        tree_coordinate = (x,y)
        tree = Tree(tree_height, False)
        forest.map[tree_coordinate] = tree
        y += 1
    y = 0
    x += 1

# brute force algorithm to check from all 4 sides

# top to bottom
for j in range(grid_size):
    tallest_height = None
    for i in range(grid_size):
        coordindate = (i,j)
        tree_height = forest.map[coordindate].height
        if tallest_height == None or tree_height > tallest_height:
            tallest_height = tree_height
            forest.map[coordindate].visible = True

# bottom to top
for j in range(grid_size):
    tallest_height = None
    for i in reversed(range(grid_size)):
        coordindate = (i,j)
        tree_height = forest.map[coordindate].height
        if tallest_height == None or tree_height > tallest_height:
            tallest_height = tree_height
            forest.map[coordindate].visible = True     

# left to right
for i in range(grid_size):
    tallest_height = None
    for j in range(grid_size):
        coordindate = (i,j)
        tree_height = forest.map[coordindate].height
        if tallest_height == None or tree_height > tallest_height:
            tallest_height = tree_height
            forest.map[coordindate].visible = True

# right to left
for i in range(grid_size):
    tallest_height = None
    for j in reversed(range(grid_size)):
        coordindate = (i,j)
        tree_height = forest.map[coordindate].height
        if tallest_height == None or tree_height > tallest_height:
            tallest_height = tree_height
            forest.map[coordindate].visible = True

visible_count = 0
for i in range(grid_size):
    for j in range(grid_size):
        coordindate = (i,j)
        if forest.map[coordindate].visible:
            visible_count += 1

print('part1:', visible_count)

best_scenic_score = 0
for i in range(grid_size):
    for j in range(grid_size):
        coordindate = (i,j)
        current_height = forest.map[coordindate].height

        current_scenic_score = 1

        # looking up
        u = i - 1
        u_score = 0
        while u >= 0:
            u_coordindate = (u,j)
            u_height = forest.map[u_coordindate].height
            u_score += 1
            if u_height >= current_height:
                break
            u -= 1
        current_scenic_score *= u_score

        # looking down
        d = i + 1
        d_score = 0
        while d < grid_size:
            d_coordindate = (d,j)
            d_height = forest.map[d_coordindate].height
            d_score += 1
            if d_height >= current_height:
                break
            d += 1
        current_scenic_score *= d_score

        # looking left
        l = j - 1
        l_score = 0
        while l >= 0:
            l_coordindate = (i,l)
            l_height = forest.map[l_coordindate].height
            l_score += 1
            if l_height >= current_height:
                break
            l -= 1
        current_scenic_score *= l_score

        # looking right
        r = j + 1
        r_score = 0
        while r < grid_size:
            r_coordindate = (i,r)
            r_height = forest.map[r_coordindate].height
            r_score += 1
            if r_height >= current_height:
                break
            r += 1
        current_scenic_score *= r_score

        if current_scenic_score > best_scenic_score:
            best_scenic_score = current_scenic_score

print('part2:', best_scenic_score)
