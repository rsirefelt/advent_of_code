import numpy as np
import matplotlib.pyplot as plt
from utils import read_lines

def parseInput(filename):
    lines = read_lines(filename)
    idx = 0
    dots = []
    while len(lines[idx]) > 0:
        x,y = lines[idx].split(',')
        dots.append((int(x), int(y)))
        idx = idx + 1
    idx = idx + 1
    instructions = []
    while idx < len(lines):
        coord, val = lines[idx].split(' ')[-1].split('=')
        instructions.append([coord, int(val)])
        idx = idx + 1

    dots = set(dots)
    return dots, instructions

def fold(dots, coord, value):
    new_dots = set()
    for x,y in dots:
        if coord == 'y':
            if y > value:
                y = 2*value - y
        if coord == 'x':
            if x > value:
                x = 2*value - x
        new_dots.add((x,y))
    return new_dots

dots, instructions = parseInput("/home/carl/Code/AdventOfCode/Day13/input.txt")

# Part 1
dots_after_one_fold = fold(dots, instructions[0][0], instructions[0][1])
print("Part 1:", len(dots_after_one_fold))
for coord, value in instructions[:1]:
    dots = fold(dots, coord, value)

# Part 2
for coord, value in instructions:
    dots = fold(dots, coord, value)
max_x = max([x for x,y in dots])
max_y = max([y for x,y in dots])
image = np.zeros(())
image = np.zeros((max_y+1, max_x+1), dtype=bool)
for x,y in dots:
    image[y,x] = True
plt.figure()
plt.imshow(image)
plt.show()
