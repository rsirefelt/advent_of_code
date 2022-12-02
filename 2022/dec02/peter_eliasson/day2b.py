
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

def outcome_to_enum(s : str) -> int:
    # X means you need to lose, Y means you need to end the round in
    # a draw, and Z means you need to win.
    if s == "X":
        return LOST
    if s == "Y":
        return DRAW
    if s == "Z":
        return WIN
    raise NotImplemented()


def determine_my_play(op_play, outcome):
    if outcome == DRAW:
        return op_play
    if op_play == ROCK:
        return PAPER if outcome == WIN else SCISSORS
    if op_play == PAPER:
        return SCISSORS if outcome == WIN else ROCK
    if op_play == SCISSORS:
        return ROCK if outcome == WIN else PAPER


with open("input.txt") as f:
    score = 0
    for line in f:
        line = line.strip()
        [op_play, outcome] = line.split()
        op_play = op_to_enum(op_play)
        outcome = outcome_to_enum(outcome)
        my_play = determine_my_play(op_play, outcome)
        
        score += SCORE_BY_PLAY[my_play]
        score += SCORE_BY_OUTCOME[outcome]

print(score)

