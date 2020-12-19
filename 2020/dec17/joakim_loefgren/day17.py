import numpy as np
from scipy.ndimage import correlate


def parse_input(input_file):
    with open(input_file, "r") as fp:
        trans = str.maketrans({".": "0 ", "#": "1 "})
        text = fp.read().translate(trans)
    pocket_slice = np.array(
        [np.fromstring(row, dtype=np.int64, sep=" ") for row in text.split("\n")[:-1]]
    )
    return pocket_slice


def create_pocket(pocket_slice, ncycles, ndim=3):
    nc = ncycles
    nx, ny = pocket_slice.shape
    shape = 2 * nc * np.ones(ndim, dtype=np.int64)
    shape[:2] += pocket_slice.shape
    shape[2:] += 1
    pocket = np.zeros(shape, dtype=np.int64)
    inds = nc * np.ones((ndim, 2), dtype=np.int64)
    inds[0, 1] += nx
    inds[1, 1] += ny
    slc = (slice(nc, nc + nx), slice(nc, nc + ny)) + (nc,) * (ndim - 2)
    pocket[slc] = pocket_slice
    return pocket, inds


def execute_pocket(pocket, inds, ncycles, ndim=3):
    neighbor_filter = np.ones((3,) * ndim, dtype=np.int64)
    neighbor_filter[(1,) * ndim] = 0
    pocket_new = pocket.copy()
    for i in range(1, ncycles + 1):
        slc = []
        for d in range(ndim):
            slc.append(slice(inds[d, 0] - i, inds[d, 1] + i + 1))

        ps = pocket[tuple(slc)]
        ps_new = pocket_new[tuple(slc)]
        nbs = correlate(ps, neighbor_filter, mode="constant", cval=0)
        ps_new[np.logical_and(ps == 0, nbs == 3)] = 1
        ps_new[np.logical_and(ps == 1, ~np.logical_or(nbs == 2, nbs == 3))] = 0
        ps[:] = ps_new

    return np.sum(pocket)


if __name__ == "__main__":
    pocket_slice = parse_input("./input_day17.txt")
    ncycles = 6

    ndim = 3   # Part I
    pocket, inds = create_pocket(pocket_slice, ncycles, ndim=ndim)
    print(execute_pocket(pocket, inds, ncycles, ndim))

    ndim = 4  # Part II
    pocket, inds = create_pocket(pocket_slice, ncycles, ndim=ndim)
    print(execute_pocket(pocket, inds, ncycles, ndim))
