import numpy as np

def main():
    ids = set()
    size = (1000,1000)
    fabric = np.zeros(size)
    fabric_ids = np.zeros(size)
    
    fabric_overlap = np.zeros(size)
    # with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            input = string.rstrip().replace('#','').replace(' @ ',',').\
                replace(': ',',').replace('x',',').split(',')
            # print(input)
            id=int(input[0])
            start_col = int(input[1])
            start_row = int(input[2])
            width = int(input[3])
            length = int(input[4])
            
            remove_me = False
            for row in range(start_row,start_row+length):
                for col in range(start_col,start_col+width):
                    if fabric[row,col]==0:
                        fabric[row,col] += 1
                        fabric_ids[row,col] = id
                        if id not in ids:
                            ids.add(id)
                    else:
                        fabric[row,col] += 1
                        block_id = fabric_ids[row,col]
                        ids.discard(block_id)
                        remove_me = True
            
            if remove_me:
                ids.discard(id)
  
        print(ids)    

if __name__ == "__main__": main()
	