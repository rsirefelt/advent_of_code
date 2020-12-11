import numpy as np
import time

floor_value = 100000
directions = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1) ]
def read_layout(filename):
    rules = {}

    with open(filename, 'r') as f:
        data_lines = f.readlines()
        layout_list = []
        for string in data_lines:
            row = []
            for char in string.rstrip():
                if char == 'L':
                    row.append(0)
                elif char == '.':
                    row.append(floor_value)

            layout_list.append(row)

        layout = np.array(layout_list)

    return layout

def count_neighbours(layout, row, col, size):
    if 0 < row < size[0]-1:
        min_row = row-1
        max_row = row+2
    elif row == 0:
        min_row = row
        max_row = row+2
    elif row == size[0]-1:
        min_row = row-1
        max_row = row+1

    if 0 < col < size[1]-1:
        min_col = col-1
        max_col = col+2
    elif col == 0:
        min_col = col
        max_col = col+2
    elif col == size[1]-1:
        min_col = col-1
        max_col = col+1

    num_neighbours = layout[min_row:max_row,min_col:max_col].sum()
    num_neighbours -= layout[row,col]
    num_neighbours = num_neighbours % floor_value
      
    return(num_neighbours)

def count_seen_occupied(layout, row, col, size):
    occupied = 0
    for direction in directions:
        tile_to_check = np.array([row,col])
        # print(tile_to_check)
        check_next = True
        while check_next:
            tile_to_check += direction
            if 0 <= tile_to_check[0] < size[0] and 0 <= tile_to_check[1] < size[1]:
                # print(tile_to_check)
                # print(layout[tile_to_check[0], tile_to_check[1]])
                if layout[tile_to_check[0], tile_to_check[1]] == 1:
                    occupied += 1
                    # print('oc')
                    check_next = False
                    break
                elif layout[tile_to_check[0], tile_to_check[1]] == 0:
                    check_next = False
                    break
            else:
                break

    return occupied


def update_layout(layout):
    size = layout.shape

    new_layout = layout.copy()
    for row in range(size[0]):
        for col in range(size[1]):
            
            if layout[row,col] == 0:
                neighbours = count_neighbours(layout, row, col, size)
                if neighbours == 0:
                    new_layout[row,col] = 1
            elif layout[row,col] == 1:
                neighbours = count_neighbours(layout, row, col, size)
                if neighbours >= 4:
                    new_layout[row,col] = 0
          
    return new_layout
    
def update_layout2(layout):
    size = layout.shape

    new_layout = layout.copy()
    for row in range(size[0]):
        for col in range(size[1]):
            if layout[row,col] == 0:
                neighbours = count_seen_occupied(layout, row, col, size)
                if neighbours == 0:
                    new_layout[row,col] = 1
            elif layout[row,col] == 1:
                neighbours = count_seen_occupied(layout, row, col, size)
                if neighbours >= 5:
                    new_layout[row,col] = 0
          
    return new_layout

def get_occupied_sets_part1(layout):
    occupied_sets = 0
    while True:
        new_layout = update_layout(layout)

        if (new_layout == layout).all():
            occupied_sets = layout.sum() % floor_value
            break
        else:
            layout = new_layout
    return occupied_sets

def get_occupied_sets_part2(layout):
    occupied_sets = 0
    while True:
        new_layout = update_layout2(layout)
        # print(layout)
        # print()
        if (new_layout == layout).all():
            occupied_sets = layout.sum() % floor_value
            break
        else:
            layout = new_layout
    return occupied_sets

def main():
    layout = read_layout('testdata.csv')
    layout = read_layout('data.csv')
    
    start = time.time()
    occupied_sets = get_occupied_sets_part1(layout)
    end = time.time()
    print(['Part 1 time: ', end - start])
    print('Number of occupied sets part 1: %i' %occupied_sets)

    start = time.time()
    occupied_sets = get_occupied_sets_part2(layout)
    end = time.time()
    print(['Part 1 time: ', end - start])
    print('Number of occupied sets part 2: %i' %occupied_sets)
if __name__ == "__main__": main()