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
    
    for iRow in range(rowSize):
        for iCol in range(colSize):
            minDist = size[0] + size[1]
            coordLabel = 0
            for label, coord in enumerate(input):
                dist = calcDist((iCol, iRow), coord)
                if dist < minDist:
                    minDist = dist
                    coordLabel = label + 1
                elif dist == minDist:
                    coordLabel = 0
                
            map[iRow, iCol] = coordLabel
    
    maxArea = 0
    for label in range(1,len(input)+1):
        labelMap = map==label
        area = np.sum(labelMap)
        unlimit = np.sum(labelMap[0,:])
        unlimit += np.sum(labelMap[-1,:])
        unlimit += np.sum(labelMap[:,0])
        unlimit += np.sum(labelMap[:,-1])
        if area > maxArea and unlimit == 0:
            maxArea = area
    print(maxArea)


if __name__ == "__main__": main()
	
