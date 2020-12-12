from itertools import product

import numpy as np


def parse_input(input_file="input_day11.py"):
    with open(input_file, "r") as fp:
        text_trans = fp.read().translate(str.maketrans({".": "-1 ", "L": "0 "}))
        lines = text_trans.split("\n")[:-1]

    seats = np.vstack([np.fromstring(line, dtype=np.int64, sep=" ") for line in lines])
    return seats


def neighborhood(seats, i, j):
    nbh = seats[max(i - 1, 0) : i + 2, max(j - 1, 0) : j + 2].flatten()
    inds = np.argwhere(nbh == seats[i, j])
    nbh = np.delete(nbh, inds[0][0])
    nbh = nbh[nbh != -1]
    return nbh


def line_of_sight(seats, i, j):
    visible = np.zeros(8, np.int64)
    visible[0] = _first_visible(seats[i, j + 1 :])
    visible[1] = _first_visible(seats[i, :j][::-1])
    visible[2] = _first_visible(seats[i + 1 :, j])
    visible[3] = _first_visible(seats[:i, j][::-1])
    visible[4] = _first_visible(_diag_view(seats, i, j, view="top right"))
    visible[5] = _first_visible(_diag_view(seats, i, j, view="top left"))
    visible[6] = _first_visible(_diag_view(seats, i, j, view="bottom right"))
    visible[7] = _first_visible(_diag_view(seats, i, j, view="bottom left"))
    return visible[visible != -1]


def _diag_view(arr, i, j, view="top right"):
    nrows, ncols = arr.shape
    if view == "top right":
        lim = min(i + 1, ncols - j)
        diag = np.array([arr[i - k, j + k] for k in range(1, lim)])
    elif view == "bottom right":
        lim = min(nrows - i, ncols - j)
        diag = np.array([arr[i + k, j + k] for k in range(1, lim)])
    elif view == "bottom left":
        lim = min(nrows - i, j + 1)
        diag = np.array([arr[i + k, j - k] for k in range(1, lim)])
    elif view == "top left":
        lim = min(i + 1, j + 1)
        diag = np.array([arr[i - k, j - k] for k in range(1, lim)])
    else:
        raise ValueError("Invalid view")
    return diag


def _first_visible(ray):
    for i in range(len(ray)):
        if ray[i] in [0, 1]:
            return ray[i]
    return -1


def apply_rules(seats, proximity_func, tol):
    new_seats = seats.copy()
    nrows, ncols = seats.shape
    for i, j in product(range(nrows), range(ncols)):
        if seats[i, j] == 0:
            nbh = proximity_func(seats, i, j)
            if np.all(nbh == 0):
                new_seats[i, j] = 1
        elif seats[i, j] == 1:
            nbh = proximity_func(seats, i, j)
            if np.sum(nbh == 1) >= tol:
                new_seats[i, j] = 0
    return new_seats


def occupancy(seats):
    return np.sum(seats[seats != -1])


def equilibrium_occupancy(seats, proximity_func, tol, max_iter=200):
    for i in range(max_iter):
        new_seats = apply_rules(seats, proximity_func, tol)
        if np.array_equal(seats, new_seats):
            seats = new_seats
            break
        seats = new_seats
    else:
        print("Equilibrum not reached.")
    return occupancy(seats)


def print_seats(seats):
    subs = {-1: ".", 0: "L", 1: "#"}
    seats_str = ""
    for row in seats:
        seats_str += "".join([subs[s] for s in row]) + "\n"
    print(seats_str)


if __name__ == "__main__":

    seats = parse_input()

    # Part I
    occ = equilibrium_occupancy(seats, neighborhood, 4)
    print(occ)

    # Part II
    occ = equilibrium_occupancy(seats, line_of_sight, 5)
    print(occ)
