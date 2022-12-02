def score_round(round):
    opponent_choice, my_choice = round.split(' ')

    if my_choice == 'X':
        if opponent_choice == 'A':
            score = 1 + 3
        elif opponent_choice == 'B':
            score = 1 + 0
        else:
            score = 1 + 6
    elif my_choice == 'Y':
        if opponent_choice == 'A':
            score = 2 + 6
        elif opponent_choice == 'B':
            score = 2 + 3
        else:
            score = 2 + 0
    else:
        if opponent_choice == 'A':
            score = 3 + 0
        elif opponent_choice == 'B':
            score = 3 + 6
        else:
            score = 3 + 3
    return score


def score_round_b(round):
    opponent_choice, my_choice = round.split(' ')

    if my_choice == 'X':
        if opponent_choice == 'A':
            score = 3 + 0
        elif opponent_choice == 'B':
            score = 1 + 0
        else:
            score = 2 + 0
    elif my_choice == 'Y':
        if opponent_choice == 'A':
            score = 1 + 3
        elif opponent_choice == 'B':
            score = 2 + 3
        else:
            score = 3 + 3
    else:
        if opponent_choice == 'A':
            score = 2 + 6
        elif opponent_choice == 'B':
            score = 3 + 6
        else:
            score = 1 + 6
    return score


rounds = []
with open('inputs/day2') as f:
    rounds = f.read().splitlines()


print(sum(score_round(round) for round in rounds))
print(sum(score_round_b(round) for round in rounds))
