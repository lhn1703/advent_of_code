with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

houses_dict = {}
x = 0
y = 0
origin_coord = (x,y)

houses_dict[origin_coord] = 1
houses_received = 1

for c in input_text:
    prev_coord = (x,y)

    if c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    elif c == '<':
        x -= 1
    elif c == '>':
        x += 1

    current_coord = (x,y)
    
    if current_coord in houses_dict:
        houses_dict[current_coord] += 1
    else:
        houses_dict[current_coord] = 1
        houses_received += 1

    # print(prev_coord, c, current_coord, houses_received) 

print('houses received:', houses_received)



with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

houses_dict = {}
s_x = 0
s_y = 0
r_x = 0
r_y = 0
origin_coord = (s_x,s_x)

houses_dict[origin_coord] = 2
houses_received = 1
s_move = True


for c in input_text:
    if s_move:
        if c == '^':
            s_y += 1
        elif c == 'v':
            s_y -= 1
        elif c == '<':
            s_x -= 1
        elif c == '>':
            s_x += 1
        x,y = s_x,s_y
    else:
        if c == '^':
            r_y += 1
        elif c == 'v':
            r_y -= 1
        elif c == '<':
            r_x -= 1
        elif c == '>':
            r_x += 1
        x,y = r_x,r_y

    current_coord = (x,y)
    
    if current_coord in houses_dict:
        houses_dict[current_coord] += 1
    else:
        houses_dict[current_coord] = 1
        houses_received += 1

    s_move = not s_move

    
print('houses received:', houses_received)

