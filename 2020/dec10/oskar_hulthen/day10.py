from collections import Counter

import numpy as np


def task1(int_list):
    diff = [int_list[i + 1] - int_list[i] for i in range(len(int_list) - 1)]
    counts = Counter(diff)
    return counts[1] * counts[3]


def task2(int_list):
    # To automatically return 0 for node values that are unreachable.
    previous_paths = Counter()
    previous_paths[0] = 1
    for val in int_list[1:]:
        for i in range(3):
            # Check all possible paths through the previous 3 nodes.
            previous_paths[val] += previous_paths[val - (i + 1)]

    return previous_paths[int_list[-1]]


if __name__ == "__main__":
    with open("input") as f:
        lines = list(f.readlines())
        int_list = [int(i) for i in lines]

    int_list.append(0)  # Add start point
    int_list.append(max(int_list) + 3)  # Add end point
    int_list.sort()

    print(task1(int_list))
    print(task2(int_list))
