import parse
from itertools import combinations, permutations

with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

boundary = 20
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

# sum = 0
# for x in range(min_x, max_x + 1):
#     current_coord = (x, y_pos)
    
#     for sensor in sensor_list:
#         if current_coord in map.keys():
#             continue
#         sensor_x = sensor.sensor_x
#         sensor_y = sensor.sensor_y
#         current_mhd = mhd(x, y_pos, sensor_x, sensor_y)
#         if current_mhd <= sensor.manhattan_distance:
#             map[current_coord] = '#'
#             sum += 1

# print('part1', sum)


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

    print('sensor ({},{}), d={}, pos={},{}; neg={},{}'.format(sensor_x, sensor_y, manhattan_distance, -sensor_x + sensor_y + manhattan_distance, -sensor_x + sensor_y - manhattan_distance, sensor_x + sensor_y + manhattan_distance, sensor_x + sensor_y - manhattan_distance))

positive_line_intercepts = list(set(positive_line_intercepts))
negative_line_intercepts = list(set(negative_line_intercepts))

p_temp = []
n_temp = []
for i in range(len(positive_line_intercepts)):
    if 0 <= positive_line_intercepts[i] <= boundary:
        p_temp.append(positive_line_intercepts[i])
for i in range(len(negative_line_intercepts)):
    if 0 <= negative_line_intercepts[i] <= boundary:
        n_temp.append(negative_line_intercepts[i])

positive_line_intercepts = p_temp
negative_line_intercepts = n_temp


print(sorted(positive_line_intercepts))
print(sorted(negative_line_intercepts))

neg_intercept_combinations = list(combinations(negative_line_intercepts, 2))
pos_intercept_combinations = list(combinations(positive_line_intercepts, 2))

# print(pos_intercept_combinations)
# print(neg_intercept_combinations)

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

# the point must be vertical midpoint between two positive intercept candidate pairs
# the point must be the horizontal midpoint between two negative intercept candidate pairs


beacon_candidates = []
for pos_combo in pos_intercept_candidates:
    pos1, pos2 = pos_combo
    x = (pos1 + pos2) / 2
    for neg_combo in neg_intercept_candidates:
        neg1, neg2 = neg_combo
        y = (neg1 + neg2) / 2
        beacon_candidates.append((x,y))

beacon_candidates = list(set(beacon_candidates))

for b in beacon_candidates:
    print(b)

for beacon_candidate in beacon_candidates:
    found = True
    beacon_x, beacon_y = beacon_candidate
    for sensor in sensor_list:
        sensor_x = sensor.sensor_x
        sensor_y = sensor.sensor_y
        current_mhd = mhd(beacon_x, beacon_y, sensor_x, sensor_y)
        if current_mhd <= sensor.manhattan_distance:
            found = False
            break
    if found:
        print('part2', beacon_candidate)
        break
            

