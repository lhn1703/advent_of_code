import ast
import functools

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().split('\n\n')

def recursive_check(a, b):                              # returns true if a < b recursively
    check = None
    if type(a) is int and type(b) is int:
        if a > b:
            check = False
        elif a < b:
            check = True
    elif type(a) is list and type(b) is list:
        for aa, bb in zip(a,b):
            check = recursive_check(aa, bb)
            if check != None:
                break
        if check == None and len(a) > len(b):
            check = False
        elif check == None and len(a) < len(b):
            check = True
    elif type(a) is int and type(b) is list:
        check = recursive_check([a], b)
    elif type(a) is list and type(b) is int:
        check = recursive_check(a, [b])
    return check
    
pair_list = []
for pair in input_text:
    str0 = pair.split('\n')[0]
    str1 = pair.split('\n')[1]

    p0 = ast.literal_eval(str0)
    p1 = ast.literal_eval(str1)

    pair_list.append(recursive_check(p0,p1))


sum = 0
for i in range(len(pair_list)):
    if pair_list[i]:
        sum += i+1
print('part1', sum)


### PART 2 ###
with open('input.txt', 'r') as input_file:
    input_text = input_file.read().split()

input_text.append('[[2]]')
input_text.append('[[6]]')


def comparator_key(a, b):
    if a == b:
        return 0
    if recursive_check(a, b):
        return -1
    else:
        return 1

packet_list = []
for line in input_text:
    packet_list.append(ast.literal_eval(line))

packet_list = sorted(packet_list, key=functools.cmp_to_key(comparator_key))

product = 1
for i in range(len(packet_list)):
    if packet_list[i] == [[2]] or packet_list[i] == [[6]]:
        product *= i + 1

print('part2', product)
