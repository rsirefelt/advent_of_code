import numpy as np


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        heightmap = []

        for line in input_lines:
            heightmap.append([int(c) for c in line.rstrip()])

    return np.array(heightmap)


def is_lowest_level(map, row, col, map_size):
    lowest = True
    if row > 0:
        lowest = lowest and map[row, col] < map[row - 1, col]
    if row < map_size[0] - 1:
        lowest = lowest and map[row, col] < map[row + 1, col]
    if col > 0:
        lowest = lowest and map[row, col] < map[row, col - 1]
    if col < map_size[1] - 1:
        lowest = lowest and map[row, col] < map[row, col + 1]

    return lowest


def crawler(heightmap, row, col, map_size, already_visited):
    if heightmap[row, col] == 9 or (row * map_size[1] + col) in already_visited:
        return 0

    already_visited.append(row * map_size[1] + col)

    basin_size = 1
    if row > 0:
        basin_size += crawler(heightmap, row - 1, col, map_size, already_visited)

    if row < map_size[0] - 1:
        basin_size += crawler(heightmap, row + 1, col, map_size, already_visited)

    if col > 0:
        basin_size += crawler(heightmap, row, col - 1, map_size, already_visited)

    if col < map_size[1] - 1:
        basin_size += crawler(heightmap, row, col + 1, map_size, already_visited)

    return basin_size


def prob1(heightmap):
    heigt_size = heightmap.shape
    risk_level_sum = 0
    for row in range(heigt_size[0]):
        for col in range(heigt_size[1]):

            lowest = is_lowest_level(heightmap, row, col, heigt_size)
            if lowest:
                risk_level_sum += heightmap[row, col] + 1

    print("Problem 1, risk level sum:", risk_level_sum)


def prob2(heightmap):
    heigt_size = heightmap.shape
    basin_sizes = []
    for row in range(heigt_size[0]):
        for col in range(heigt_size[1]):

            lowest = is_lowest_level(heightmap, row, col, heigt_size)
            if lowest:
                already_visited = []
                basin_sizes.append(
                    crawler(heightmap, row, col, heigt_size, already_visited)
                )
    three_largest = np.argsort(basin_sizes)[-3:]
    mult = 1
    for ind in three_largest:
        mult *= basin_sizes[ind]
    print("Problem 2, risk level sum:", mult)


def main():
    height_map = readData()

    prob1(height_map)
    prob2(height_map)


if __name__ == "__main__":
    main()
