with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

def move_head(h_coord, direction):
    hx, hy = h_coord
    if direction == 'R':
        hx += 1
    elif direction == 'L':
        hx -= 1
    elif direction == 'D':
        hy -= 1
    elif direction == 'U':
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

    tail_diagonals = [
        (tx-1, ty+1),
        (tx+1, ty+1),
        (tx-1, ty-1),
        (tx+1, ty-1)
    ]

    if t_coord in adjacent_coordinates:
        pass
    elif hx == tx:                                      # check if head is same row/column as tail and find the nearest adjacent point
        if (tx, ty-1) in adjacent_coordinates:
            ty -= 1
        else:
            ty += 1
    elif hy == ty:
        if (tx-1, ty) in adjacent_coordinates:
            tx -= 1
        else:
            tx += 1
    else:                                               # move tail by one diagonal adjacent to head
        for diagonal in tail_diagonals:
            if diagonal in adjacent_coordinates:
                tx, ty = diagonal
        
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
        if rope[9] not in unique_t_coords:
            unique_t_coords.append(rope[9])
print('part2:', len(unique_t_coords))
