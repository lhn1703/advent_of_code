import parse

with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

min_x = None
max_x = None
min_y = None
max_y = None

map = {}

# first pass to map the initial board
for line in input_text:
    sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
    sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)

    # map[(sensor_x, sensor_y)] = 'S'
    # map[(beacon_x, beacon_y)] = 'B'

    manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

    if min_x == None or sensor_x - manhattan_distance < min_x:
        min_x = sensor_x - manhattan_distance
    if min_y == None or sensor_y - manhattan_distance < min_y:
        min_y = sensor_y - manhattan_distance
    if max_x == None or sensor_x + manhattan_distance > max_x:
        max_x = sensor_x + manhattan_distance
    if max_y == None or sensor_y + manhattan_distance > max_y:
        max_y = sensor_y + manhattan_distance

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        map[(x,y)] = '.'

def recursive_scan(x0, y0, x1, y1, manhattan_distance):
    current_mhd = abs(x1 - x0) + abs(y1 - y0)
    print(x0, y0, x1, y1, manhattan_distance, current_mhd)
    if current_mhd > manhattan_distance:
        return
    
    if map[(x1,y1)] == '.':
        map[(x1,y1)] = '#'
    
    # recusively check all four adjacent quadrants of the origin
    recursive_scan(x0, y0, x1-1, y1, manhattan_distance)
    recursive_scan(x0, y0, x1+1, y1, manhattan_distance)
    recursive_scan(x0, y0, x1, y1-1, manhattan_distance)
    recursive_scan(x0, y0, x1, y1+1, manhattan_distance)


# second pass to perform aglorithm
# for line in input_text:
#     sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
#     sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
#     manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

#     map[(sensor_x, sensor_y)] = 'S'
#     map[(beacon_x, beacon_y)] = 'B'

#     # current_x, current_y = sensor_x, sensor_y

#     recursive_scan(sensor_x, sensor_y, sensor_x, sensor_y, manhattan_distance)

line = input_text[6]
sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

map[(sensor_x, sensor_y)] = 'S'
map[(beacon_x, beacon_y)] = 'B'

# current_x, current_y = sensor_x, sensor_y

recursive_scan(sensor_x, sensor_y, sensor_x, sensor_y, manhattan_distance)
    
for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        print(map[(x,y)], end='')
    print('\n')

