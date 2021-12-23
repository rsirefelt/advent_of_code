import numpy as np
from itertools import product


def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        density = np.zeros((len(lines), len(lines[0])), dtype=int)
        for i, line in enumerate(lines):
            density[i, :] = [int(c) for c in line]
    return density


class Pathfinder:

    def __init__(self, density):
        self.density = density
        self.risk_min = int(1e8)
        self.pos_end = (density.shape[0] - 1, density.shape[1] - 1)

    def tile(self, reps=(5, 5)):
        density = self.density
        nx = density.shape[0]
        ny = density.shape[1]
        density_new = np.zeros((reps[0]*nx, reps[1]*ny), dtype=int)
        for i in range(reps[0]):
            for j in range(reps[0]): 
                density_new[i*nx : (i + 1)*nx, j*ny : (j + 1)*ny] = density + i + j

        self.pos_end = (density.shape[0] - 1, density.shape[1] - 1)
        self.density = np.array(density_new)
        self.density[self.density > 9] = self.density[self.density > 9] % 9

    def dynamic(self):
        risks = np.zeros_like(self.density, dtype=int)
        density = self.density
        density[0, 0] = 0
        risks[0, :] = np.cumsum(density[0, :]) 
        risks[:, 0] = np.cumsum(density[:, 0]) 
        density[0, 0] = 1

        # initialize: coming from top or left
        for i, j in product(range(1, risks.shape[0]), range(1, risks.shape[1])):
            risks[i, j] = density[i, j] + min(risks[i - 1, j], risks[i, j - 1])

        #####
        changes = True
        risks_copy = np.zeros_like(risks)
        while changes:
            risks_copy[:, :] = risks
            # coming from right
            for i in range(density.shape[1] - 1):
                risks[:, i] = np.minimum(risks[:, i], risks[:, i + 1] + density[:, i])
            # coming from bottom
            for i in range(density.shape[0] - 1):
                risks[i, :] = np.minimum(risks[i, :], risks[i + 1, :] + density[i, :])
            # coming from top
            for i in range(1, density.shape[0]):
                risks[i, :] = np.minimum(risks[i, :], risks[i - 1, :] + density[i, :])
            # coming from left
            for i in range(1, density.shape[1]):
                risks[:, i] = np.minimum(risks[:, i], risks[:, i - 1] + density[:, i])
            changes = not np.array_equal(risks, risks_copy)
        return risks
 

if __name__ == '__main__':
    density = parse_input('./input_day15.txt')

    # Part I
    pf = Pathfinder(density)
    risks = pf.dynamic()
    print(risks[-1, -1])

    # Part II
    pf = Pathfinder(density)
    pf.tile()
    risks = pf.dynamic()
    print(risks[-1, -1])
