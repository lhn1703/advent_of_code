with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

def move(h_coord, t_coord, direction):            # can only move 1 tile at a time
    hx, hy = h_coord
    tx, ty = t_coord

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
    
    new_h_coord = (hx, hy)
    new_t_coord = (tx, ty)

    return new_h_coord, new_t_coord

h_coord = (0,0)
t_coord = (0,0)

unique_t_coords = [t_coord]

for line in input_text:
    direction = line.split()[0]
    steps = int(line.split()[1])

    for step in range(steps):
        h_coord, t_coord = move(h_coord, t_coord, direction)
        if t_coord not in unique_t_coords:
            unique_t_coords.append(t_coord)

print('part1:', len(unique_t_coords))

# rope = []
# for i in range(10):
#     rope.append((0,0))

# unique_t_coords = [(0,0)]

# for line in input_text:
#     direction = line.split()[0]
#     steps = int(line.split()[1])

#     for i in range(len(rope)-1):
#         current_h_coord = rope[i]
#         current_t_coord = rope[i+1]

#         for step in range(steps):
#             new_h_coord, new_t_coord = move(h_coord, t_coord, direction)
#             rope[i] = new_h_coord
#             rope[i+1] = new_t_coord
#             print(current_h_coord, current_h_coord, new_h_coord, new_t_coord)

#         if rope[9] not in unique_t_coords:
#             unique_t_coords.append(rope[9])


# print('part2:', len(unique_t_coords))
