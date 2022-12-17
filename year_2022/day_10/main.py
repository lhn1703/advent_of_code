with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

def parse_line(line):
    if line == 'noop':
        return 'noop', None
    else:
        return 'addx', int(line.split()[1])

instruction_program = []
for line in input_text:
    op, value = parse_line(line)
    instruction = (op, value)
    instruction_program.append(instruction)

sum = 0
current_cycle = 1
rx = 1
cycle_check = [20, 60, 100, 140, 180, 220]

while instruction_program != []:
    current_instruction = instruction_program.pop(0)
    op, value = current_instruction

    current_cycle += 1
    if current_cycle in cycle_check:
        sum += rx * current_cycle   
        print('sum', current_cycle, rx, rx*current_cycle) 

    if op == 'noop':
        pass
    elif op == 'addx':
        current_cycle += 1
        rx += value
        print(current_cycle, rx)
        if current_cycle in cycle_check:
            sum += rx * current_cycle   
            print('sum', current_cycle, rx, rx*current_cycle) 

    print(current_cycle, rx)

print('part1', sum)


# current_cycle = 1
# rx = 1
# line = ['........................................']



#     print(current_cycle, rx)

