# just straight procedural programming for simple problems, can refactor if needed

# part 1
floor = 0

with open('input.txt', 'r') as input_file:
    input_string = input_file.read()

for char in input_string:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print('part 1 floor:', floor)

# part 2
floor = 0
char_position = 1

with open('input.txt', 'r') as input_file:
    input_string = input_file.read()

for char in input_string:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

    if floor == -1:
        break

    char_position += 1

print('part 2 char_position:', char_position)