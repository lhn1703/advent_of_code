import re

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

nice_strings = 0
vowels = ('a', 'e', 'i', 'o', 'u')
naughty_substrings = ['ab', 'cd', 'pq', 'xy']


def check_string(s):
    vowel_count = 0
    for c in s:
        if c in vowels:
            vowel_count += 1
        if vowel_count == 3:
            break
    # regex tgat matches entire word that contains repeated character
    if not (re.match(r'\b(?=\w*(\w)\1)\w+\b', s)):
        return False
    for naughty_substring in naughty_substrings:
        if naughty_substring in s:
            return False

    if (vowel_count == 3):
        return True
    else:
        return False


for line in input_text:
    if check_string(line):
        nice_strings += 1

print(check_string('ugknbfddgicrmopn'))
print(check_string('jchzalrnumimnmhp'))
print(check_string('haegwjzuvuyypxyu'))
print(check_string('dvszwmarrgswjxmb'))
print(nice_strings)

with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

nice_strings_2 = 0
def check_string_2(s):
    found_pair = False
    char_pair = s[0]
    s_temp = s[1:]          # pop off first character

    # can't bother with creating a regex for this
    while len(s_temp) > 2:
        char_pair += s_temp[0]  # iterate over every character pairs in the string
        s_temp = s_temp[1:]
        if char_pair in s_temp:
            found_pair = True
            break
        char_pair = char_pair[1]    # pop out the first character in pair

    if not re.match(r'\b.*(\w).\1.*\b', s):
        return False
        
    if not found_pair:
        return False
    else: 
        return True

for line in input_text:
    if check_string_2(line):
        nice_strings_2 += 1

print(check_string_2('qjhvhtzxzqqjkmpb'))
print(check_string_2('xxyxx'))
print(check_string_2('uurcxstgmygtbstg'))
print(check_string_2('ieodomkazucvgmuy'))
print(nice_strings_2)
