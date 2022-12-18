import numpy as np
from scipy.ndimage import binary_dilation, binary_fill_holes, convolve, generate_binary_structure

with open('inputs/day18') as f:
    cubes = f.read().splitlines()

for fill_holes in (False, True):
    grid = np.zeros((100, 100, 100), dtype=bool)
    for cube in cubes:
        index = tuple([int(coord)+1 for coord in cube.split(',')])
        grid[index] = True

    neighbor_elem = generate_binary_structure(rank=3, connectivity=1)
    if fill_holes:
        grid = binary_fill_holes(grid, neighbor_elem)
    dilated_grid = binary_dilation(grid, neighbor_elem)
    only_neighbors = np.logical_and(dilated_grid, np.logical_not(grid))
    neighbor_count = convolve(only_neighbors.astype(int), neighbor_elem, mode='constant')

    print(sum(neighbor_count[grid]))
