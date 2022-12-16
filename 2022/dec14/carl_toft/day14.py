import numpy as np

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseCaves(lines):
    for line in lines:
        parts = line.split(" -> ")
        for end_idx in range(1,len(parts)):
            start = [int(val) for val in parts[end_idx-1].split(",")]
            end = [int(val) for val in parts[end_idx].split(",")]
            if start[0] == end[0]:
                x = start[0]
                start_val = min(start[1], end[1])
                end_val = max(start[1], end[1])
                assert end_val >= start_val, "Wrong order!"
                for y in range(start_val, end_val+1):
                    map[y, x] = 1
            elif start[1] == end[1]:
                y = start[1]
                start_val = min(start[0], end[0])
                end_val = max(start[0], end[0])
                assert end_val >= start_val, "Wrong order!"
                for x in range(start_val, end_val+1):
                    map[y, x] = 1
            else:
                assert False, "Incorrect input!"

map = np.zeros((1000, 1000))
data = parseCaves(parseInput("input.txt"))
should_stop = False

while not should_stop:
    sand_pos = [500, 0]
    while sand_pos[1] < 999:
        if map[sand_pos[1]+1, sand_pos[0]] == 0:
            sand_pos[1] = sand_pos[1] + 1
            continue
        if map[sand_pos[1]+1, sand_pos[0]-1] == 0:
            sand_pos[1] = sand_pos[1] + 1
            sand_pos[0] = sand_pos[0]-1
            continue
        if map[sand_pos[1]+1, sand_pos[0]+1] == 0:
            sand_pos[1] = sand_pos[1] + 1
            sand_pos[0] = sand_pos[0] + 1
            continue

        # Sand comes to rest
        map[sand_pos[1], sand_pos[0]] = 2
        break
    #print(map[0:11, 493:505])
    if sand_pos[1] == 999:
        break

print("Part 1: " + str(np.sum(map == 2)))


map = np.zeros((1000, 1000))
data = parseCaves(parseInput("input.txt"))
should_stop = False
floor_level = np.max(np.where(map == 1)[0]) + 2
for x in range(0, 1000):
    map[floor_level, x] = 1

while not should_stop:
    sand_pos = [500, 0]
    while sand_pos[1] < 999:
        if map[sand_pos[1]+1, sand_pos[0]] == 0:
            sand_pos[1] = sand_pos[1] + 1
            continue
        if map[sand_pos[1]+1, sand_pos[0]-1] == 0:
            sand_pos[1] = sand_pos[1] + 1
            sand_pos[0] = sand_pos[0]-1
            continue
        if map[sand_pos[1]+1, sand_pos[0]+1] == 0:
            sand_pos[1] = sand_pos[1] + 1
            sand_pos[0] = sand_pos[0] + 1
            continue

        # Sand comes to rest
        map[sand_pos[1], sand_pos[0]] = 2
        break
    #print(map[0:11, 493:505])
    if sand_pos[0] == 500 and sand_pos[1] == 0:
        break

print("Part 2: " + str(np.sum(map == 2)))

xxx = 3
