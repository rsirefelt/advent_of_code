
ROCK = 0
PAPER = 1
SCISSORS = 2

LOST = 0
DRAW = 1
WIN = 2

SCORE_BY_PLAY = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}
SCORE_BY_OUTCOME = {
    LOST: 0,
    DRAW: 3,
    WIN: 6,
}


def op_to_enum(s : str) -> int:
    # A for Rock, B for Paper, and C for Scissors
    if s == "A":
        return ROCK
    elif s == "B":
        return PAPER
    elif s == "C":
        return SCISSORS
    raise NotImplemented()

def my_play_to_enum(s : str) -> int:
    # X for Rock, Y for Paper, and Z for Scissors
    if s == "X":
        return ROCK
    if s == "Y":
        return PAPER
    if s == "Z":
        return SCISSORS
    raise NotImplemented()


def play(op_play, me_play):
    if op_play == me_play:
        return DRAW
    if op_play == ROCK:
        return WIN if me_play == PAPER else LOST
    if op_play == PAPER:
        return WIN if me_play == SCISSORS else LOST
    if op_play == SCISSORS:
        return WIN if me_play == ROCK else LOST

with open("input.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        [op_play, my_play] = line.split()
        op_play = op_to_enum(op_play)
        my_play = my_play_to_enum(my_play)
        outcome = play(op_play, my_play)
        
        score += SCORE_BY_PLAY[my_play]
        score += SCORE_BY_OUTCOME[outcome]

print(score)

