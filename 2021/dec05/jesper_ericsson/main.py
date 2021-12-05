import re
import numpy as np

regex_lines = re.compile(r"([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)")


def readData():
    filename = "testdata.csv"
    size = (10, 10)
    filename = "data.csv"
    size = (1000, 1000)
    lines = []
    with open(filename, "r") as f:
        input_data = f.readlines()
        for row in input_data:
            row_values = regex_lines.findall(row)
            lines.append([int(i) for i in row_values[0]])

    return lines, size


def add_line(coordinate_map, line):
    if line[0] > line[2]:
        x_ind = range(line[0], line[2] - 1, -1)
    else:
        x_ind = range(line[0], line[2] + 1)

    if line[1] > line[3]:
        y_ind = range(line[1], line[3] - 1, -1)
    else:
        y_ind = range(line[1], line[3] + 1)

    coordinate_map[x_ind, y_ind] += 1


def prob1(lines, size):
    coordinate_map = np.zeros(size)
    for line in lines:
        if line[0] == line[2] or line[1] == line[3]:
            add_line(coordinate_map, line)
    num_points = np.sum(coordinate_map > 1)
    print("Prob1, Number overlapping points:", num_points)


def prob2(lines, size):
    coordinate_map = np.zeros(size)
    for line in lines:
        add_line(coordinate_map, line)

    num_points = np.sum(coordinate_map > 1)
    print("Prob2, Number overlapping points:", num_points)


def main():
    lines, size = readData()

    prob1(lines, size)
    prob2(lines, size)


if __name__ == "__main__":
    main()
