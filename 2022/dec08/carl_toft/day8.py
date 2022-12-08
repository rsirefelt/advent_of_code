import numpy as np

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    lines = lines[:-1]
    forest = []
    for line in lines:
        tree_row = [int(char) for char in line]
        forest.append(tree_row)
    forest = np.array(forest)

    return forest

forest = parseInput("input.txt")
forest_int = forest[1:-1, 1:-1]

left = np.column_stack([np.max(forest[1:-1,:k], axis=1) for k in range(1,forest.shape[1]-1)])
right = np.column_stack([np.max(forest[1:-1,(k+1):], axis=1) for k in range(1,forest.shape[1]-1)])
top = np.vstack([np.max(forest[:k,1:-1], axis=0) for k in range(1,forest.shape[0]-1)])
bottom = np.vstack([np.max(forest[(k+1):,1:-1], axis=0) for k in range(1,forest.shape[0]-1)])

is_visible = np.logical_or(forest_int > left, forest_int > right)
is_visible = np.logical_or(is_visible, forest_int > top)
is_visible = np.logical_or(is_visible, forest_int > bottom)

num_visible = np.sum(is_visible) + 2*forest.shape[0] + 2*(forest.shape[1]-2)

print("Part 1: " + str(num_visible))

# Part 2
best_scenic_score = 0
for row in range(1, forest.shape[0-1]):
    for col in range(1, forest.shape[0 - 1]):
        num_visible_trees = []
        curr_score = 0
        for delta_x in range(1, forest.shape[1]):
            if col+delta_x >= forest.shape[1]:
                break
            curr_score = curr_score + 1
            if forest[row, col + delta_x] >= forest[row,col]:
                break
        num_visible_trees.append(curr_score)

        curr_score = 0
        for delta_x in range(1, forest.shape[1]):
            if col - delta_x < 0:
                break
            curr_score = curr_score + 1
            if forest[row, col - delta_x] >= forest[row, col]:
                break
        num_visible_trees.append(curr_score)

        curr_score = 0
        for delta_y in range(1, forest.shape[0]):
            if row + delta_y >= forest.shape[0]:
                break
            curr_score = curr_score + 1
            if forest[row + delta_y, col] >= forest[row, col]:
                break
        num_visible_trees.append(curr_score)

        curr_score = 0
        for delta_y in range(1, forest.shape[0]):
            if row - delta_y < 0:
                break
            curr_score = curr_score + 1
            if forest[row - delta_y, col] >= forest[row, col]:
                break
        num_visible_trees.append(curr_score)

        num_visible_trees = np.array(num_visible_trees)
        scenic_score = np.prod(num_visible_trees)
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score


print("Part 2: " + str(best_scenic_score))