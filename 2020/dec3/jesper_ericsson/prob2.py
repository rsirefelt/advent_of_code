def read_map(filename):
    input_data = []
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            input_data.append(string.rstrip())
    return input_data

def evaluate_slope(input_map, num_cols, num_rows,col_step, row_step):
    current_col = 0
    trees = 0
    free = 0

    for row_ind in range(0,num_rows, row_step):
        row = input_map[row_ind]
        if row[current_col] == '#':
            trees += 1
        else:
            free += 1
        
        current_col = (current_col + col_step)%num_cols
    print (['Trees: ', trees])
    print (['Free space: ', free])
    return trees

def main():
    # input_map = read_map('testdata.csv')
    input_map = read_map('data.csv')
    input_cols = len(input_map[0])
    input_rows = len(input_map)
    print(input_cols,input_rows)

    product = 1
    product *= evaluate_slope(input_map, input_cols, input_rows,1, 1)
    product *= evaluate_slope(input_map, input_cols, input_rows,3, 1)
    product *= evaluate_slope(input_map, input_cols, input_rows,5, 1)
    product *= evaluate_slope(input_map, input_cols, input_rows,7, 1)
    product *= evaluate_slope(input_map, input_cols, input_rows,1, 2)

    print(['Product: ', product])

if __name__ == "__main__": main()