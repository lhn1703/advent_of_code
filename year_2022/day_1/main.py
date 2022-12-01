with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

calorie_list = []
cal = 0

for line in input_text:
    if line != '':
        cal += int(line)
    else:
        calorie_list.append(cal)
        cal = 0
calorie_list.append(cal)                    # append the last line of the file since it doesn't end with a ''
print('max calories: {}'.format(max(calorie_list)))

top_3_cal = sorted(calorie_list)[-3:]
print('top 3 calories sum', top_3_cal, sum(top_3_cal))
    

    