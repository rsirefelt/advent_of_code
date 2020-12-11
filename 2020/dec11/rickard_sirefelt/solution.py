import numpy as np
import copy
import pandas as pd

orig_empty_pos, curr_empty_pos, curr_occ_pos = list(), list(), list()
next_empty_pos, next_occ_pos = list(), list()
input_ = list()
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        input_.append(list(line.rstrip()))
        for j, c in enumerate(line.rstrip()):
            if c == "L":
                orig_empty_pos.append(np.array([i + 1, j + 1], dtype=np.int32))


# Part 1:
curr_map = np.zeros([len(input_) + 2, len(input_[0]) + 2], dtype=np.int32)
next_map = np.zeros([len(input_) + 2, len(input_[0]) + 2], dtype=np.int32)
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int32)
curr_empty_pos = orig_empty_pos.copy()
while True:
    for p in curr_empty_pos:
        if np.sum(curr_map[p[0] - 1 : p[0] + 2, p[1] - 1 : p[1] + 2] * kernel) == 0:
            next_occ_pos.append(p)
            next_map[p[0], p[1]] = 1

    for p in curr_occ_pos:
        if np.sum(curr_map[p[0] - 1 : p[0] + 2, p[1] - 1 : p[1] + 2] * kernel) > 3:
            next_empty_pos.append(p)
            next_map[p[0], p[1]] = 0

    if (curr_map == next_map).all():
        break

    curr_map = next_map.copy()
    curr_empty_pos = next_empty_pos.copy()
    curr_occ_pos = next_occ_pos.copy()
    next_occ_pos.clear()
    next_empty_pos.clear()

print(f"1) Number of occupied pos: {np.sum(curr_map)}")

# Part 2:
curr_map = copy.deepcopy(input_)
next_map = copy.deepcopy(input_)
curr_empty_pos, curr_occ_pos = list(), list()
directions = np.array(
    [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]],
    dtype=np.int32,
)


def check_flip(p, curr_map, flip_empty):
    see_occ = np.zeros(8, dtype=np.int32)
    for i, dir_ in enumerate(directions):
        s = p.copy()
        while True:
            s += dir_
            if (s < 0).any() or s[0] >= len(curr_map) or s[1] >= len(curr_map[0]):
                break
            elif curr_map[s[0]][s[1]] == "#":
                see_occ[i] = 1
                break
            elif curr_map[s[0]][s[1]] == "L":
                break

    if flip_empty:
        return see_occ.sum() == 0
    else:
        return see_occ.sum() > 4


curr_empty_pos = [r - np.array([1, 1]) for r in orig_empty_pos]

while True:
    for p in curr_empty_pos:
        if check_flip(p, curr_map, True):
            next_occ_pos.append(p)
            next_map[p[0]][p[1]] = "#"

    for p in curr_occ_pos:
        if check_flip(p, curr_map, False):
            next_empty_pos.append(p)
            next_map[p[0]][p[1]] = "L"

    if curr_map == next_map:
        break

    curr_map = copy.deepcopy(next_map)
    curr_empty_pos = next_empty_pos.copy()
    curr_occ_pos = next_occ_pos.copy()
    next_occ_pos.clear()
    next_empty_pos.clear()


count = sum([row.count("#") for row in curr_map])

print(f"2) Number of occupied pos: {count}")
