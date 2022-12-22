import parse
from itertools import combinations

with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

y_pos = 10

min_x = None
max_x = None
min_y = None
max_y = None

map = {}
sensor_list = []

def mhd(x0, y0, x1, y1):
    return abs(x1 - x0) + abs(y1 - y0)

class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y, manhattan_distance) -> None:
        self.sensor_x = sensor_x
        self.sensor_y = sensor_y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.manhattan_distance = manhattan_distance
    perimeter = None

# first pass to map the initial board
for line in input_text:
    sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
    sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)

    map[(sensor_x, sensor_y)] = 'S'
    map[(beacon_x, beacon_y)] = 'B'

    manhattan_distance = mhd(sensor_x, sensor_y, beacon_x, beacon_y)

    sensor = Sensor(sensor_x, sensor_y, beacon_x, beacon_y, manhattan_distance)
    sensor_list.append(sensor)

    if min_x == None or sensor_x - manhattan_distance < min_x:
        min_x = sensor_x - manhattan_distance
    if min_y == None or sensor_y - manhattan_distance < min_y:
        min_y = sensor_y - manhattan_distance
    if max_x == None or sensor_x + manhattan_distance > max_x:
        max_x = sensor_x + manhattan_distance
    if max_y == None or sensor_y + manhattan_distance > max_y:
        max_y = sensor_y + manhattan_distance



sum = 0
for x in range(min_x, max_x + 1):
    current_coord = (x, y_pos)
    if current_coord in map.keys():
        continue
    
    for sensor in sensor_list:
        sensor_x = sensor.sensor_x
        sensor_y = sensor.sensor_y
        current_mhd = mhd(x, y_pos, sensor_x, sensor_y)
        if current_mhd <= sensor.manhattan_distance:
            map[current_coord] = '#'
            sum += 1
            continue

print('part1', sum)

### PART 2 ALGORITHM ###
# solution from https://www.youtube.com/watch?v=w7m48_uCvWI 
# each sensor has a manhattan perimiter that is diamond shaped
# y - y0 = m(x - x0) + d
# m = ± 1
# d = ± manhattan distance
# at sensor location (x0, y0)
# positive line eqn: y = x + (-x0 + y0 ± d)
# negative line eqn: y = -x + (x0 + y0 ± d)
# find the points where a pair of positive lines have a gap of 2
    # out of those points find the point where the a pair of negative lines have a gap of 2
        # verify that this point is not wihtin manhattan distance of any sensor

negative_line_intercepts = []
positive_line_intercepts = []

for line in input_text:
    sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
    sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
    manhattan_distance = mhd(sensor_x, sensor_y, beacon_x, beacon_y)

    positive_line_intercepts.append(-sensor_x + sensor_y + manhattan_distance)
    positive_line_intercepts.append(-sensor_x + sensor_y - manhattan_distance)
    negative_line_intercepts.append(sensor_x + sensor_y + manhattan_distance)
    negative_line_intercepts.append(sensor_x + sensor_y - manhattan_distance)

neg_intercept_combinations = combinations(negative_line_intercepts, 2)
pos_intercept_combinations = combinations(positive_line_intercepts, 2)

pos_intercept_candidates = []
neg_intercept_candidates = []

# the solution must be in between these intercept pairs
for combo in pos_intercept_combinations:
    intercept0, intercept1 = combo
    if abs(intercept0 - intercept1) == 2:
        pos_intercept_candidates.append(combo)
for combo in neg_intercept_combinations:
    intercept0, intercept1 = combo
    if abs(intercept0 - intercept1) == 2:
        neg_intercept_candidates.append(combo)

