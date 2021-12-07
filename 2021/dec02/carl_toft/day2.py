from utils import read_lines

lines = read_lines("/home/carl/Code/AdventOfCode/Day2/input.txt")

# Read the input as two lists: one with the direction of motion and one with the magnitude
direction = []
magnitude = []
for line in lines:
    parts = line.split(" ")
    direction.append(parts[0])
    magnitude.append(int(parts[1]))

# Move the submarine around according to the instructions in part 1
horizontal_pos = 0
depth = 0
for k in range(len(direction)):
    if direction[k] == "forward":
        horizontal_pos = horizontal_pos + magnitude[k]
    elif direction[k] == "up":
        depth = depth - magnitude[k]
    elif direction[k] == "down":
        depth = depth + magnitude[k]

print("Part 1: ", horizontal_pos*depth)

# Restart the submarine, and move it according to part 2 instructions
horizontal_pos = 0
depth = 0
aim = 0
for k in range(len(direction)):
    if direction[k] == "forward":
        horizontal_pos = horizontal_pos + magnitude[k]
        depth = depth + aim*magnitude[k]
    elif direction[k] == "up":
        aim = aim - magnitude[k]
    elif direction[k] == "down":
        aim = aim + magnitude[k]

print("Part 2: ", horizontal_pos*depth)