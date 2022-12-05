def part_1(input):
    score = 0
    for line in input:
        split = line.strip().split(" ")
        opponent, play = split[0], split[1]
        if opponent == "A" and play == "X":
            score += 3 + 1
        elif opponent == "A" and play == "Y":
            score += 6 + 2
        elif opponent == "A" and play == "Z":
            score += 0 + 3
        elif opponent == "B" and play == "X":
            score += 0 + 1
        elif opponent == "B" and play == "Y":
            score += 3 + 2
        elif opponent == "B" and play == "Z":
            score += 6 + 3
        elif opponent == "C" and play == "X":
            score += 6 + 1
        elif opponent == "C" and play == "Y":
            score += 0 + 2
        elif opponent == "C" and play == "Z":
            score += 3 + 3
        else:
            raise Exception("Non-handled case")

    print("Score part 1: " + str(score))


def part_2(input):
    score = 0
    for line in input:
        split = line.strip().split(" ")
        opponent, instruction = split[0], split[1]
        if opponent == "A" and instruction == "X":
            score += 0 + 3
        elif opponent == "A" and instruction == "Y":
            score += 3 + 1
        elif opponent == "A" and instruction == "Z":
            score += 6 + 2
        elif opponent == "B" and instruction == "X":
            score += 0 + 1
        elif opponent == "B" and instruction == "Y":
            score += 3 + 2
        elif opponent == "B" and instruction == "Z":
            score += 6 + 3
        elif opponent == "C" and instruction == "X":
            score += 0 + 2
        elif opponent == "C" and instruction == "Y":
            score += 3 + 3
        elif opponent == "C" and instruction == "Z":
            score += 6 + 1
        else:
            raise Exception("Non-handled case")

    print("Score part 2: " + str(score))


if __name__ == "__main__":
    input = []
    with open("input") as f:
        input = f.readlines()

    part_1(input)
    part_2(input)
