import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

from utils import read_lines

def parseHeightmap(filename):
    lines = read_lines(filename)
    num_rows = len(lines)
    num_cols = len(lines[0])
    heightmap = np.zeros((num_rows, num_cols), dtype=int)
    for row in range(num_rows):
        for col in range(num_cols):
            heightmap[row,col] = int(lines[row][col])

    return heightmap

def padHeightmap(heightmap):
    padded_heightmap = np.ones((heightmap.shape[0]+2, heightmap.shape[1]+2), dtype=int)*9
    padded_heightmap[1:padded_heightmap.shape[0]-1, 1:padded_heightmap.shape[1]-1] = heightmap
    return padded_heightmap

# Read the heightmap and pad it with large values around
heightmap = parseHeightmap("/home/carl/Code/AdventOfCode/Day9/input.txt")
heightmap = padHeightmap(heightmap)
minima = np.zeros_like(heightmap, dtype=bool)
total_risk = 0
for row in range(1, heightmap.shape[0]-1):
    for col in range(1, heightmap.shape[1]-1):
        # Find heights at neighbouring locations
        left = heightmap[row,col-1]
        right = heightmap[row, col+1]
        top = heightmap[row-1, col]
        bottom = heightmap[row+1, col]

        if heightmap[row,col] < np.min([left, right, top, bottom]):
            minima[row,col] = True
            total_risk = total_risk + 1 + heightmap[row,col]
print("Part 1:", total_risk)


basins = np.copy(minima)
# Fill the basins
for iter in range(10):
    points = np.nonzero(basins)
    # For each point already in the basin, add any of its relevant neighbours
    for k in range(points[0].size):
        row = points[0][k]
        col = points[1][k]
        # Add any neighbours to the basin, if the neighbour has a larger height
        if heightmap[row, col-1] > heightmap[row,col] and heightmap[row, col-1] != 9:
            basins[row, col-1] = True
        if heightmap[row, col+1] > heightmap[row,col] and heightmap[row, col+1] != 9:
            basins[row, col+1] = True
        if heightmap[row-1, col] > heightmap[row,col] and heightmap[row-1, col] != 9:
            basins[row-1, col] = True
        if heightmap[row+1, col] > heightmap[row,col] and heightmap[row+1, col] != 9:
            basins[row+1, col] = True

label, num_features = scipy.ndimage.label(basins)
basin_sizes = np.sort([np.sum(label == k) for k in range(1, num_features+1)])

print('Part 2:', basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])

plt.figure()
plt.subplot(121)
plt.imshow(heightmap)
plt.subplot(122)
plt.imshow(basins)
plt.show()