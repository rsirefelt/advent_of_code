import numpy as np


def count_trees(input_file, slopes):
    num_trees = np.zeros(slopes.shape[0], np.int64)
    with open(input_file) as fp:
        for iline, line in enumerate(fp):
            for islope, slope in enumerate(slopes):
                right, down = slope
                if iline % down == 0:
                    num_cols = len(line) - 1
                    if line[(iline//down * right) % num_cols] == "#":
                        num_trees[islope] += 1

    return np.product(num_trees)


if __name__ == "__main__":

    input_file = "input_day3.txt"

    # Part I
    slopes = np.array([[3, 1]])
    print(count_trees(input_file, slopes))

    # Part II
    slopes = np.array([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])
    print(count_trees(input_file, slopes))
