import numpy as np
import time

def read_start_plane(filename):
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        start_plane_list = []
        for string in data_lines:
            row = []
            for char in string.rstrip():
                if char == '#':
                    row.append(1)
                elif char == '.':
                    row.append(0)

            start_plane_list.append(row)

    return np.array(start_plane_list) 

def count_neighbours(space,hyper, layer, row, col, size):
    if 0 < hyper < size[0]-1:
        min_hyper = hyper-1
        max_hyper = hyper+2
    elif hyper == 0:
        min_hyper = hyper
        max_hyper = hyper+2
    elif hyper == size[0]-1:
        min_hyper = hyper-1
        max_hyper = hyper+1
    
    if 0 < layer < size[1]-1:
        min_layer = layer-1
        max_layer = layer+2
    elif layer == 0:
        min_layer = layer
        max_layer = layer+2
    elif layer == size[1]-1:
        min_layer = layer-1
        max_layer = layer+1

    if 0 < row < size[2]-1:
        min_row = row-1
        max_row = row+2
    elif row == 0:
        min_row = row
        max_row = row+2
    elif row == size[2]-1:
        min_row = row-1
        max_row = row+1

    if 0 < col < size[3]-1:
        min_col = col-1
        max_col = col+2
    elif col == 0:
        min_col = col
        max_col = col+2
    elif col == size[3]-1:
        min_col = col-1
        max_col = col+1

    num_neighbours = space[min_hyper:max_hyper, min_layer:max_layer,min_row:max_row,min_col:max_col].sum()
    num_neighbours -= space[hyper,layer,row,col]
      
    return(num_neighbours)

def update_space(space, layers, hyper_layers):
    size = space.shape

    new_space = space.copy()
    for hyper in range(hyper_layers[0], hyper_layers[1]):
        for layer in range(layers[0], layers[1]):
            for row in range(size[2]):
                for col in range(size[3]):
                    
                    if space[hyper,layer,row,col] == 0:
                        neighbours = count_neighbours(space, hyper,layer, row, col, size)
                        if neighbours == 3:
                            new_space[hyper,layer,row,col] = 1
                    elif space[hyper, layer, row,col] == 1:
                        neighbours = count_neighbours(space, hyper,layer, row, col, size)
                        if not (2 <= neighbours <= 3):
                            new_space[hyper,layer,row,col] = 0
          
    return new_space

def get_active_cubes(space, start_cycles,use_hyper):

    for i in range(1, start_cycles+1):
        layers_to_check = (start_cycles-i,start_cycles + i+1)
        if use_hyper:
            space = update_space(space, layers_to_check, layers_to_check)
        else:
            space = update_space(space, layers_to_check, (start_cycles, start_cycles+1))

    return space.sum()

def main():
    start_plane = read_start_plane('testdata.csv')
    start_plane = read_start_plane('data.csv')

    start_cycles = 6
    start_num_rows, start_num_cols = start_plane.shape
    num_rows = start_num_rows + start_cycles * 2
    num_cols = start_num_cols + start_cycles * 2
    num_layers = 1 + start_cycles * 2
    space = np.zeros((num_layers ,num_layers, num_rows, num_cols))
    space[start_cycles,start_cycles, start_cycles:start_cycles+start_num_rows, start_cycles:start_cycles+start_num_cols] = start_plane

    start = time.time()
    active_cubes = get_active_cubes(space, start_cycles, False)
    end = time.time()

    print('Part 1 time: %f' %(end - start))
    print('Number of active cubes: %i' %active_cubes)

    start = time.time()
    active_cubes = get_active_cubes(space, start_cycles, True)
    end = time.time()

    print('Part 2 time: %f' %(end - start))
    print('Number of active cubes: %i' %active_cubes)
if __name__ == "__main__": main()