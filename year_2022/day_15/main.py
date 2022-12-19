with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

grid_zize = 600
map = {}
for y in range(grid_zize):
    for x in range(grid_zize):
        coord = (x,y)
        map[coord] = '.'
source_coord = (500,0)
map[source_coord] = '+'

for line in input_text:
    input_list = line.split(' -> ')
    for i in range(len(input_list)-1):
        str_coord_0 = input_list[i]
        str_coord_1 = input_list[i+1]

        x0 = int(str_coord_0.split(',')[0])
        y0 = int(str_coord_0.split(',')[1])
        x1 = int(str_coord_1.split(',')[0])
        y1 = int(str_coord_1.split(',')[1])

        # fill in the endpoints first
        map[(x0,y0)] = '#'
        map[(x1,y1)] = '#'

        while x0 < x1:
            x0 += 1
            map[(x0,y0)] = '#'
        while x1 < x0:
            x1 += 1
            map[(x1,y1)] = '#'
        while y0 < y1:
            y0 += 1
            map[(x0,y0)] = '#'
        while y1 < y0:
            y1 += 1
            map[(x1,y1)] = '#'

def sand_fall(source_coord = source_coord):
    x, y = source_coord
    while True:
        down_coord = (x,y+1)
        left_down_coord = (x-1,y+1)
        right_down_coord = (x+1,y+1)
        if y+1 >= grid_zize:                      # falls into abyss
            return None
        if map[down_coord] == '.':
            x, y = down_coord
        elif map[left_down_coord] == '.':
            x, y = left_down_coord
        elif map[right_down_coord] == '.':
            x, y = right_down_coord
        else:
            break
    return (x,y)
    

i = 0
while True:
    if sand_fall() == None:
        break
    else:
        map[sand_fall()] = 'o'
    i += 1
print('part1', i)


### PART 2 ###

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

max_y = 0
for line in input_text:
    input_list = line.split(' -> ')
    for s in input_list:
        x, y = int(s.split(',')[0]), int(s.split(',')[1])
        if y > max_y:
            max_y = y
max_y += 3

max_x = 100000
map = {}
for y in range(max_y):
    for x in range(max_x):
        coord = (x,y)
        map[coord] = '.'
source_coord = (500,0)
map[source_coord] = '+'
for x in range(max_x):
    map[(x,max_y-1)] = '#'

for line in input_text:
    input_list = line.split(' -> ')
    for i in range(len(input_list)-1):
        str_coord_0 = input_list[i]
        str_coord_1 = input_list[i+1]

        x0 = int(str_coord_0.split(',')[0])
        y0 = int(str_coord_0.split(',')[1])
        x1 = int(str_coord_1.split(',')[0])
        y1 = int(str_coord_1.split(',')[1])

        # fill in the endpoints first
        map[(x0,y0)] = '#'
        map[(x1,y1)] = '#'

        while x0 < x1:
            x0 += 1
            map[(x0,y0)] = '#'
        while x1 < x0:
            x1 += 1
            map[(x1,y1)] = '#'
        while y0 < y1:
            y0 += 1
            map[(x0,y0)] = '#'
        while y1 < y0:
            y1 += 1
            map[(x1,y1)] = '#'

def sand_fall(source_coord = source_coord):
    x, y = source_coord
    xs, ys = source_coord
    while True:
        down_coord = (x,y+1)
        left_down_coord = (x-1,y+1)
        right_down_coord = (x+1,y+1)
        
        # if the 3 blocks below origin is filled, then the source will be filled
        # brute force approach, but my i9-13900k and 32GB RAM can handle it
        if map[(xs, ys+1)] == 'o' and map[(xs-1, ys+1)] == 'o' and map[(xs+1, ys+1)] == 'o':        
            return None

        if map[down_coord] == '.':
            x, y = down_coord
        elif map[left_down_coord] == '.':
            x, y = left_down_coord
        elif map[right_down_coord] == '.':
            x, y = right_down_coord
        else:
            break
    return (x,y)
    
i = 1
while True:
    if sand_fall() == None:
        break
    else:
        map[sand_fall()] = 'o'
    i += 1

print('part2', i)

