import parse
from tqdm import tqdm
import time

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

y_pos = 2000000

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

start_time = time.time()

sum = 0
for x in range(min_x, max_x + 1):
    current_coord = (x, y_pos)
    
    for sensor in sensor_list:
        if current_coord in map.keys():
            continue
        sensor_x = sensor.sensor_x
        sensor_y = sensor.sensor_y
        current_mhd = mhd(x, y_pos, sensor_x, sensor_y)
        if current_mhd <= sensor.manhattan_distance:
            map[current_coord] = '#'
            sum += 1

print('part1', sum, 'time:', time.time() - start_time)




