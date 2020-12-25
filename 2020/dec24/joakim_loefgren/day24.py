""" Advent of Code Day 24 """
import numpy as np


def load_input(input_file):
    with open(input_file) as fp:
        lines = fp.read().splitlines()

    return lines


if __name__ == "__main__":
    renovation_list = load_input("./input_day24.txt")

    # Represent each tile position in terms of its coords. relative
    # units vectors pointing east and north east.
    cardinal_coords = {
        "e": (1, 0),
        "w": (-1, 0),
        "ne": (0, 1),
        "sw": (0, -1),
        "nw": (-1, 1),
        "se": (1, -1),
    }

    tiles = {}
    x = np.zeros(2, dtype=np.int64)
    for cardinals in renovation_list:
        it_cardinals = iter(cardinals)
        while c := next(it_cardinals, False):
            dx = cardinal_coords.get(c)
            if not dx:
                c += next(it_cardinals)
                dx = cardinal_coords[c]
            x += dx
        x_t = tuple(x)
        tiles[x_t] = 1 - tiles.get(x_t, 0)
        x[:] = 0

    # Part I
    print(sum(tiles.values()))

    # Part II
    n_days = 100
    for d in range(1, n_days + 1):
        flip = {}
        # Determine flips for black tiles by counting neighbors 
        # and add white neighbors when missing.
        for x in list(tiles.keys()):
            x_neighbors = [
                    (x[0] + dx[0], x[1] + dx[1])
                    for dx in cardinal_coords.values()
                ]
            count = 0
            for x_n in x_neighbors:
                if not tiles.get(x_n):
                    tiles[x_n] = 0
                else:
                    count += tiles[x_n]
            color = tiles[x]
            if color == 1:
                if count == 0 or count > 2:
                    flip[x] = 1
                else:
                    flip[x] = 0
            else:
                if count == 2:
                    flip[x] = 1
                else:
                    flip[x] = 0
        # Determine flips for white tiles.
        for x in tiles:
            if x not in flip:
                x_neighbors = [
                        (x[0] + dx[0], x[1] + dx[1])
                        for dx in cardinal_coords.values()
                    ]
                count = sum([tiles.get(x_n, 0) for x_n in x_neighbors])
                color = tiles[x]
                if count == 2:
                    flip[x] = 1

        # perform flips
        for x in flip:
            if flip[x]:
                tiles[x] = 1 - tiles[x]

    print(sum(tiles.values()))
