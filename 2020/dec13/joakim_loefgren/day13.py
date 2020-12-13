""" Advent of Code Day 13 """
import numpy as np


def load_input(input_file):
    with open(input_file) as fp:
        lines = fp.read().splitlines()
    t_depart = int(lines[0])
    t_schedule = lines[1].split(",")
    return t_depart, t_schedule


if __name__ == "__main__":
    t_depart, t_schedule = load_input("./input_day13.txt")
    busses = np.array([int(t) for t in t_schedule if t != "x"])

    # Part I
    runs = t_depart // busses
    if np.any(runs) == 0:
        res = 0
    else:
        t_wait = busses * (1 + runs) - t_depart
        imin = np.argmin(t_wait)
        res = busses[imin] * t_wait[imin]
    print(res)

    # Part II
    # Iteratively find a departure time consistent with the constraints.
    # A time compatible with busses b1, b2 has a period of b1*b2 if they have no gcd
    t_diffs = np.array([i for i, t in enumerate(t_schedule) if t != "x"])
    t = busses[0] + t_diffs[0]
    period = busses[0]
    for i in range(1, len(busses)):
        while True:
            t += period
            if (t + t_diffs[i]) % busses[i] == 0:
                break
        period = period * busses[i] # not needed // np.gcd(period, busses[i])
    print(t)
