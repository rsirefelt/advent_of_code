import numpy as np

treemaps = []
with open('inputs/day3') as f:
    for line in f:
        row = line.rstrip()
        treerow = np.array([c == '#' for c in row])
        treemaps.append(treerow)

treemap = np.array(treemaps)


def evaluate_direction(dx, dy, map):
    x = 0
    y = 0
    count = 0
    while y < map.shape[0]:
        count += map[y, x]
        x = (x + dx) % map.shape[1]
        y = y + dy

    return count


print(f'a) {evaluate_direction(3,1,treemap)}')

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
prod = 1
for slope in slopes:
    prod *= evaluate_direction(slope[0], slope[1], treemap)

print(f'b) {prod}')
