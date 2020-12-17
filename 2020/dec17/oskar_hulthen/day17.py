from itertools import product
import numpy as np


def task(grid, target_dims=3, cycles=6):
    dim_diff = target_dims - len(grid.shape)

    # Expand dimensions to target dims.
    for _ in range(dim_diff):
        grid = np.expand_dims(grid, -1)

    # Get adjacent steps.
    step_combinations = list(product([-1, 0, 1], repeat=target_dims))
    # Remove 0 step
    step_combinations.remove(tuple([0] * target_dims))

    for i in range(cycles):
        # Pad with inactive nodes for each dimension -1, +1 (as these needs to be checked).
        padding = [(1, 1) for _ in range(target_dims)]
        grid = np.pad(grid, padding)

        previous_grid = grid.copy()

        # Check all elements in the previous grid.
        for idx in np.ndindex(previous_grid.shape):
            prev_val = previous_grid[idx]
            adjacent_count = count_adjacent(idx, previous_grid, step_combinations)

            if prev_val == 1 and adjacent_count not in [2, 3]:
                grid[idx] = 0
            elif prev_val == 0 and adjacent_count == 3:
                grid[idx] = 1

    return np.count_nonzero(grid)


def count_adjacent(idx, grid, combinations):
    """Count cubes that are idx + combinations[i] steps apart."""
    count = 0
    limits = grid.shape
    for step in combinations:
        # Add tuple
        test_idx = tuple(dim_idx + dim_step for dim_idx, dim_step in zip(idx, step))
        try:
            count += grid[test_idx] == 1
        except IndexError:
            # Skip indices that are outside defined grid
            continue

    return count


if __name__ == "__main__":
    with open("input") as f:
        lines = [line.rstrip() for line in f.readlines()]

    # Create grid
    grid = np.zeros((len(lines), len(lines[0])))
    translation = {".": 0, "#": 1}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            grid[row, col] = translation[char]

    res_1 = task(grid.copy())
    res_2 = task(grid.copy(), target_dims=4)

    print(f"\nResults: task1 = {res_1}, task2 = {res_2}")
