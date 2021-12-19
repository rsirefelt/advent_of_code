import numpy as np
from utils import read_lines

def readMatrix(filename):
    """Read input matrix and pad it with -np.inf around the border."""
    lines = read_lines(filename)
    matrix = np.ones((len(lines)+2, len(lines[0])+2), dtype=int)*(np.inf)
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            matrix[row+1,col+1] = lines[row][col]
    return matrix

def solvePathOptimized(cost):
    lowest_cost_so_far = np.ones_like(cost, dtype=int)*np.inf
    size = lowest_cost_so_far.shape[0]
    lowest_cost_so_far[1, 1] = 0
    visited = np.ones_like(lowest_cost_so_far, dtype=bool)
    visited[1:size-1, 1:size-1] = False

    finished = False
    row = 1
    col = 1
    while not finished:
        # Update the tentative cost of its neighbours
        if cost[row - 1, col] < np.inf:
            lowest_cost_so_far[row-1,col] = min(lowest_cost_so_far[row-1,col], lowest_cost_so_far[row,col] + cost[row-1,col])
        if cost[row + 1, col] < np.inf:
            lowest_cost_so_far[row+1,col] = min(lowest_cost_so_far[row+1,col], lowest_cost_so_far[row,col] + cost[row+1,col])
        if cost[row, col - 1] < np.inf:
            lowest_cost_so_far[row,col-1] = min(lowest_cost_so_far[row,col-1], lowest_cost_so_far[row,col] + cost[row,col-1])
        if cost[row, col + 1] < np.inf:
            lowest_cost_so_far[row,col+1] = min(lowest_cost_so_far[row,col+1], lowest_cost_so_far[row,col] + cost[row,col+1])

        # Check if we are done
        if row == size-2 and col == size-2:
            finished = True

        # Find the unvisited node with the smallest tentative cost
        visited[row,col] = True
        tmp = np.copy(lowest_cost_so_far)
        tmp[visited] = np.inf
        curr_node = np.argmin(tmp)
        row = curr_node // size
        col = curr_node - row * size
        #print(row,col)

        #print(lowest_cost_so_far)

    return lowest_cost_so_far[size-2,size-2]

def solvePath(cost):
    lowest_cost_so_far = np.ones_like(cost, dtype=int)*np.inf
    size = lowest_cost_so_far.shape[0]
    lowest_cost_so_far[size-2, size-2] = 0

    for iter in range(size*5):
        any_change = False
        for row in range(size-2, 0, -1):
            for col in range(size-2, 0, -1):
                if row == size - 2 and col == size - 2:
                    continue
                cost1 = lowest_cost_so_far[row-1, col] + cost[row-1, col]
                cost2 = lowest_cost_so_far[row+1, col] + cost[row+1, col]
                cost3 = lowest_cost_so_far[row, col-1] + cost[row, col-1]
                cost4 = lowest_cost_so_far[row, col+1] + cost[row, col+1]
                new_cost = np.min([cost1, cost2, cost3, cost4])
                if new_cost < lowest_cost_so_far[row,col]:
                    lowest_cost_so_far[row,col] = new_cost
                    any_change = True
        if not any_change:
            break
    return lowest_cost_so_far[1,1]

# Part 1
cost = readMatrix("/home/carl/Code/AdventOfCode/Day15/input.txt")
size = cost.shape[0]-2
print("Part 1:", solvePathOptimized(cost))

# Part 2. Construct the new cost matrix
new_size = 5*(cost.shape[0]-2)+2
cost_part_2 = np.ones((new_size, new_size))*np.inf
#cost_inside = cost[1:size+1, 1:size+1]
for row in range(5):
    row_idx = 1 + size*row
    cost_inside = np.copy(cost[1:size + 1, 1:size + 1])
    for kk in range(row):
        cost_inside = cost_inside + 1
        cost_inside[cost_inside == 10] = 1
    for col in range(5):
        col_idx = 1 + size*col
        cost_part_2[row_idx:row_idx+size, col_idx:col_idx+size] = np.copy(cost_inside)
        cost_inside = cost_inside + 1
        cost_inside[cost_inside == 10] = 1

print("Part 2:", solvePathOptimized(cost_part_2))