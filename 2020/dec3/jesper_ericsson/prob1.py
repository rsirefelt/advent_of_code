def main():
    input_data = []
    # with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            input_data.append(string.rstrip())

    # print(input_data)
    input_cols = len(input_data[0])
    input_rows = len(input_data)
    print(input_cols,input_rows)
    current_col = 0
    trees = 0
    free = 0
    col_step = 3
    for row in input_data:
        if row[current_col] == '#':
            trees += 1
        else:
            free += 1
        
        current_col = (current_col + col_step)%input_cols
    print (['Trees: ', trees])
    print (['Free space: ', free])

            

if __name__ == "__main__": main()
	