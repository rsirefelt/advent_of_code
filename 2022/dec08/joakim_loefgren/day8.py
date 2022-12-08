import numpy as np

trees = np.loadtxt("./input.txt", dtype=str)
trees = np.array([list(row) for row in trees], dtype=np.int64)

# Part I
num_visible = 2 * (trees.shape[0] + trees.shape[1] - 2)
for k in range(trees.size):
    i, j = np.unravel_index(k, trees.shape)
    if 0 < i < trees.shape[0] - 1 and 0 < j < trees.shape[1] - 1:
        t = trees[i, j]
        if (
            np.all(trees[:i, j] < t)
            or np.all(trees[i + 1 :, j] < t)
            or np.all(trees[i, :j] < t)
            or np.all(trees[i, j + 1 :] < t)
        ):
            num_visible += 1
            continue

print(num_visible)

# Part II
def calc_view_dists(trees, i, j, direction=None):
    t = trees[i, j]
    if direction == 'up':
        tree_line = trees[:i, j][::-1]
    elif direction == 'down':
        tree_line = trees[i + 1:, j]
    elif direction == 'left':
        tree_line = trees[i, :j][::-1]
    elif direction == 'right':
        tree_line = trees[i, j + 1:]
    else:
        return 0
    inds = np.where(tree_line >= t)[0]
    if len(inds) > 0:
        return inds[0] + 1
    else:
        return len(tree_line)
        

scores = np.zeros(trees.size, dtype=np.int64)
directions = ['up', 'down', 'left', 'right']
for k in range(trees.size):
    view_dists = []
    i, j = np.unravel_index(k, trees.shape)
    if 0 < i < trees.shape[0] - 1 and 0 < j < trees.shape[1] - 1:
        for direc in directions:
            view_dists.append(calc_view_dists(trees, i, j, direction=direc))
    scores[k] = np.product(view_dists)

print(np.max(scores))
