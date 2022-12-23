import numpy as np
import matplotlib.pyplot as plt

def get_wrapper(cube_size):
    wrapper = {}
    # Left side of 1 to upside down left side of 4
    for row in range(cube_size):
        wrapper[(row, cube_size, 0)] = (3*cube_size-1-row, 0, 0) # (target_row, target_col, new_angle) # POTENTIALLY DANGEROUS HERE
    # Right side of 1 to left side of 2 already done
    # Right side of 2 to upside down right side of 5
    for row in range(cube_size):
        wrapper[(row, 3*cube_size-1, 180)] = (3*cube_size - 1 - row, 2*cube_size-1, 180)
    # Left side of 5 to right side of 4 already done

    # Top side of 1 to left side of 6
    for col in range(cube_size):
        wrapper[(0, cube_size+col, 90)] = (3*cube_size + col, 0, 0)
    # Top side of 2 to bottom side of 6
    for col in range(cube_size):
        wrapper[(0, 2*cube_size+col, 90)] = (4*cube_size-1, col, 270)
    # Bottom side of 5 to right side of 6
    for col in range(cube_size):
        wrapper[(3*cube_size-1, cube_size+col, 270)] = (3*cube_size + col, cube_size-1, 180)
    # Bottom side of 4 to top side of 6 already done

    # Bottom side of 1 to top side of 3 already done
    # Top side of 4 to left side of 3
    for col in range(cube_size):
        wrapper[(2*cube_size, col, 90)] = (cube_size + col, cube_size, 0)
    # Top side of 5 to bottom side of 3 already done
    # Bottom side of 2 to right side of 3
    for col in range(cube_size):
        wrapper[(cube_size-1, 2*cube_size+col, 270)] = (cube_size+col, 2*cube_size-1, 180)

    # Also add all the sides the other way around as well
    keys = []
    values = []
    for key, value in wrapper.items():
        keys.append(key)
        values.append(value)
    for idx in range(len(keys)):
        wrapper[values[idx]] = keys[idx]

    return wrapper

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def getImage(map, curr_row, curr_col):
    image = np.zeros((len(map), len(map[0]), 3))
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == ".":
                image[row, col, 0] = 1.0
                image[row, col, 1] = 1.0
                image[row, col, 2] = 1.0
            if map[row][col] == "#":
                image[row, col, 0] = 0.0
                image[row, col, 1] = 0.0
                image[row, col, 2] = 0.0
    image[curr_row, curr_col, 0] = 1.0
    image[curr_row, curr_col, 1] = 0.0
    image[curr_row, curr_col, 2] = 0.0

    return image


def parseMap(lines):
    map = []
    max_column_width = max([len(line) for line in lines[:-1]])
    for idx in range(len(lines) - 2):
        line = lines[idx]
        if len(line) == max_column_width:
            map.append(line)
        else:
            num_missing = max_column_width - len(line)
            map.append(line + num_missing*' ')

    instruction_string = lines[-1]
    instructions = []
    last_char = -1
    for curr_char in range(len(instruction_string)):
        if instruction_string[curr_char] == "L" or instruction_string[curr_char] == "R":
            instructions.append(int(instruction_string[last_char + 1:curr_char]))
            instructions.append(instruction_string[curr_char])
            last_char = curr_char
    instructions.append(int(instruction_string[(last_char+1):]))

    return map, instructions

def getStartPos(map):
    for row, line in enumerate(map):
        for col, char in enumerate(line):
            if char == ".":
                return (row, col)

def move(curr_row, curr_col, curr_angle, distance, map, wrapper):
    for d in range(distance):
        delta_row = round(np.sin(curr_angle * np.pi / 180))
        delta_col = round(np.cos(curr_angle * np.pi / 180))

        new_col = curr_col + delta_col
        new_row = curr_row + delta_row

        if new_row < 0 or new_row >= 200 or new_col < 0 or new_col >= 150 or map[new_row][new_col] == " ":
            # Wrap around the cube!
            new_hyp_row, new_hyp_col, new_angle = wrapper[(curr_row, curr_col, (curr_angle + 180) % 360)]
            if map[new_hyp_row][new_hyp_col] != "#":
                #print("Jumped at (" + str(curr_row) + ", " + str(curr_col) + "). Curr dir: " + str(curr_angle) + ", new angle: " + str(new_angle))
                curr_row = new_hyp_row
                curr_col = new_hyp_col
                curr_angle = new_angle
            else:
                return curr_row, curr_col, curr_angle
        elif map[new_row][new_col] == "#":
            return curr_row, curr_col, curr_angle
        elif map[new_row][new_col] == ".":
            curr_row = new_row
            curr_col = new_col
        else:
            assert False, "We should never get here!"
    return curr_row, curr_col, curr_angle

map, instructions = parseMap(parseInput("input.txt"))

wrapper = get_wrapper(50)

curr_row, curr_col = getStartPos(map)
curr_angle = 0

for line in map:
    print(line)

for instruction in instructions:
    if instruction == "L":
        curr_angle = curr_angle - 90
        curr_angle = curr_angle % 360
    elif instruction == "R":
        curr_angle = curr_angle + 90
        curr_angle = curr_angle % 360
    else:
        distance = instruction
        image = getImage(map, curr_row, curr_col)
        curr_row, curr_col, curr_angle = move(curr_row, curr_col, curr_angle, distance, map, wrapper)
        image[curr_row, curr_col, 0] = 0.0
        image[curr_row, curr_col, 1] = 1.0
        image[curr_row, curr_col, 2] = 0.0
        #if jumped:
        #    plt.figure()
        #    plt.imshow(image)
        #    plt.title("Moved " + str(distance) + " in angle " + str(curr_angle))
        #    plt.show()

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

curr_col = curr_col+1
curr_row = curr_row+1
score = facing_score + 4*curr_col + 1000*curr_row
print("Part 2: " + str(score))
