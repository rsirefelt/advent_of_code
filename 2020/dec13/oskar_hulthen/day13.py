import numpy as np


def task1(timestamp, busses):
    busses = [int(buss) for buss in busses if buss != "x"]
    min_remainder = np.inf
    buss_id = -1
    for buss in busses:
        repeats = np.ceil(timestamp / buss)
        remainder = (repeats * buss) % timestamp
        if remainder < min_remainder:
            min_remainder = remainder
            buss_id = buss

    return int(min_remainder * buss_id)


def task2(busses):
    busses = [(int(buss), idx) for idx, buss in enumerate(busses) if buss != "x"]
    timestamp = 0
    divisors = 1
    for buss, offset in busses:
        repeats = 0
        # Find timestamp that follows current rule.
        while (timestamp + offset) % buss != 0:
            # Add multiples that divide previous busses.
            # I.e. making sure that previous rules apply.
            timestamp += divisors
            repeats += 1
        print(
            f"buss {buss} with offset {offset}: "
            f"solved at {timestamp}. Added {divisors}, {repeats} times"
        )
        divisors *= buss

    return timestamp


if __name__ == "__main__":
    with open("input") as f:
        lines = list(f.readlines())
    timestamp = int(lines[0])
    busses = lines[1].rstrip().split(",")
    res1 = task1(timestamp, busses)
    print(f"Result task 1: {res1}")
    res2 = task2(busses)
    print(f"Result task 2: {res2}")
