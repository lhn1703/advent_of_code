with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

lights_lit = 0
grid = [[0]*1000 for i in range(1000)]      # creates a 1000x1000 2d array initialized to 0s

for line in input_text:
    first_pair = None
    second_pair = None

    temp_split = line.split()
    for possible_pair in temp_split:
        if possible_pair[0].isdigit():
            if first_pair == None:
                first_pair = possible_pair
            else:
                second_pair = possible_pair

    x0, y0 = first_pair.split(',')
    x1, y1 = second_pair.split(',')
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    if 'toggle' in line:
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] ^= 1             # X ^ 1 = !X
    elif 'turn on' in line:
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] = 1            
    elif 'turn off' in line:
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] = 0         
    
for i in range(1000):
    for j in range(1000):
        if grid[i][j] == 1:
            lights_lit += 1

print(lights_lit)

brightness = 0
grid = [[0]*1000 for i in range(1000)]      # creates a 1000x1000 2d array initialized to 0s

for line in input_text:
    first_pair = None
    second_pair = None

    temp_split = line.split()
    for possible_pair in temp_split:
        if possible_pair[0].isdigit():
            if first_pair == None:
                first_pair = possible_pair
            else:
                second_pair = possible_pair

    x0, y0 = first_pair.split(',')
    x1, y1 = second_pair.split(',')
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

    if 'toggle' in line:
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] += 2             
    elif 'turn on' in line:
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] += 1            
    elif 'turn off' in line:
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                if grid[i][j] > 0:              # minimum brightness == 0
                    grid[i][j] -= 1    

    
for i in range(1000):
    for j in range(1000):
        brightness += grid[i][j]

print(brightness)