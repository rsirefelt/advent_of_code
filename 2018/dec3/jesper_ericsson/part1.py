import numpy as np
def main():
    fabric = np.zeros((1000,1000))

    # with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            input = string.rstrip().replace('#','').replace(' @ ',',').\
                replace(': ',',').replace('x',',').split(',')
            #print(input)
            id=int(input[0])
            start_col = int(input[1])
            start_row = int(input[2])
            width = int(input[3])
            length = int(input[4])
            
            fabric[start_row:start_row+length, start_col:start_col+width] += 1
            
        print(np.sum(fabric>1))

if __name__ == "__main__": main()
	