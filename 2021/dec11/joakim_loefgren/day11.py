import numpy as np


def parse_input(file_path="./input_day11.txt"):
    """Reads the height map and adds some padding. """
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        grid = np.zeros((len(lines) + 2, len(lines[0]) + 2), dtype=int)
        for i, line in enumerate(lines):
            grid[i + 1, 1:-1] = [int(c) for c in line]
    return grid


class OctopusGrid:
    def __init__(self, grid):
        self.grid = grid
        self.has_flashed = []
        self.total_flashes = 0
        self.recent_flashes = 0

    def get_neighbors(self, i, j):
        return [
            (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1),
            (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1),
        ]

    def step(self, num=1):
        for i in range(num):
            self.grid += 1
            self.has_flashed = []
            inds = np.argwhere(self.grid > 9)

            for i, j in inds:
                self._flash(i, j)

            for i, j in self.has_flashed:
                self.grid[i, j] = 0

            self.recent_flashes = len(self.has_flashed)
            self.total_flashes += self.recent_flashes

    def _inbounds(self, i, j):
        grid = self.grid
        return (0 < i < grid.shape[0] - 1) and (0 < j < grid.shape[1] - 1)

    def should_flash(self, i, j):
        condition = (
            self._inbounds(i, j) and self.grid[i, j] > 9 and (i, j) not in self.has_flashed
        )
        return condition

    def _flash(self, i, j):
        if self.should_flash(i, j):
            grid = self.grid
            grid[i - 1: i + 2, j - 1: j + 2] += 1
            self.has_flashed.append((i, j))
            for ij in self.get_neighbors(i, j):
                self._flash(*ij)

    @property
    def size(self):
        return (self.grid.shape[0] - 2) * (self.grid.shape[1] - 2)

    def view(self):
        print(self.grid[1:-1, 1:-1])

    def run(self, num_steps):
        for i in range(num_steps):
            self.step()
    
if __name__ == '__main__':
    grid = parse_input()
    og = OctopusGrid(grid.copy())

    # Part I 
    og.step(100)
    print(og.total_flashes)

    # Part II
    og = OctopusGrid(grid)
    num_step = 0
    while og.recent_flashes < og.size:
        og.step()
        num_step += 1
    print(num_step)
