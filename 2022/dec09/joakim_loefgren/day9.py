import numpy as np

with open("./input.txt") as f:
    lines = f.read().splitlines()

unit_vecs = {
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "L": np.array([-1, 0]),
    "R": np.array([1, 0]),
}

# set 2 for part I
n_rope = 10
pos = np.zeros((n_rope, 2), dtype=np.int64)

visited = set([(0, 0)])

for line in lines:
    direc, step = line.split()
    step = int(step)
    trans_head = unit_vecs[direc]
    for s in range(step):
        pos[0, :] += trans_head
        pos_prev = pos[0, :]
        for i in range(1, n_rope):
            delta = pos_prev - pos[i, :]
            if np.any(np.abs(delta) > 1):
                pos[i, :] += np.sign(delta)
            pos_prev = pos[i, :]

        visited.add(tuple(pos[-1, :]))

print(len(visited))
