""" Advent of Code Day 5 """
import numpy as np


def decode_seat(seat):
    bits = ['0' if c in ['F', 'L'] else '1' for c in seat]
    row = int(''.join(bits[:7]), base=2)
    col = int(''.join(bits[7:]), base=2)
    sid = 8*row + col
    return sid


def parse_input(input_file='input_day5.txt'):
    with open(input_file, 'r') as fp:
        seats = fp.read().splitlines()

    return seats


if __name__ == "__main__":
    seats = parse_input()

    # Part I
    sids = np.array([decode_seat(s) for s in seats])
    print(np.max(sids))

    # Part II
    sids = np.sort(sids)
    ind = np.where(np.diff(sids) == 2)[0][0]
    my_sid = sids[ind] + 1
    print(my_sid)
