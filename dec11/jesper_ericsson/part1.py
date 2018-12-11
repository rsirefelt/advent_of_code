import numpy as np

def createMatrix(size, serialNumber):
    fuelCells = np.zeros(size)
    it = np.nditer(fuelCells, flags=['multi_index'],  op_flags=['readwrite'])
    while not it.finished:
        # print("%d <%s>" % (it[0], it.multi_index))
        rackId = it.multi_index[0] + 11
        powerLevel = rackId * (it.multi_index[1] + 1) + serialNumber
        powerLevel *= rackId

        it[0] = int(powerLevel/100) % 10 - 5
        # print()
        it.iternext()
    return fuelCells

def calcSums(fuelCells, size):
    maxSum = 0
    for iCol in range(size[0]-2):
        for iRow in range(size[1]-2):
            # print(np.sum(fuelCells[iCol:iCol+2, iRow:iRow+2]))
            sum = np.sum(fuelCells[iCol:iCol+3, iRow:iRow+3])
            if sum > maxSum:
                maxSum = sum
                index = (iCol+1, iRow+1)
    print(maxSum)
    print(index)


def main():
    serialNumber = 9435
    size = (300,300)
    fuelCells = createMatrix(size, serialNumber)
    calcSums(fuelCells, size)

if __name__ == "__main__": main()
	
