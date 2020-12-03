import numpy as np


def get_num_trees(slope, sub_map):
    num_trees = 0
    pos = np.array([0, 0])

    while pos[1] < len(sub_map):
        if sub_map[pos[1]][pos[0]] == "#":
            num_trees += 1
        pos += slope
        pos[0] = pos[0] % len(sub_map[0])

    return num_trees


with open("input.txt", "r") as f:
    sub_map = [line.rstrip() for line in f]

# Part 1:
slope = np.array([3, 1])  # (dx, dy)
num_trees = get_num_trees(slope, sub_map)
print(num_trees)

# Part 2:
slopes = [
    np.array([1, 1]),
    np.array([3, 1]),
    np.array([5, 1]),
    np.array([7, 1]),
    np.array([1, 2]),
]
tree_prod = 1
for slope in slopes:
    num_trees = get_num_trees(slope, sub_map)
    tree_prod *= num_trees
print(tree_prod)
