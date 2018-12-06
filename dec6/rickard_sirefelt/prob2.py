import numpy as np

coords = np.loadtxt(
    "dec6/rickard_sirefelt/input.txt", delimiter=',', dtype=int)

minX, minY = min(coords[:, 0]), min(coords[:, 1])
maxX, maxY = max(coords[:, 0]), max(coords[:, 1])
num_coords = len(coords)
coords_new = coords - (minX, minY)
grid = np.zeros((maxY + 1 - minY, maxX + 1 - minX), dtype=int)

for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        dist = 0
        for coord in coords_new:
            dist += abs(x - coord[0]) + abs(y - coord[1])

        if dist < 10000:
            grid[y, x] += 1

print(np.sum(grid))
