import numpy as np
from scipy import ndimage


def get_active_cubes(input_, n_dim, n_cycles):
    for i in range(n_dim - 2):
        input_ = np.expand_dims(input_, axis=-1)

    d_size = [input_.shape[0] + 2 * n_cycles, input_.shape[1] + 2 * n_cycles]

    for i in range(n_dim - 2):
        d_size.append(1 + 2 * n_cycles)

    pocket_dim = np.zeros(d_size, dtype=np.int32)

    init_s = [
        slice(
            int((d_size[0] - input_.shape[0]) / 2),
            int((d_size[0] + input_.shape[0]) / 2),
        ),
        slice(
            int((d_size[1] - input_.shape[1]) / 2),
            int((d_size[1] + input_.shape[1]) / 2),
        ),
    ]

    for i in range(n_dim - 2):
        init_s.append(slice(int((d_size[i + 2] / 2)), int((d_size[i + 2] / 2) + 1)))

    pocket_dim[init_s] = input_

    k = np.ones([3] * n_dim, dtype=np.int32)
    k[(1,) * n_dim] = 0
    for i in range(n_cycles):
        nonzero_idx = np.nonzero(pocket_dim)
        s = np.min(nonzero_idx, axis=1) - 1
        e = np.max(nonzero_idx, axis=1) + 2
        roi_r = []
        for i in range(n_dim):
            roi_r.append(slice(s[i], e[i]))

        roi = pocket_dim[roi_r].copy()
        conv_out = ndimage.convolve(roi, k, mode="constant").ravel()

        it = np.nditer(roi.ravel(), flags=["f_index"], op_flags=["readwrite"])
        for c in it:
            if c == 1:
                c[...] = 1 if conv_out[it.index] in range(2, 4) else 0
            else:
                c[...] = 1 if conv_out[it.index] == 3 else 0
        pocket_dim[roi_r] = roi

    return np.sum(pocket_dim)


input_ = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_.append([c for c in line.replace("#", "1").replace(".", "0").rstrip()])

input_ = np.array(input_, dtype=np.int32)
n_cycles = 6
print(f"1) Number of active cubes {get_active_cubes(input_, 3, n_cycles)}")
print(f"2) Number of active cubes {get_active_cubes(input_, 4, n_cycles)}")
