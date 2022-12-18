import numpy as np
import scipy.ndimage

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseDroplets(lines):
    droplets = []
    for line in lines:
        droplet = tuple([int(x) for x in line.split(',')])
        droplets.append(droplet)
    return droplets

lava_droplets = parseDroplets(parseInput("input.txt"))
lava_droplets = set(lava_droplets)
total_area = 0

for droplet in lava_droplets:
    neighbours = []
    x = droplet[0]
    y = droplet[1]
    z = droplet[2]

    for delta_x in [-1, 1]:
        neighbours.append((x+delta_x, y, z))
    for delta_y in [-1, 1]:
        neighbours.append((x,y+delta_y,z))
    for delta_z in [-1, 1]:
        neighbours.append((x,y,z+delta_z))

    for neighbour in neighbours:
        if neighbour not in lava_droplets:
            total_area = total_area + 1

print("Part 1: " + str(total_area))

lava_droplets = parseDroplets(parseInput("input.txt"))
droplet_map = np.ones((24, 24, 24), dtype=bool)
offset = 3
for droplet in lava_droplets:
    droplet_map[droplet[0]+offset, droplet[1]+offset, droplet[2]+offset] = False
labels, N = scipy.ndimage.label(droplet_map)
xxx = 3

total_area = 0

for droplet in lava_droplets:
    neighbours = []
    x = droplet[0]
    y = droplet[1]
    z = droplet[2]

    for delta_x in [-1, 1]:
        neighbours.append((x+delta_x, y, z))
    for delta_y in [-1, 1]:
        neighbours.append((x,y+delta_y,z))
    for delta_z in [-1, 1]:
        neighbours.append((x,y,z+delta_z))

    for neighbour in neighbours:
        if neighbour not in lava_droplets:
            if labels[neighbour[0]+offset, neighbour[1]+offset, neighbour[2]+offset] == 1:
                total_area = total_area + 1

print("Part 2: " + str(total_area))