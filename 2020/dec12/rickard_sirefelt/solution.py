import re
import numpy as np

instructions = list()
with open("input.txt", "r") as f:
    for line in f.readlines():
        dir_, val = re.match(r"(\w)(\d+)", line).groups()
        if dir_ == "E":
            instructions.append(["C", np.array([int(val), 0])])
        elif dir_ == "N":
            instructions.append(["C", np.array([0, int(val)])])
        elif dir_ == "W":
            instructions.append(["C", np.array([-int(val), 0])])
        elif dir_ == "S":
            instructions.append(["C", np.array([0, -int(val)])])
        elif dir_ == "L":
            instructions.append(["T", int(val)])
        elif dir_ == "R":
            instructions.append(["T", -int(val)])
        else:
            instructions.append([dir_, int(val)])


# Part 1:
def get_new_dir(deg, curr_dir):
    theta = np.radians(deg)
    c, s = np.cos(theta), np.sin(theta)
    return np.round(np.matmul(np.array([[c, -s], [s, c]]), curr_dir))


manhattan_dist = np.array([0, 0])
curr_dir = np.array([1, 0])
for key, val in instructions:
    if key == "C":
        manhattan_dist += val
    elif key == "T":
        curr_dir = get_new_dir(val, curr_dir)
    else:
        manhattan_dist += (curr_dir * val).astype(np.int64)


# Part 2:
ship2wp = np.array([10, 1])
ship_pos = np.array([0, 0])
for key, val in instructions:
    if key == "C":
        ship2wp += val
    elif key == "T":
        ship2wp = get_new_dir(val, ship2wp)
    else:
        ship_pos += (ship2wp * val).astype(np.int64)


print(f"1) Manhattan distans {abs(manhattan_dist).sum()}")
print(f"2) Manhattan distans {abs(ship_pos).sum()}")
