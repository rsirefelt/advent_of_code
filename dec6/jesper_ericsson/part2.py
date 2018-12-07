import numpy as np

def calcDist(point1, point2):
    return abs(point2[0]-point1[0]) + abs(point2[1]-point1[1]) 

def main():
    # input = np.genfromtxt('testdata.csv', delimiter=',')
    input = np.genfromtxt('input.txt', delimiter=',')

    size = np.max(input, axis=0)
    rowSize = int(size[1]) + 1
    colSize = int(size[0]) + 1
    map = np.zeros((rowSize, colSize))
    allowedDist = 10000
    
    for iRow in range(rowSize):
        for iCol in range(colSize):
            dist =0
            for coord in input:
                dist += calcDist((iCol, iRow), coord)
                
            map[iRow, iCol] = dist < allowedDist

    area = np.sum(map)

    print(area)


if __name__ == "__main__": main()
	
