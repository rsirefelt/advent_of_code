import numpy as np


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        connections = {}
        for line in input_lines:
            first, second = line.rstrip().split("-")

            if first in connections:
                connections[first].append(second)
            else:
                connections[first] = [second]

            if second in connections:
                connections[second].append(first)
            else:
                connections[second] = [first]

    return connections


def get_valid_paths(connections, cave, small_visited_caves, second_visited):
    if cave == "end":
        return 1

    if cave in small_visited_caves:
        if second_visited or cave == "start":
            return 0
        else:
            second_visited = True

    if cave.islower():
        small_visited_caves.add(cave)
    num_valid_paths = 0
    for child in connections[cave]:
        num_valid_paths += get_valid_paths(
            connections, child, small_visited_caves.copy(), second_visited
        )

    return num_valid_paths


def main():
    connections = readData()

    valid_paths = get_valid_paths(connections, "start", set([]), True)
    print("Prob1 number of valid paths:", valid_paths)

    valid_paths2 = get_valid_paths(connections, "start", set([]), False)
    print("Prob2 number of valid paths:", valid_paths2)


if __name__ == "__main__":
    main()
