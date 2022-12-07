with open('input.txt', 'r') as input_file:
    input_text = input_file.read()

begin = 0
end = 4
index = 4

for i in range(len(input_text)):
    marker_window = input_text[begin:end]
    if len(set(marker_window)) == 4:
        break
    begin += 1
    end += 1 
    index += 1

print('part1:', index)

begin = 0
end = 14
index = 14

for i in range(len(input_text)):
    marker_window = input_text[begin:end]
    if len(set(marker_window)) == 14:
        break
    begin += 1
    end += 1 
    index += 1

print('part2:', index)