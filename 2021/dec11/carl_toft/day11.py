import numpy as np
from utils import read_lines

def readMatrix(filename):
    """Read input matrix and pad it with -np.inf around the border."""
    lines = read_lines(filename)
    matrix = np.ones((len(lines)+2, len(lines[0])+2), dtype=int)*(-np.inf)
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            matrix[row+1,col+1] = lines[row][col]
    return matrix

energies = readMatrix("/home/carl/Code/AdventOfCode/Day11/input.txt")

num_flashes = 0
for timestep in range(10000):
    energies = energies + 1

    # Find which octopuses are about to flash this step
    to_flash = np.nonzero(energies == 10)
    to_flash = [[to_flash[0][k], to_flash[1][k]] for k in range(len(to_flash[0]))]
    for pos in to_flash:
        energies[pos[0], pos[1]] += 1 # add one so we don't count this again as a new flash later

    # Flash them one at a time, adding any new ones about to flash to the list
    while len(to_flash) > 0:
        # Flash the last one
        pos = to_flash.pop()
        num_flashes = num_flashes + 1
        energies[pos[0]-1:pos[0]+2, pos[1]-1:pos[1]+2] += 1

        new_flashes = np.nonzero(energies == 10)
        new_flashes = [[new_flashes[0][k], new_flashes[1][k]] for k in range(len(new_flashes[0]))]
        for tmp in new_flashes:
            energies[tmp[0], tmp[1]] += 1
        to_flash = to_flash + new_flashes

    energies[energies >= 10] = 0

    if timestep == 99:
        print("Part 1:", num_flashes)

    if not np.any(energies[1:energies.shape[0]-1, 1:energies.shape[1]-1]):
        print("Part 2:", timestep+1)
        break