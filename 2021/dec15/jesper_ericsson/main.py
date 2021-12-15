import numpy as np
import matplotlib.pyplot as plt
from numpy.core.numeric import zeros_like

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        risklevels = []

        for line in input_lines:
            risklevels.append([int(c) for c in line.rstrip()])

    return np.array(risklevels)


# def get_valid_paths(risklevels, visited, lowest_score, map_size, current_score, coords):
#     if coords != (0, 0):
#         current_score += risklevels[coords[0], coords[1]]

#     # print(visited)
#     if current_score > visited[coords[0], coords[1]]:
#         return lowest_score

#     visited[coords[0], coords[1]] = current_score

#     # print(lowest_score)
#     if current_score > lowest_score:
#         return lowest_score

#     if coords[0] == map_size[0] - 1 and coords[1] == map_size[1] - 1:
#         print(visited)
#         return current_score

#     for direction in directions:
#         new_coords = (coords[0] + direction[0], coords[1] + direction[1])
#         if 0 <= new_coords[0] < map_size[0] and 0 <= new_coords[1] < map_size[1]:

#             lowest_score = get_valid_paths(
#                 risklevels,
#                 visited,
#                 lowest_score,
#                 map_size,
#                 current_score,
#                 new_coords,
#             )
#     return lowest_score


def calculate_risk_level(risklevels):
    init_cost = 100000
    map_size = risklevels.shape
    risk_sum = np.ones_like(risklevels, dtype=int) * init_cost
    visited = np.zeros_like(risklevels, dtype=bool)

    current_node = (0, 0)
    risk_sum[current_node] = 0
    while True:
        current_risk_sum = risk_sum[current_node]
        for direction in directions:
            new_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= new_node[0] < map_size[0] and 0 <= new_node[1] < map_size[1]:
                if not visited[new_node]:
                    risk_sum[new_node] = min(
                        risk_sum[new_node], risklevels[new_node] + current_risk_sum
                    )

        visited[current_node] = True

        current_node = np.unravel_index(
            np.argmin(risk_sum + visited * init_cost), map_size
        )
        if current_node[0] == map_size[0] - 1 and current_node[1] == map_size[1] - 1:
            return risk_sum[current_node]


def prob1(risklevels):
    print(calculate_risk_level(risklevels))


def prob2(risklevels):
    map_size = risklevels.shape

    new_map_size = (map_size[0] * 5, map_size[0] * 5)
    new_risk_levels = np.zeros(new_map_size, dtype=int)

    for i in range(5):
        for j in range(5):
            extra_cost = i + j
            new_risk_levels[
                i * map_size[0] : (i + 1) * map_size[0],
                j * map_size[1] : (j + 1) * map_size[1],
            ] = (
                np.mod(risklevels + extra_cost - 1, 9) + 1
            )
    print(calculate_risk_level(new_risk_levels))


def main():
    risklevels = readData()

    prob1(risklevels)

    prob2(risklevels)


if __name__ == "__main__":
    main()
