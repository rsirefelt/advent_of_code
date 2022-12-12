import os
import numpy as np
# from numpy.core.numeric import zeros_like

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def read_data(filename):
    with open(filename, "r") as f:
        input_lines = f.readlines()
        elevations = []

        for line in input_lines:
            elevations.append([ord(c) for c in line.rstrip()])

    return np.array(elevations)



def find_trail(elevations, start_node, end_node):
    init_cost = 100000
    map_size = elevations.shape
    steps = np.ones_like(elevations, dtype=int) * init_cost
    visited = np.zeros_like(elevations, dtype=bool)
    current_node = start_node

    steps[current_node] = 0
    while True:
        for direction in directions:
            new_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= new_node[0] < map_size[0] and 0 <= new_node[1] < map_size[1]:
                if not visited[new_node] and elevations[new_node]  <= elevations[current_node] + 1:
                    steps[new_node] = min(
                        steps[new_node], steps[current_node] + 1
                    )

        visited[current_node] = True

        current_node = np.unravel_index(
            np.argmin(steps + visited * init_cost), map_size
        )
        if current_node[0] == end_node[0] and current_node[1] == end_node[1]:
            return steps[current_node]


def prob1(elevations, start_node, end_node):

    print(f"Trail 1 length: {find_trail(elevations, start_node, end_node)}")

def find_trail_2(elevations, start_node):
    init_cost = 100000
    map_size = elevations.shape
    steps = np.ones_like(elevations, dtype=int) * init_cost
    visited = np.zeros_like(elevations, dtype=bool)
    current_node = start_node

    steps[current_node] = 0
    while True:
        # current_risk_sum = steps[current_node]
        for direction in directions:
            new_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= new_node[0] < map_size[0] and 0 <= new_node[1] < map_size[1]:
                if not visited[new_node] and elevations[new_node]  >= elevations[current_node] - 1:
                    steps[new_node] = min(
                        steps[new_node], steps[current_node] + 1
                    )

        visited[current_node] = True

        current_node = np.unravel_index(
            np.argmin(steps + visited * init_cost), map_size
        )
        if elevations[current_node] == ord('a'):
            return steps[current_node]

def prob2(elevations, end_node):
    print(f"Trail 2 length: {find_trail_2(elevations, end_node)}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"
    elevations = read_data(filename)

    start_node = tuple(np.argwhere(elevations == ord('S'))[0])
    end_node = tuple(np.argwhere(elevations == ord('E'))[0])
    elevations[start_node] = ord('a')
    elevations[end_node] = ord('z')

    prob1(elevations, start_node, end_node)
    prob2(elevations, end_node)


if __name__ == "__main__":
    main()
