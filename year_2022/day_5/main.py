with open('input.txt', 'r') as input_file:
    input_text = input_file.read()
initial_state = input_text.split('\n\n')[0].splitlines()
instructions = input_text.split('\n\n')[1].splitlines()

board_state = {}

stack_indices = []
crate_positions = []                
crates_line = initial_state[-1]

for i in range (len(crates_line)):
    if crates_line[i].isdigit():
        stack_indices.append(i)
        crate_positions.append(crates_line[i])

crate_positions = [int(x) for x in crate_positions]
stack_indices = [int(x) for x in stack_indices]

for crate_position in crate_positions:
    board_state[crate_position] = []

initial_state.pop() 
for line in reversed(initial_state):
    for stack_index, crate_position in zip(stack_indices, crate_positions):
        if line[stack_index].isalpha():
            board_state[crate_position].append(line[stack_index])

for line in instructions:
    instruction = line.split()
    instruction_n = []
    for s in instruction:
        if s.isdigit():
            instruction_n.append(int(s))

    move_amount = instruction_n[0]
    source = instruction_n[1]
    destination = instruction_n[2]

    for i in range(move_amount):
        crate = board_state[source].pop()
        board_state[destination].append(crate)

s = ''
for i in crate_positions:
    s += board_state[i][-1]

print('part1:', s)

# resetting the board state
board_state = {}
for crate_position in crate_positions:
    board_state[crate_position] = []

for line in reversed(initial_state):
    for stack_index, crate_position in zip(stack_indices, crate_positions):
        if line[stack_index].isalpha():
            board_state[crate_position].append(line[stack_index])

for line in instructions:
    instruction = line.split()
    instruction_n = []
    for s in instruction:
        if s.isdigit():
            instruction_n.append(int(s))

    move_amount = instruction_n[0]
    source = instruction_n[1]
    destination = instruction_n[2]

    crates = board_state[source][-move_amount:]
    board_state[source] = board_state[source][:-move_amount]
    board_state[destination].extend(crates)



s = ''
for i in crate_positions:
    s += board_state[i][-1]

print('part2:', s)