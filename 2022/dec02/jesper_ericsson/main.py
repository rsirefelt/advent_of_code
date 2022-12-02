import numpy as np


def read_data(filename):
    strategies = []
    with open(filename, "r") as f:
        data_lines = f.readlines()
        for string in data_lines:
            strategies.append(string.rstrip().split())

    return strategies


def calc_score(round):
    player = round[1]
    opponent = round[0]
    score = 0
    if player == "X":
        score += 1
        if opponent == "A":
            score += 3
        elif opponent == "C":
            score += 6
    elif player == "Y":
        score += 2
        if opponent == "B":
            score += 3
        elif opponent == "A":
            score += 6
    elif player == "Z":
        score += 3
        if opponent == "C":
            score += 3
        elif opponent == "B":
            score += 6

    return score


def create_round(strategy):
    opponent = strategy[0]
    result = strategy[1]

    player = ""
    if opponent == "A":
        if result == "X":
            player = "Z"
        elif result == "Y":
            player = "X"
        else:
            player = "Y"
    elif opponent == "B":
        if result == "X":
            player = "X"
        elif result == "Y":
            player = "Y"
        else:
            player = "Z"
    elif opponent == "C":
        if result == "X":
            player = "Y"
        elif result == "Y":
            player = "Z"
        else:
            player = "X"

    return opponent, player


def prob1(strategies):
    tot_score = 0
    for strategy in strategies:
        tot_score += calc_score(strategy)
    print(f"Total score prob 1: {tot_score}")


def prob2(strategies):
    tot_score = 0
    for strategy in strategies:
        round = create_round(strategy)
        tot_score += calc_score(round)
    print(f"Total score prob 2: {tot_score}")


def main():
    filename = "testdata.csv"
    filename = "data.csv"

    strategies = read_data(filename)

    prob1(strategies)
    prob2(strategies)


if __name__ == "__main__":
    main()
