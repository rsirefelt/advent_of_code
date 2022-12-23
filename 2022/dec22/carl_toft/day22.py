import numpy as np

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseMap(lines):
    map = []
    max_column_width = max([len(line) for line in lines[:-1]])
    map.append(" "*(max_column_width+2))
    for idx in range(len(lines) - 2):
        line = lines[idx]
        if len(line) == max_column_width:
            map.append(" " + line + " ")
        else:
            num_missing = max_column_width - len(line)
            map.append(" " + line + num_missing*' ' + " ")
    map.append(" "*(max_column_width+2))

    instruction_string = lines[-1]
    instructions = []
    last_char = -1
    for curr_char in range(len(instruction_string)):
        if instruction_string[curr_char] == "L" or instruction_string[curr_char] == "R":
            instructions.append(int(instruction_string[last_char + 1:curr_char]))
            instructions.append(instruction_string[curr_char])
            last_char = curr_char
    instructions.append(int(instruction_string[curr_char:]))

    return map, instructions

def getStartPos(map):
    for row, line in enumerate(map):
        for col, char in enumerate(line):
            if char == ".":
                return (row, col)

def move(curr_row, curr_col, curr_angle, distance, map, teleporting=False):
    for d in range(distance):
        delta_row = round(np.sin(curr_angle * np.pi / 180))
        delta_col = round(np.cos(curr_angle * np.pi / 180))

        new_col = curr_col + delta_col
        new_row = curr_row + delta_row

        if map[new_row][new_col] == " ":
            # Teleport! Figure out if we should teleport horizontally or vertically
            if teleporting == True:
                return curr_row, curr_col
            new_hyp_row, new_hyp_col = move(curr_row, curr_col, curr_angle+180, 1000000, map, teleporting=True)
            if map[new_hyp_row][new_hyp_col] != "#":
                curr_row = new_hyp_row
                curr_col = new_hyp_col
        elif map[new_row][new_col] == "#" and teleporting == False:
            return curr_row, curr_col
        elif map[new_row][new_col] == "#" and teleporting == True:
            curr_row = new_row
            curr_col = new_col
        elif map[new_row][new_col] == ".":
            curr_row = new_row
            curr_col = new_col
        else:
            assert False, "We should never get here!"
    return curr_row, curr_col

map, instructions = parseMap(parseInput("input.txt"))
move_map = []
for line in map:
    move_map.append(line)

curr_row, curr_col = getStartPos(map)
curr_angle = 0

for line in map:
    print(line)

for instruction in instructions:
    if instruction == "L":
        curr_angle = curr_angle - 90
    elif instruction == "R":
        curr_angle = curr_angle + 90
    else:
        distance = instruction
        curr_row, curr_col = move(curr_row, curr_col, curr_angle, distance, map)

delta_row = round(np.sin(curr_angle * np.pi / 180))
delta_col = round(np.cos(curr_angle * np.pi / 180))
if delta_col == 1 and delta_row == 0:
    facing_score = 0
elif delta_col == -1 and delta_row == 0:
    facing_score = 2
elif delta_col == 0 and delta_row == 1:
    facing_score = 1
elif delta_col == 0 and delta_row == -1:
    facing_score = 3

score = facing_score + 4*curr_col + 1000*curr_row
print("Part 1: " + str(score))

xxx = 3