import itertools
from collections import deque

import numpy as np


def count_neighbors(cubes, pos):
    neighbors = [
        (pos[0] + 1, pos[1], pos[2]),
        (pos[0] - 1, pos[1], pos[2]),
        (pos[0], pos[1] + 1, pos[2]),
        (pos[0], pos[1] - 1, pos[2]),
        (pos[0], pos[1], pos[2] + 1),
        (pos[0], pos[1], pos[2] - 1),
    ]
    return sum(1 for nb in neighbors if nb in cubes)


def get_bounded_neighbors(pos, bounds):
    neighbors = []
    if bounds[0, 0] < pos[0]:
        neighbors.append((pos[0] - 1, pos[1], pos[2]))
    if bounds[0, 1] > pos[0]:
        neighbors.append((pos[0] + 1, pos[1], pos[2]))
    if bounds[1, 0] < pos[1]:
        neighbors.append((pos[0], pos[1] - 1, pos[2]))
    if bounds[1, 1] > pos[1]:
        neighbors.append((pos[0], pos[1] + 1, pos[2]))
    if bounds[2, 0] < pos[2]:
        neighbors.append((pos[0], pos[1], pos[2] - 1))
    if bounds[2, 1] > pos[2]:
        neighbors.append((pos[0], pos[1], pos[2] + 1))
    return neighbors


def find_exterior(cubes, bounds):
    """BFS search"""
    pos = tuple(bounds[:, 0])
    exterior = set([pos])
    que = deque([pos])
    while len(que) > 0:
        pos = que.pop()
        for nb in get_bounded_neighbors(pos, bounds):
            if nb not in cubes and nb not in exterior:
                exterior.add(nb)
                que.appendleft(nb)
    return exterior


if __name__ == "__main__":

    cube_locs = np.loadtxt("./input.txt", delimiter=",", dtype=int)
    cubes = set(tuple(row) for row in cube_locs)
    total_area = sum(6 - count_neighbors(cubes, c) for c in cubes)
    print(total_area)  # part I

    x_max = np.max(cube_locs[:, 0])
    y_max = np.max(cube_locs[:, 1])
    z_max = np.max(cube_locs[:, 2])
    bounds = np.array([[-1, x_max + 1], [-1, y_max + 1], [-1, z_max + 1]])
    exterior = find_exterior(cubes, bounds)
    space = set(pos for pos in itertools.product(*[range(*tuple(b)) for b in bounds]))
    interior = space - set.union(exterior, cubes)
    cubes.update(interior)
    exterior_area = sum(6 - count_neighbors(cubes, c) for c in cubes)
    print(exterior_area)  # part II
