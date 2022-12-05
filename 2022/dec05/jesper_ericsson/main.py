import numpy as np

import os
from collections import deque
import re


regex_moves = re.compile(r"move ([0-9]*) from ([0-9]*) to ([0-9]*)")


def read_data(filename):
    pile_strings = []
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if line.lstrip()[0] == "1":
                num_piles = int(line.rstrip()[-1])
                break
            else:
                pile_strings.append(line.rstrip("\n"))

            if not line:
                break
        f.readline()
        instruction_lines = f.readlines()

    piles = [deque() for _ in range(num_piles)]

    for line in reversed(pile_strings):
        for pile_ind, letter in enumerate(range(1, num_piles * 4, 4)):
            if line[letter].isalpha():
                piles[pile_ind].append(line[letter])

    moves = []
    for line in instruction_lines:
        moves.append([int(x) for x in regex_moves.search(line).groups()])

    return piles, moves


def move_pile_9000(number, in_queue, out_queue):
    for _ in range(number):
        out_queue.append(in_queue.pop())


def move_pile_9001(number, in_queue, out_queue):
    tmp_queue = deque()
    for _ in range(number):
        tmp_queue.append(in_queue.pop())

    for _ in range(number):
        out_queue.append(tmp_queue.pop())


def prob1(piles, moves):
    for move in moves:
        move_pile_9000(move[0], piles[move[1] - 1], piles[move[2] - 1])

    answer = ""
    for pile in piles:
        answer += pile.pop()
    print(f"Prob1: {answer}")


def prob2(piles, moves):
    for move in moves:
        move_pile_9001(move[0], piles[move[1] - 1], piles[move[2] - 1])

    answer = ""
    for pile in piles:
        answer += pile.pop()
    print(f"Prob2: {answer}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"
    piles, moves = read_data(filename)

    prob1(piles, moves)
    piles, moves = read_data(filename)
    prob2(piles, moves)


if __name__ == "__main__":
    main()
