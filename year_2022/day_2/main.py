with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

total_score = 0

for line in input_text:
    round_score = 0
    
    opponent_move = line.split()[0]
    player_move = line.split()[1]

    total_score += round_score

    
    