import re
import copy

import numpy as np


class Cave:
    def __init__(self, rocks, add_floor=True):
        """Build cave"""
        self.rocks = copy.deepcopy(rocks)
        xlim = [0, np.max([np.max(path[:, 1]) for path in self.rocks])]
        ylim = [
            np.min([np.min(path[:, 0]) for path in self.rocks]),
            np.max([np.max(path[:, 0]) for path in self.rocks]),
        ]
        if add_floor:
            xlim[1] += 2
            ylim[0] -= 150
            ylim[1] += 150
        
        grid = np.zeros((xlim[1] - xlim[0] + 1, ylim[1] - ylim[0] + 1), dtype=np.int64)
        if add_floor:
            grid[xlim[1], :] = 1
        source = (0, 500 - ylim[0])
        grid[source[0], source[1]] = 3
        for path in self.rocks.copy():
            path[:, 0] -= ylim[0]
            for i in range(path.shape[0] - 1):
                start = path[i, :]
                stop = path[i + 1, :]
                if start[0] > stop[0] or start[1] > stop[1]:
                    start, stop = stop, start
                grid[start[1] : stop[1] + 1, start[0] : stop[0] + 1] = 1
        self.grid = grid
        self.source = source

    def __str__(self):
        s = np.zeros_like(self.grid, dtype=str)
        s[:, :] = "."
        s[self.grid == 1] = "#"  # rock
        s[self.grid == 3] = "+"  # source
        s[self.grid == 2] = "o"  # sand
        s = "\n".join(["".join(row) for row in s])
        return s

    def drop_sand(self):
        grid = self.grid
        num_sand = 0
        try:
            while True:
                num_sand += 1
                ind = (self.source[0], self.source[1])
                grid[ind] = 2
                while True:
                    for ind_new in [
                        (ind[0] + 1, ind[1]),
                        (ind[0] + 1, ind[1] - 1),
                        (ind[0] + 1, ind[1] + 1),
                    ]:
                        if grid[ind_new] == 0:
                            grid[ind] = 0
                            grid[ind_new] = 2
                            ind = ind_new
                            break  # moved
                    else:
                        if ind == self.source:
                            print('Source blocked')
                            return num_sand
                        break  # nowhere to move
        except IndexError:
            grid[ind] = 0
            print('Sand fallling outside')
            return num_sand - 1


if __name__ == "__main__":
    rocks = []
    with open("./input.txt") as f:
        for line in f:
            rock_path = re.findall(r"(\d+),(\d+)", line.strip())
            rocks.append(np.array(rock_path, dtype=np.int64))

    # part I
    cave = Cave(rocks, add_floor=False)
    print(cave.drop_sand())

    # part II
    cave = Cave(rocks, add_floor=True)
    print(cave.drop_sand())
