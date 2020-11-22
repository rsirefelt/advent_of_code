import numpy as np

coords = np.loadtxt(
    "dec6/rickard_sirefelt/input.txt", delimiter=',', dtype=int)

minX, minY = min(coords[:, 0]), min(coords[:, 1])
maxX, maxY = max(coords[:, 0]), max(coords[:, 1])
num_coords = len(coords)
coords_new = coords - (minX, minY)

# y, x, (min_dist, point_id)
grid = np.zeros((maxY + 1 - minY, maxX + 1 - minX, 2), dtype=int)
grid[:, :, 0] = maxX + maxY
grid[:, :, 1] = num_coords

for i_coord, coord in enumerate(coords_new):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            dist = abs(x - coord[0]) + abs(y - coord[1])
            if dist < val[0]:
                val[0] = dist
                val[1] = i_coord
            elif dist == val[0]:
                val[1] = num_coords

area_for_each_coord = np.zeros(len(coords) + 1, dtype=int)
for row in grid:
    for val in row:
        area_for_each_coord[val[1]] += 1

inf_coord = np.unique(
    np.concatenate((grid[:, 0, 1], grid[:, grid.shape[1] - 1, 1],
                    grid[0, :, 1], grid[grid.shape[0] - 1, :, 1]))).tolist()

allowed_coord = []
for i in range(num_coords):
    if i not in inf_coord:
        allowed_coord.append(i)

print(max(area_for_each_coord[allowed_coord]))
