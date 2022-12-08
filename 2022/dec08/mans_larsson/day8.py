import numpy as np

with open('inputs/day8') as f:
    data = f.read().splitlines()

tree_grid = np.stack([np.array([int(c) for c in data[i]]) for i in range(len(data))])
visible = np.zeros_like(tree_grid, dtype=bool)


for start_index, increment in zip((0, tree_grid.shape[1]-1), (1, -1)):
    for i in range(tree_grid.shape[0]):
        tree_height = -1
        current_index = start_index
        for _ in range(tree_grid.shape[1]):
            if tree_grid[i, current_index] > tree_height:
                visible[i, current_index] = True
                tree_height = tree_grid[i, current_index]
            current_index += increment

for start_index, increment in zip((0, tree_grid.shape[0]-1), (1, -1)):
    for i in range(tree_grid.shape[1]):
        tree_height = -1
        current_index = start_index
        for _ in range(tree_grid.shape[0]):
            if tree_grid[current_index, i] > tree_height:
                visible[current_index, i] = True
                tree_height = tree_grid[current_index, i]
            current_index += increment

print(visible.sum())

scenic_scores = np.zeros_like(tree_grid)

for i in range(1, tree_grid.shape[0]-1):
    for j in range(1, tree_grid.shape[1]-1):
        scenic_score = 1
        # left
        viewing_dist = 1
        for diff in range(-1, -j, -1):
            if tree_grid[i, j] <= tree_grid[i, j + diff]:
                break
            viewing_dist += 1
        scenic_score *= viewing_dist

        # right
        viewing_dist = 1
        for diff in range(1, tree_grid.shape[1] - j - 1, 1):
            if tree_grid[i, j] <= tree_grid[i, j + diff]:
                break
            viewing_dist += 1
        scenic_score *= viewing_dist

        # down
        viewing_dist = 1
        for diff in range(-1, -i, -1):
            if tree_grid[i, j] <= tree_grid[i + diff, j]:
                break
            viewing_dist += 1
        scenic_score *= viewing_dist

        # up
        viewing_dist = 1
        for diff in range(1, tree_grid.shape[0] - i - 1, 1):
            if tree_grid[i, j] <= tree_grid[i + diff, j]:
                break
            viewing_dist += 1
        scenic_score *= viewing_dist

        scenic_scores[i, j] = scenic_score

print(scenic_scores.max())
