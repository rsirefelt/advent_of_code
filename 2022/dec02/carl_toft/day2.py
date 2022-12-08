HAND_SCORE = {"X" : 1, "Y" : 2, "Z" : 3}
WINS = {("A", "Y"), ("B", "Z"), ("C", "X")}
DRAWS = {("A", "X"), ("B", "Y"), ("C", "Z")}
LOSSES = {("A", "Z"), ("B", "X"), ("C", "Y")}

def resolveRoundPart1(round):
    score = HAND_SCORE[round[1]]
    if round in LOSSES:
        return score
    if round in DRAWS:
        return score+3
    if round in WINS:
        return score+6

def resolveRoundPart2(round):
    if round[1] == "X":
        for hand in ["X", "Y", "Z"]:
            if (round[0], hand) in LOSSES:
                return resolveRoundPart1((round[0], hand))
        assert False
    if round[1] == "Y":
        for hand in ["X", "Y", "Z"]:
            if (round[0], hand) in DRAWS:
                return resolveRoundPart1((round[0], hand))
        assert False
    if round[1] == "Z":
        for hand in ["X", "Y", "Z"]:
            if (round[0], hand) in WINS:
                return resolveRoundPart1((round[0], hand))
        assert False

with open("input.txt") as f:
    lines = f.readlines()
lines = [line[:-1] for line in lines[:-1]]

data = [tuple(line.split(" ")) for line in lines]

total_score_part1 = 0
total_score_part2 = 0
for round in data:
    total_score_part1 = total_score_part1 + resolveRoundPart1(round)
    total_score_part2 = total_score_part2 + resolveRoundPart2(round)

print("Part 1: " + str(total_score_part1))
print("Part 2: " + str(total_score_part2))