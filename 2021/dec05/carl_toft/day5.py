import numpy as np
from utils import read_lines

def parseInput(filename):
    """Parse input and return it as a 2D array."""
    input = read_lines(filename)
    lines = np.zeros((len(input), 4), dtype=int)
    for idx, line in enumerate(input):
        start, end = line.split('->')
        start = start.strip()
        end = end.strip()
        start = tuple((int(x) for x in start.split(',')))
        end = tuple((int(x) for x in end.split(',')))
        lines[idx, 0] = start[0]
        lines[idx, 1] = start[1]
        lines[idx, 2] = end[0]
        lines[idx, 3] = end[1]
    return lines

lines = parseInput("/home/carl/Code/AdventOfCode/Day5/input.txt")

# Build a map that fits all lines
size = np.max(lines)+1
map = np.zeros((size, size))

# Add all lines to the map
for k in range(lines.shape[0]):
    # Only look at horizontal or vertical lines
    if lines[k,0] != lines[k,2] and lines[k,1] != lines[k,3]:
        # The line is diagonal. Parametrize it by the x-values
        if lines[k,2] > lines[k,0]:
            x_start = lines[k,0]
            x_stop = lines[k,2]+1
            y_start = lines[k,1]
            y_stop = lines[k,3]+1
        else:
            x_start = lines[k,2]
            x_stop = lines[k,0]+1
            y_start = lines[k,3]
            y_stop = lines[k,1]+1
        y_step = np.sign(y_stop - y_start)
        for kk in range(x_stop-x_start):
            map[y_start+y_step*kk, x_start + kk] += 1

    if lines[k,0] == lines[k,2]:
        # The line is vertical
        map[lines[k,1]:lines[k,3]+1, lines[k,0]] += 1
        map[lines[k,3]:lines[k,1]+1, lines[k, 0]] += 1
    if lines[k,1] == lines[k,3]:
        # The line is horizontal
        map[lines[k,1], lines[k,0]:lines[k,2]+1] += 1
        map[lines[k,1], lines[k,2]:lines[k,0] + 1] += 1

print(map)
print('Part 2:', np.sum(map>=2))
