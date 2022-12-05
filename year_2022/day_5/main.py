with open('test.txt', 'r') as input_file:
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


    

print(instruction_digits)