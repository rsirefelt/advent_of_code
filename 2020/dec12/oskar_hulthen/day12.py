import math
import regex as re
import numpy as np


def task1(actions):
    directions = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    directions = {key: np.array(val) for key, val in directions.items()}
    dir_order = list(directions.keys())
    cur_direction = "E"

    current_pos = np.array((0, 0))

    for action, val in actions:
        val = int(val)
        if action == "F":
            update = directions[cur_direction] * val

        elif action in ["L", "R"]:
            rotation_steps = val // 90
            cur_index = dir_order.index(cur_direction)

            if action == "R":
                new_index = cur_index + rotation_steps
            else:
                new_index = cur_index - rotation_steps

            cur_direction = dir_order[new_index % 4]
            update = np.array((0, 0))

        elif action in directions.keys():
            update = directions[action] * val

        current_pos += update

    return abs(current_pos[0]) + abs(current_pos[1])


def task2(actions):
    directions = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    directions = {key: np.array(val) for key, val in directions.items()}
    dir_order = list(directions.keys())

    waypoint = np.array((10, 1))
    current_pos = np.array((0, 0))

    for action, val in actions:
        val = int(val)
        if action == "F":
            current_pos += waypoint * val

        elif action in ["L", "R"]:

            rads = np.deg2rad(val)
            if action == "R":
                rads = -rads
            else:
                rads = rads

            # Rotation around (0,0)
            dir_ = (int(np.cos(rads)), int(np.sin(rads)))
            waypoint = np.array(
                (
                    waypoint[0] * dir_[0] - waypoint[1] * dir_[1],
                    waypoint[1] * dir_[0] + waypoint[0] * dir_[1],
                )
            )

        elif action in directions.keys():
            waypoint += directions[action] * val

    return abs(current_pos[0]) + abs(current_pos[1])


if __name__ == "__main__":
    actions = []

    with open("input") as f:
        lines = list(f.readlines())
        for line in lines:
            pattern = re.findall("([A-Z])([0-9]*)", line)
            actions.append(pattern[0])

    res1 = task1(actions)
    print(res1)
    res2 = task2(actions)
    print(res2)
