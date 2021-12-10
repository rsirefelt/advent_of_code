import numpy as np
from itertools import product


def parse_input(file_path="./input_day9.txt"):
    """Reads the height map and adds some padding. """
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        heights = 9*np.ones((len(lines) + 2, len(lines[0]) + 2), dtype=int)
        for i, line in enumerate(lines):
            heights[1 + i:-1, 1:-1] = [int(c) for c in line]
    return heights


class BasinFinder:
    def __init__(self, heights):
        self.heights = heights
        self.labels = -1 * (self.heights == 9).astype(int)
        self.max_label = 1

    def calc_risk_level(self):
        heights = self.heights
        nrows, ncols = np.array(heights.shape) - 2
        risk_level = 0
        for i, j in product(range(1, nrows + 1), range(1, ncols + 1)):
            heights_nn = [
                heights[inds[0], inds[1]] for inds in self.get_neighbors(i, j)
            ]
            if any(heights[i, j] >= h for h in heights_nn):
                continue
            else:
                risk_level += heights[i, j] + 1
        return risk_level

    def get_neighbors(self, i, j):
        return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j -1)]

    def label_neighbors(self, i, j):
        """Recursively label neighboring points starting from i, j. """
        if self.labels[i, j] == 0:
            self.labels[i, j] = self.max_label
            for inds in self.get_neighbors(i, j):
                self.label_neighbors(*inds)
            return True
        return False

    def run(self):
        nrows, ncols = np.array(self.labels.shape) - 2
        for i, j in product(range(1, nrows + 1), range(1, ncols + 1)):
            if self.label_neighbors(i, j):
                self.max_label += 1

    def get_sizes(self):
        sizes = []
        for label in range(1, self.max_label):
            sizes.append(np.sum(self.labels == label))
        return sizes


if __name__ == '__main__':
    heights = parse_input()
    basin_finder = BasinFinder(heights)

    # Part I 
    print(basin_finder.calc_risk_level())

    # Part II
    basin_finder.run()
    sizes = basin_finder.get_sizes()
    print(np.product(np.sort(sizes)[-3:]))
