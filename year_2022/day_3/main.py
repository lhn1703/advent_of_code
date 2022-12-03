with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

def get_duplicate_char(string_1, string_2):
    unique_char_list_1 = set(string_1)
    unique_char_list_2 = set(string_2)

    for char in unique_char_list_1:
        if char in unique_char_list_2:
            return char

def get_points_from_char(c):
    ascii_value = ord(c)
    if c.isupper():
        ascii_value -= 38
    else:
        ascii_value -= 96
    return ascii_value

sum = 0

for line in input_text:
    string_1, string_2 = line[:len(line)//2], line[len(line)//2:]
    duplicate_char = get_duplicate_char(string_1, string_2)
    points = get_points_from_char(duplicate_char)
    sum += points

print('sum', sum)

def get_duplicate_char_3(string_1, string_2, string_3):
    unique_char_list_1 = set(string_1)
    unique_char_list_2 = set(string_2)
    unique_char_list_3 = set(string_3)

    for char in unique_char_list_1:
        if char in unique_char_list_2:
            if char in unique_char_list_3:
                return char
    
sum = 0
group = []

for line in input_text:
    group.append(line)

    if len(group) == 3:
        duplicate_char = get_duplicate_char_3(group[0], group[1], group[2])
        points = get_points_from_char(duplicate_char)
        sum += points
        group = []

print('sum', sum)
