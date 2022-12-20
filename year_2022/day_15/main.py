import parse
from tqdm import tqdm

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

min_x = None
max_x = None
min_y = None
max_y = None

map = {}

# first pass to map the initial board
for line in tqdm(input_text, desc='init:'):
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

for y in tqdm(range(min_y, max_y+1), desc='y init:'):
    for x in tqdm(range(min_x, max_x+1), desc='x init:'):
        map[(x,y)] = '.'

def scan_range(x0, y0, manhattan_distance):
    for x1 in tqdm(range(x0 - manhattan_distance, x0 + manhattan_distance + 1), 'x'):
        for y1 in range(y0 - manhattan_distance, y0 + manhattan_distance + 1):
            current_mhd = abs(x1 - x0) + abs(y1 - y0)
            if current_mhd > manhattan_distance:
                continue
            elif (x1,y1) not in map.keys():
                map[(x1,y1)] = '#'
    


# second pass to perform aglorithm
for line in tqdm(input_text, desc='line:'):
    sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
    sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
    manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

    map[(sensor_x, sensor_y)] = 'S'
    map[(beacon_x, beacon_y)] = 'B'

    current_x, current_y = sensor_x, sensor_y
    scan_range(current_x, current_y, manhattan_distance)

# for y in range(min_y, max_y+1):
#     for x in range(min_x, max_x+1):
#         print(map[(x,y)], end='')
#     print('\n')

sum = 0
for x in range(min_x, max_x+1):
    if (x,2000000) in map.keys() and map[(x,10)] == '#':
        sum += 1
print('part1', sum)

