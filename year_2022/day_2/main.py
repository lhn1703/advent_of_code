with open('input.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'lose': 0,
    'draw': 3,
    'win': 6
}

total_score = 0

for line in input_text:
    round_score = 0

    opponent_move = line.split()[0]
    player_move = line.split()[1]

    if opponent_move == 'A':                                            # rock 
        if player_move == 'X':                              # rock
            round_score = points['draw'] + points['rock']
        elif player_move == 'Y':                            # paper
            round_score = points['win'] + points['paper']
        elif player_move == 'Z':                            # scissors
            round_score = points['lose'] + points['scissors']
    elif opponent_move == 'B':                                          # paper
        if player_move == 'X':                              # rock
            round_score = points['lose'] + points['rock']
        elif player_move == 'Y':                            # paper
            round_score = points['draw'] + points['paper']
        elif player_move == 'Z':                            # scissors
            round_score = points['win'] + points['scissors']
    elif opponent_move == 'C':                                          # scissors
        if player_move == 'X':                              # rock
            round_score = points['win'] + points['rock']
        elif player_move == 'Y':                            # paper
            round_score = points['lose'] + points['paper']
        elif player_move == 'Z':                            # scissors
            round_score = points['draw'] + points['scissors']

    total_score += round_score

print('part 1 total score:', total_score)

total_score = 0

for line in input_text:
    round_score = 0

    opponent_move = line.split()[0]
    player_move = line.split()[1]

    if opponent_move == 'A':                                        # rock 
        if player_move == 'X':                                          # lose
            round_score = points['lose'] + points['scissors']
        elif player_move == 'Y':                                        # draw
            round_score = points['draw'] + points['rock']
        elif player_move == 'Z':                                        # win
            round_score = points['win'] + points['paper']
    elif opponent_move == 'B':                                      # paper
        if player_move == 'X':                                          # lose
            round_score = points['lose'] + points['rock']
        elif player_move == 'Y':                                        # draw
            round_score = points['draw'] + points['paper']
        elif player_move == 'Z':                                        # win
            round_score = points['win'] + points['scissors']
    elif opponent_move == 'C':                                      # scissors
        if player_move == 'X':                                          # lose
            round_score = points['lose'] + points['paper']
        elif player_move == 'Y':                                        # draw
            round_score = points['draw'] + points['scissors']
        elif player_move == 'Z':                                        # win
            round_score = points['win'] + points['rock']
            
    total_score += round_score

print('part 2 total score:', total_score)


    
    