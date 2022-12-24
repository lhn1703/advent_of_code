import parse
from itertools import product

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

boundary = 4000000
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

# ax + by = c
class Line:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

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
'''
every sensor has a perimeter that is shaped like a paralellogram
each of the lines of that perimeter has a slope of 1 or -1
point slope form: y - y0 = m(x - x0) + d
    sensor origin = (x0,y0) 
    slope m = 1 or -1
    intercept d = (mhd+1) or -(mhd+1)
convert line to ax + by = c and extract a,b,c
    positive lines: -1x + 1y = -x0 + y0 +- d
        a = -1
        b = 1
        c = -x0 + y0 +- d
    negative lines: 1x + 1y = x0 + y0 +- d
        a = 1
        b = 1
        c = x0 + y0 +- d
cramer's rule intersection point: (x,y) = ((c1*b2-b1*c2)/(a1*b2-b1*a2), (a1*c2-c1*a2)/(a1*b2-b1*a2))
search through every possible intersection points by taking permutations of the two lines lists
    if intersection point:
        check if point falls within boundaries
        check if it is not detected by any sensor at all
'''

intersection_points = []
pos_lines = []
neg_lines = []

for line in input_text:
    sensor_x, sensor_y, beacon_x, beacon_y = parse.parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
    sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
    manhattan_distance = mhd(sensor_x, sensor_y, beacon_x, beacon_y) + 1 # looking for line just outside mhd

    pos_line1 = Line(-1, 1, -sensor_x + sensor_y + manhattan_distance)
    pos_line2 = Line(-1, 1, -sensor_x + sensor_y - manhattan_distance)
    neg_line1 = Line(1, 1, sensor_x + sensor_y + manhattan_distance)
    neg_line2 = Line(1, 1, sensor_x + sensor_y - manhattan_distance)

    pos_lines.append(pos_line1)
    pos_lines.append(pos_line2)
    neg_lines.append(neg_line1)
    neg_lines.append(neg_line2)

line_pairs = list(product(pos_lines, neg_lines))
line_pairs = list(set(line_pairs))                  # removes all duplicate points

for line_pair in line_pairs:
    line1, line2 = line_pair
    a1, b1, c1 = line1.a, line1.b, line1.c
    a2, b2, c2 = line2.a, line2.b, line2.c

    x, y = (c1*b2-b1*c2)/(a1*b2-b1*a2), (a1*c2-c1*a2)/(a1*b2-b1*a2)

    if x % 1 != 0 or y % 1 != 0:        # check if they are both integers
        continue
    if not (0 <= x <= boundary and 0 <= y <= boundary) :  # check if they both are within the boundary
        continue

    point = (int(x), int(y))
    intersection_points.append(point)

intersection_points = list(set(intersection_points))    # remove duplicates
solution_point = None
for point in sorted(intersection_points):
    found = True
    for sensor in sensor_list:
        x0, y0 = point
        x1, y1 = sensor.sensor_x, sensor.sensor_y
        current_mhd = mhd(x0, y0, x1, y1)
        sensor_mhd = sensor.manhattan_distance
        if current_mhd <= sensor_mhd:
            found = False
            break
    if found:
        solution_point = point
        break

x, y = solution_point
print('part2', solution_point, x * 4000000 + y)