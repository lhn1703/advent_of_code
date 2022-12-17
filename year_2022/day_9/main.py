with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

def move_head(h_coord, direction):
    hx, hy = h_coord
    if direction == 'U':
        hx += 1
    elif direction == 'D':
        hx -= 1
    elif direction == 'L':
        hy -= 1
    elif direction == 'R':
        hy += 1
    else:
        raise Exception(direction, 'is not a valid direction')
    return (hx, hy)

def move_tail(new_h_coord, t_coord, direction):            # can only move 1 tile at a time
    hx, hy = new_h_coord
    tx, ty = t_coord

    # generate all adjacent coordinates to the head, also including the head location so 9 total
    adjacent_coordinates = (
        (hx, hy),
        (hx-1, hy-1),
        (hx-1, hy),
        (hx-1, hy+1),
        (hx, hy-1),
        (hx, hy),
        (hx, hy+1),
        (hx+1, hy-1),
        (hx+1, hy),
        (hx+1, hy+1)
    )

    if t_coord in adjacent_coordinates:
        pass
    elif hx == tx or hy == ty:          # if the head and tail are in the same row or column, simple translation
        if direction == 'U':
            tx += 1
        elif direction == 'D':
            tx -= 1
        elif direction == 'L':
            ty -= 1
        elif direction == 'R':
            ty += 1
    else:
        if direction == 'U':            # if vertical direction, then must be in the same column
            tx += 1
            ty = hy
        elif direction == 'D':
            tx -= 1
            ty = hy
        elif direction == 'L':          # if horizontal movement, must be in the same row
            ty -= 1
            tx = hx
        elif direction == 'R':
            ty += 1
            tx = hx
    
    new_t_coord = (tx, ty)

    return new_t_coord

h_coord = (0,0)
t_coord = (0,0)

unique_t_coords = [t_coord]

for line in input_text:
    direction = line.split()[0]
    steps = int(line.split()[1])

    for step in range(steps):
        h_coord = move_head(h_coord, direction)
        t_coord = move_tail(h_coord, t_coord, direction)    
        if t_coord not in unique_t_coords:
            unique_t_coords.append(t_coord)

print('part1:', len(unique_t_coords))

rope = []
for i in range(10):
    rope.append((0,0))

unique_t_coords = [(0,0)]

for line in input_text:
    direction = line.split()[0]
    steps = int(line.split()[1])

    for step in range(steps):
        rope[0] = move_head(rope[0], direction)
        for i in range(len(rope)-1):
            rel_h_coord = rope[i]
            
            rel_t_coord = rope[i+1]
            rope[i+1] = move_tail(rel_h_coord, rel_t_coord, direction)

            print('direction:', direction, ',step:', step, ',i:', i, rope)
            input("Press Enter to continue...")
        if rope[9] not in unique_t_coords:
            unique_t_coords.append(rope[9])

print('part2:', len(unique_t_coords))
