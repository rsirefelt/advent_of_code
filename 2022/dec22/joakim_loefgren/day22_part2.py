import re

import numpy as np


def parse_input(filename):

    with open(filename) as f:
        maze_text, instr_text = f.read().split("\n\n")

    # parse maze
    trans = str.maketrans({" ": "0 ", ".": "1 ", "#": "2 "})
    maze_text = maze_text.translate(trans)
    rows = maze_text.split("\n")
    shape = (len(rows), max([len(r) for r in rows]) // 2)
    maze = np.zeros(shape, dtype=int)
    for i, row in enumerate(rows):
        diff = maze.shape[1] - len(row) // 2
        if diff > 0:
            row += "0 " * diff
        maze[i, :] = np.fromstring(row, sep=" ", dtype=int)

    # extra zero padding to avoid range checks
    maze_big = np.zeros((maze.shape[0] + 2, maze.shape[1] + 2), dtype=int)
    maze_big[1:-1, 1:-1] = maze

    # parse path
    instructions = re.findall(r"(\d+|[LR])", instr_text)
    return maze_big, instructions


def label_cubes(maze, side):
    cube_curr = 1
    cubes = np.zeros_like(maze)
    icorner_cubes = {}
    for i in range(0, maze.shape[0]//side):
        for j in range(0, maze.shape[1]//side):
            ind = (i*side + 1, j*side + 1)
            if maze[ind] != 0:
                cubes[ind[0]:ind[0] + side, ind[1]: ind[1] + side] = cube_curr
                icorner_cubes[cube_curr] = np.array(ind, dtype=int)
                cube_curr += 1
    return cubes, icorner_cubes


def transition_index(ilocal, trans, refl, axis, side=50):
    ilocal_nb = np.array([0, 0])
    if trans:
        ilocal_nb[axis] = ilocal[1 - axis]
    else:
        ilocal_nb[axis] = ilocal[axis]
    if refl:
        ilocal_nb[axis] = side - 1 - ilocal_nb[axis]
    return ilocal_nb


if __name__ == "__main__":
    maze, instructions = parse_input("./input.txt")
    pos = complex(1, maze[1].view(bool).argmax() // maze[1].itemsize)
    facing = 1j
    # facing >: 1j, <: -1j, ^: -1, v: 1
    ROT = {"L": 1j, "R": -1j}
    side = 50
    cubes, icorner_cubes = label_cubes(maze, side)

    # maps [cube][facing] -> (cube_neighbor, new_facing, transpose, reflect)
    # if transpose we go from row -> col on wrap
    # if reflex we go from row( or col) -> len - 1 - row( or col)
    TOPOLOGY = {
        1: {-1j: (4, 1j, False, True), -1: (6, 1j, True, False)},
        2: {1j: (5, -1j, False, True), 1: (3, -1j, True, False), -1: (6, -1, False, False)},
        3: {1j: (2, -1, True, False), -1j: (4, 1, True, False)},
        4: {-1j: (1, 1j, False, True), -1: (3, 1j, True, False)},
        5: {1j: (2, -1j, False, True), 1: (6, -1j, True, False)},
        6: {1j: (5, -1, True, False), -1j: (1, 1, True, False), 1: (2, 1, False, False)},
    }

    for instr in instructions:
        if instr in ["L", "R"]:
            facing *= ROT[instr]
        else:
            for _ in range(int(instr)):
                pos_new = pos + facing
                iglobal_new = (int(pos_new.real), int(pos_new.imag))
                tile = maze[iglobal_new]
                if tile == 2:
                    break
                elif tile == 1:
                    pos = pos_new
                else:
                    # get topological info
                    iglobal = np.array([int(pos.real), int(pos.imag)])
                    cube = cubes[tuple(iglobal)]
                    cube_new, facing_new, trans, refl = TOPOLOGY[cube][facing]
                    
                    # get local cube index
                    icorner = icorner_cubes[cube]
                    ilocal = iglobal - icorner
                    
                    flip = False
                    if facing_new in [1, -1]:
                        axis = 1
                        ilocal_new = transition_index(ilocal, trans, refl, axis)
                        flip = facing_new < 0
                    else:  # 1j, -1j
                        axis = 0
                        ilocal_new = transition_index(ilocal, trans, refl, axis)
                        flip = facing_new.imag < 0 

                    # transform back to global indices
                    icorner_new = icorner_cubes[cube_new]
                    if flip:
                        ilocal_new[1 - axis] = side - 1
                    iglobal_new = ilocal_new + icorner_new
                    tile_new = maze[tuple(iglobal_new)]

                    if tile_new == 2:
                        break
                    else:
                        # update pos and facing
                        facing = facing_new
                        pos = complex(*tuple(iglobal_new))
                        
    # calc score
    FACING_SCORES = {1j: 0, 1: 1, -1j: 2, -1: 3}
    score = int(1000*pos.real + 4*pos.imag + FACING_SCORES[facing])
    print(score)
