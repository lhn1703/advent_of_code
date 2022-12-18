import ast

with open('test.txt', 'r') as input_file:
    input_text = input_file.read().split('\n\n')

def recursive_check(a, b):
    print(a,b)
    if type(a) is int and type(b) is int:
        if a > b:
            print('here', a, b)
            return False
    if type(a) is list and type(b) is list:
        for aa, bb in zip(a, b):                    # recursively check nested lists
            recursive_check(aa, bb)
            print('here0',aa,bb)
        if type(a) is list and type(b) is list:
            if len(a) <= len(b):
                return True                             # if run out of nested values to check, then check if first list runs out first
            else:
                return False
    if type(a) is list and type(b) is int:
        bb = [b]
        return recursive_check(a, bb)
    if type(a) is int and type(b) is list:
        aa = [a]
        return recursive_check(aa, b)
    

for pair in input_text:
    str0 = pair.split('\n')[0]
    str1 = pair.split('\n')[1]

    p0 = ast.literal_eval(str0)
    p1 = ast.literal_eval(str1)

    print(recursive_check(p0, p1))

# print(recursive_check([9],[8]))
