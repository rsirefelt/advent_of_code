import numpy as np


def task1(grid):
    return update_grid(grid, count_adjacent, 4)


def task2(grid):
    return update_grid(grid, count_adjacent2, 5)


def update_grid(grid, adjacent_func, adjacent_lim):
    previous_grid = None
    iteration = 0
    while not np.array_equal(grid, previous_grid):
        iteration += 1
        print(f"\nGrid iteration: {iteration}")

        previous_grid = grid.copy()
        for row, line in enumerate(previous_grid):
            print(f"Processing row: {row} ", end="\r")
            for col, entry in enumerate(line):
                adjacent_count = adjacent_func(row, col, previous_grid)

                # Apply rules based on count.
                if entry == 0 and adjacent_count == 0:
                    grid[row, col] = 1
                elif entry == 1 and adjacent_count >= adjacent_lim:
                    grid[row, col] = 0

    return np.count_nonzero(grid == 1)


def count_adjacent(i, j, grid):
    """Check only adjacent seats"""
    count = 0
    x_lim, y_lim = grid.shape

    for x_step in [-1, 0, 1]:
        for y_step in [-1, 0, 1]:
            # Skip self
            if x_step == 0 and y_step == 0:
                continue

            x_coord = i + x_step
            y_coord = j + y_step

            # Check if coordinate is valid
            if 0 <= x_coord < x_lim and 0 <= y_coord < y_lim:
                count += grid[x_coord, y_coord] == 1

    return count


def count_adjacent2(i, j, grid):
    """Checks first seat in each direction"""
    count = 0
    x_lim, y_lim = grid.shape

    for x_step in [-1, 0, 1]:
        for y_step in [-1, 0, 1]:
            # Skip self
            if x_step == 0 and y_step == 0:
                continue

            found = False
            x_coord = i
            y_coord = j
            # Continue in direction until either outside of the grid or found seat.
            while not found:
                x_coord += x_step
                y_coord += y_step

                # Check if coordinate is valid
                if 0 <= x_coord < x_lim and 0 <= y_coord < y_lim:
                    if grid[x_coord, y_coord] == 1 or grid[x_coord, y_coord] == 0:
                        count += grid[x_coord, y_coord]
                        found = True
                else:
                    found = True

    return count


if __name__ == "__main__":
    with open("input") as f:
        lines = [line.rstrip() for line in f.readlines()]

    # Create grid
    grid = np.zeros((len(lines), len(lines[0])))
    translation = {".": -1, "L": 0, "#": 1}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            grid[row, col] = translation[char]

    res_1 = task1(grid.copy())
    res_2 = task2(grid.copy())

    print(f"\nResults: task1 = {res_1}, task2 = {res_2}")
