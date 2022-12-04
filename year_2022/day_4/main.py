with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

def parse_line(line):
    elf1_range, elf2_range = line.split(',')

    elf1_begin, elf1_end = int(elf1_range.split('-')[0]), int(elf1_range.split('-')[1])
    elf2_begin, elf2_end = int(elf2_range.split('-')[0]), int(elf2_range.split('-')[1])

    elf1_ids = []
    elf2_ids = []

    for i in range(elf1_begin, elf1_end + 1):
        elf1_ids.append(i)
    for i in range(elf2_begin, elf2_end + 1):
        elf2_ids.append(i)

    return elf1_ids, elf2_ids

subset_count = 0
for line in input_text:
    elf1_ids, elf2_ids = parse_line(line)
    elf1_set, elf2_set = set(elf1_ids), set(elf2_ids)
    if elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set):
        subset_count += 1
print('part 1:', subset_count)

overlap_count = 0
for line in input_text:
    elf1_ids, elf2_ids = parse_line(line)
    elf1_set, elf2_set = set(elf1_ids), set(elf2_ids)
    if elf1_set.intersection(elf2_set) != set():                   # if their intersection is non-empty
        overlap_count += 1
print('part 2:', overlap_count)

