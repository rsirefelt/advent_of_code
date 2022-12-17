import numpy as np
import matplotlib.pyplot as plt

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

# Find wind pattern
wind_pattern = parseInput("input.txt")[0]

# Define the rocks
rock_type_1 = np.array([[1, 1, 1, 1]], dtype=np.bool)
rock_type_2 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.bool)
rock_type_3 = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]], dtype=np.bool)
rock_type_4 = np.array([[1], [1], [1], [1]], dtype=np.bool)
rock_type_5 = np.array([[1, 1], [1, 1]], dtype=np.bool)
rocks = [rock_type_1, rock_type_2, rock_type_3, rock_type_4, rock_type_5]

map = np.zeros((100000, 7), dtype=np.bool)
floor_level = 99000
jet_idx = 0

# Begin falling rocks!
height = floor_level
NUM_ROCKS = 2022
HEIGHTS = np.zeros(NUM_ROCKS)
for rock_idx in range(NUM_ROCKS):
    if rock_idx % 1000 == 0:
        print(rock_idx)

    # Initialize the rock!
    rock = rocks[rock_idx % 5]
    rock_bottom_row = height - 3 # TODO: SHOULD THIS BE 4?
    rock_row = rock_bottom_row - rock.shape[0]
    rock_col = 2

    # Fall the rock!
    while True:
        if wind_pattern[jet_idx % len(wind_pattern)] == "<":
            delta_x_wind= -1
        elif wind_pattern[jet_idx % len(wind_pattern)] == ">":
            delta_x_wind = 1
        else:
            assert False, "We should never get here!"


        # Move the rock by the wind! Check for horizontal wall collisions
        if delta_x_wind == -1 and rock_col == 0:
            delta_x_wind = 0 # we hit the left wall
        if delta_x_wind == 1 and rock_col + rock.shape[1] == 7:
            delta_x_wind = 0 # we hit the right wall
        if np.any(np.logical_and(rock, map[rock_row:rock_row + rock.shape[0], rock_col+delta_x_wind:rock_col + delta_x_wind + rock.shape[1]])):
            delta_x_wind = 0
        rock_col = rock_col + delta_x_wind
        jet_idx = jet_idx + 1

        # Check for downwards collision and move the rock down if empty
        did_rock_collide = np.any(np.logical_and(rock, map[rock_row + 1:rock_row + 1 + rock.shape[0], rock_col:rock_col + rock.shape[1]]))
        if rock_row + rock.shape[0] < floor_level and not did_rock_collide:
            rock_row = rock_row + 1
        else: # We hit something!
            if rock_idx == 2:
                xxx = 3
            map[rock_row:rock_row + rock.shape[0], rock_col:rock_col + rock.shape[1]] = np.logical_or(map[rock_row:rock_row + rock.shape[0], rock_col:rock_col + rock.shape[1]], rock)
            height = np.nonzero(np.any(map, axis=1))[0][0]
            HEIGHTS[rock_idx] = floor_level - height

            # Show map
            #print("New map:")
            #print(map[floor_level-10:floor_level+1,:])
            break

print("Part 1: " + str(floor_level - height))

# Part 2
num_rocks = 1000000000000
period_length = 2817 - 1117
delta_height_per_period = 2623
remainder = num_rocks % period_length
whole_periods = int(num_rocks / period_length)
assert whole_periods * period_length + remainder == num_rocks, "Fail!"

total_height = HEIGHTS[remainder-1] + whole_periods*delta_height_per_period
print("Part 2: " + str(total_height))
