import numpy as np
import matplotlib.pyplot as plt


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        octopuses = []

        for line in input_lines:
            octopuses.append([int(c) for c in line.rstrip()])

    return np.array(octopuses)


def update_neighbours(octopuses, not_flashed, row, col, size):
    if 0 < row < size[0] - 1:
        min_row = row - 1
        max_row = row + 2
    elif row == 0:
        min_row = row
        max_row = row + 2
    elif row == size[0] - 1:
        min_row = row - 1
        max_row = row + 1

    if 0 < col < size[1] - 1:
        min_col = col - 1
        max_col = col + 2
    elif col == 0:
        min_col = col
        max_col = col + 2
    elif col == size[1] - 1:
        min_col = col - 1
        max_col = col + 1

    octopuses[min_row:max_row, min_col:max_col] += 1
    not_flashed[row, col] = False

    return (octopuses, not_flashed)


def update_octopuses(octopuses, octopuses_shape, image=None):
    not_flashed = np.ones_like(octopuses, dtype=bool)
    flashes = 0
    while len(octopuses[not_flashed]) > 0 and octopuses[not_flashed].max() > 9:
        for row in range(octopuses_shape[0]):
            for col in range(octopuses_shape[1]):
                if octopuses[row, col] > 9 and not_flashed[row, col]:
                    flashes += 1
                    octopuses, not_flashed = update_neighbours(
                        octopuses, not_flashed, row, col, octopuses_shape
                    )

        if len(octopuses[not_flashed]) == 0:
            break
    if image:
        image.set_data(octopuses)
        plt.draw()
        plt.pause(0.05)
    octopuses[octopuses > 9] = 0

    return flashes


def prob1(octopuses):
    octopuses_shape = octopuses.shape
    num_steps = 100
    flashes = 0

    for step in range(0, num_steps):
        octopuses += 1
        current_flashes = update_octopuses(octopuses, octopuses_shape)
        flashes += current_flashes

    print("Problem 1, flashes:", flashes)


def prob2(octopuses):
    octopuses_shape = octopuses.shape
    num_steps = 1000
    flashes = 0
    image = plt.imshow(octopuses, cmap="cividis")
    plt.ion()
    plt.show()
    for step in range(0, num_steps):
        octopuses += 1
        current_flashes = update_octopuses(octopuses, octopuses_shape, image)
        flashes += current_flashes

        if current_flashes == 100:
            print("Problem 2, Num steps:", step + 1)
            plt.pause(5.0)
            break


def main():
    octopuses = readData()
    prob1(octopuses)

    octopuses = readData()
    prob2(octopuses)


if __name__ == "__main__":
    main()
