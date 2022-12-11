import os
import numpy as np

def read_data(filename):
    with open(filename, "r") as f:
        input_lines = f.readlines()
        heightmap = []

        for line in input_lines:
            heightmap.append([int(c) for c in line.rstrip()])

    return np.array(heightmap)


def is_visible(row_ind, col_ind, map):
    if all(map[row_ind, col_ind] > map[row_ind,:col_ind]):
        return True
    elif all(map[row_ind, col_ind] > map[row_ind,col_ind+1:]):
        return True
    elif all(map[row_ind, col_ind] > map[:row_ind,col_ind]):
        return True
    elif all(map[row_ind, col_ind] > map[row_ind+1:,col_ind]):
        return True


def prob1(map):
    rows, cols = np.shape(map)
    visible_trees = rows*cols - ((rows-2) * (cols-2))

    for row in range(1,rows-1):
        for col in range(1,cols-1):
            if is_visible(row,col,map):
                visible_trees += 1

    print(f"Number visible trees: {visible_trees}")

def get_scenic_score(row_ind, col_ind, map):

    def count_trees_in_direction(height, sub_map):
        seen_trees = 0
        for other in sub_map:
            seen_trees +=1
            if height <= other:
                break
        return seen_trees
    
    tree_height = map[row_ind, col_ind]
    scenic_score = 1
    
    scenic_score *= count_trees_in_direction(tree_height, map[row_ind,col_ind-1::-1])
    scenic_score *= count_trees_in_direction(tree_height, map[row_ind,col_ind+1:])
    scenic_score *= count_trees_in_direction(tree_height, map[row_ind-1::-1,col_ind])
    scenic_score *= count_trees_in_direction(tree_height, map[row_ind+1:,col_ind])

    return scenic_score


def prob2(map):
    rows, cols = np.shape(map)
    max_score = 0
    for row in range(1,rows-1):
        for col in range(1,cols-1):
            current_score =  get_scenic_score(row,col,map)
            if current_score > max_score:
                max_score = current_score
                

    print(f"Highest Scenic score: {max_score}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"
    map = read_data(filename)

    prob1(map)
    prob2(map)


if __name__ == "__main__":
    main()
