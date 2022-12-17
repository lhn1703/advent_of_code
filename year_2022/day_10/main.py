with open('input.txt', 'r') as input_file:
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

    # print(current_cycle, rx)


    if current_cycle in cycle_check:
        sum += rx * current_cycle   
        # print('sum', current_cycle, rx, rx*current_cycle) 

    if op == 'noop':
        current_cycle += 1
    elif op == 'addx':
        current_cycle += 1
        if current_cycle in cycle_check:
            sum += rx * current_cycle   
            # print('sum', current_cycle, rx, rx*current_cycle) 

        # print(current_cycle, rx)
        current_cycle += 1
        rx += value
        # print(current_cycle, rx)
        
print('part1', sum)

current_cycle = 1
rx = 1
sprite_position = []
crt = ["." for i in range(40)]

instruction_program = []
for line in input_text:
    op, value = parse_line(line)
    instruction = (op, value)
    instruction_program.append(instruction)

while instruction_program != []:
    current_instruction = instruction_program.pop(0)
    op, value = current_instruction

    if rx == -1:
        sprite_position = [0]
    elif rx == 0:
        sprite_position = [0,1]
    elif rx == 40:
        sprite_position = [39]
    elif rx == 39:
        sprite_position = [38, 39]
    else:
        sprite_position = [rx-1, rx, rx+1]

    # for i in range(len(crt)):
    #     if crt[i] == 's' or crt[i] == 'o':
    #         crt[i] = '.'

    # for s in sprite_position:
    #     crt[s] = 's'
    # crt[current_cycle-1] = 'o'



    if current_cycle-1 in sprite_position:
        crt[current_cycle-1] = '#'
    if current_cycle % 40 == 0:
        current_cycle -= 40
        print(''.join(crt))
        crt = ["." for i in range(40)]

    # print('cycle:', current_cycle, op, value, sprite_position)
    # print(''.join(crt))
    # input('outside loop\n')

    if op == 'noop':
        current_cycle += 1
    elif op == 'addx':
        current_cycle += 1

        # for i in range(len(crt)):
        #     if crt[i] == 'o':
        #         crt[i] = '.'
        # crt[current_cycle-1] = 'o'

        if current_cycle-1 in sprite_position:
            crt[current_cycle-1] = '#'
        if current_cycle % 40 == 0:
            current_cycle -= 40
            print(''.join(crt)) 
            crt = ["." for i in range(40)]

        # print('cycle:', current_cycle, op, value, sprite_position)
        # print(''.join(crt))
        # input('second addx\n')

        
        current_cycle += 1
        rx += value


        
        

