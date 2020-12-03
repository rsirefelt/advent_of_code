import numpy as np


def task():
    with open("input") as f:
        map_ = [line.rstrip() for line in f]

    num_rows = len(map_)
    num_cols = len(map_[0])

    steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = []
    for current_step in steps:
        current_step = np.array(current_step)
        position = current_step.copy()
        tree_count = 0

        while position[1] < num_rows:
            tree_count += map_[position[1]][position[0]] == "#"

            position += current_step

            # End is solely based on rows (loop columns)
            position[0] = position[0] % num_cols

        print(f"step {current_step}: {tree_count} trees")
        tree_counts.append(tree_count)
    print(f"Mul result: {np.prod(tree_counts)}")


if __name__ == "__main__":
    task()
