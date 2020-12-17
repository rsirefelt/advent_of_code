import numpy as np
from scipy.ndimage import correlate


def run_game(state, neghbor_filter, n_iterations):
    state = np.pad(state, n_iterations)
    for i in range(n_iterations):
        neighbor_count = correlate(state, neghbor_filter)

        to_inactive = np.logical_and(np.logical_and(neighbor_count != 2, neighbor_count != 3), state == 1)
        to_active = np.logical_and(neighbor_count == 3, state == 0)

        state[to_active] = 1
        state[to_inactive] = 0

    return state


initial_conf = []
with open('inputs/day17') as f:
    for line in f:
        row = line.rstrip()
        rowmap = np.array([c == '#' for c in row])
        initial_conf.append(rowmap)

conf = np.expand_dims(np.array(initial_conf), axis=-1).astype(np.int)
neghbor_filter = np.ones((3, 3, 3), dtype=np.int)
neghbor_filter[1, 1, 1] = 0

print(f'a) {run_game(conf, neghbor_filter, 6).sum()}')

conf = np.expand_dims(np.expand_dims(np.array(initial_conf), axis=-1), axis=-1).astype(np.int)
neghbor_filter = np.ones((3, 3, 3, 3), dtype=np.int)
neghbor_filter[1, 1, 1, 1] = 0

print(f'b) {run_game(conf, neghbor_filter, 6).sum()}')
