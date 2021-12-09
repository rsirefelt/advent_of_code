import numpy as np
from scipy.ndimage import minimum_filter, convolve

height_maps = []
with open('inputs/day9') as f:
    for line in f:
        height_maps.append(np.array([c for c in line.rstrip()]).astype(np.int32))

height_map = np.stack(height_maps)

footprint = np.zeros((3, 3), dtype=bool)
footprint[1, :] = 1
footprint[:, 1] = 1
footprint[1, 1] = 0
local_minimas = minimum_filter(height_map, footprint=footprint, mode='constant', cval=9) > height_map

print(sum(height_map[local_minimas] + 1))


def grow_basin(starting_index):
    basin_mask = np.zeros_like(local_minimas)
    basin_mask[starting_index[0], starting_index[1]] = True

    for height in range(height_map[starting_index[0], starting_index[1]], 9):
        while True:
            neighbours = np.logical_and(convolve(basin_mask, footprint, mode='constant', cval=0), ~basin_mask)
            new_basin_mask = np.logical_and(neighbours, height_map == height)
            if not np.any(new_basin_mask):
                break
            basin_mask |= new_basin_mask

    return np.sum(basin_mask)


minimum_indices = np.argwhere(local_minimas)

basin_sizes = []
for i in range(minimum_indices.shape[0]):
    basin_sizes.append(grow_basin(minimum_indices[i, :]))

print(np.prod(sorted(basin_sizes)[-3:]))
