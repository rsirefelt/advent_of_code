import re

import numba
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


@numba.jit(nopython=True)
def find_first(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i


@numba.jit(nopython=True)
def find_first_nonzero(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            return i


if __name__ == "__main__":
    maze, instructions = parse_input("./input.txt")
    pos = complex(1, find_first_nonzero(maze[1]))
    dir = 1j
    ROT = {"L": 1j, "R": -1j}

    for instr in instructions:
        if instr in ["L", "R"]:
            dir *= ROT[instr]
        else:
            for _ in range(int(instr)):
                pos_new = pos + dir
                ind = (int(pos_new.real), int(pos_new.imag))
                tile = maze[ind]
                if tile == 2:
                    break
                elif tile == 1:
                    pos = pos_new
                else:
                    # find tiles ahead
                    if dir == 1:
                        tiles_ahead = maze[:, ind[1]]
                        axis = 0
                    elif dir == 1j:
                        tiles_ahead = maze[ind[0], :]
                        axis = 1
                    elif dir == -1:
                        tiles_ahead = maze[::-1, ind[1]]
                        axis = 0
                    elif dir == -1j:
                        tiles_ahead = maze[ind[0], ::-1]
                        axis = 1
                    else:
                        raise RuntimeError("Unkown direction")
                    i_next = find_first_nonzero(tiles_ahead)
                    tile_next = tiles_ahead[i_next]
                    if tile_next == 2:
                        break
                    if tile_next == 1:
                        pos_tmp = [pos.real, pos.imag]
                        pos_tmp[axis] = i_next
                        pos = complex(*pos_tmp)

    # calc score
    DIR_SCORES = {1j: 0, 1: 1, -1j: 2, -1: 3}
    score = int(1000*pos.real + 4*pos.imag + DIR_SCORES[dir])
    print(score)
