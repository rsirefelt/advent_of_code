import numpy as np

def checkGrid(theGrid):

    grid2d = np.array(theGrid)
    lastRow = 1
    nrOfColums = len(grid2d[0,:])
    nrOfRows = len(grid2d[:,0])
    allValues = []

    for i in range(nrOfRows):

        theRow = 0
        foundMirror = False
        thisRow = grid2d[i,:]

        if np.array_equal(thisRow, lastRow):
            theRow = i
            foundMirror = True
        else:
            lastRow = thisRow.copy()

        if foundMirror:
            for j in range(1, nrOfRows - i):

                row1 = grid2d[i + j,:]
                row2 = grid2d[i - j - 1,:]

                if (i - j - 1) < 0:
                    break

                if np.array_equal(row1, row2) == False:
                    foundMirror = False
                    break

        if foundMirror:
            allValues.append(theRow*100)
            foundMirror = False

    lastColumn = 1
    
    for i in range(nrOfColums):
        
        foundMirror = False
        theColumn = 0
        thisColumn = grid2d[:,i]

        if np.array_equal(thisColumn, lastColumn):
            theColumn = i
            foundMirror = True
        else:
            lastColumn = thisColumn.copy()

        if foundMirror:
            for j in range(1, nrOfColums - i):

                column1 = grid2d[:, i + j]
                column2 = grid2d[:, i - j - 1]

                if (i - j - 1) < 0:
                    break

                if np.array_equal(column1, column2) == False:
                    foundMirror = False
                    break

        if foundMirror:
            allValues.append(theColumn)
            foundMirror = False

    return allValues

if __name__ == '__main__':

    f=open("Task13.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("#","1")
        i = i.replace(".","0")
        i = list(i)
        for j in range(0, len(i)):
            i[j] = int(i[j])
        theInput.append(i)
    f.close()

    currentGrid = []

    allGrids = []

    for i in theInput:
        if len(i) == 0:
            allGrids.append(currentGrid)
            currentGrid = []
        else:
            currentGrid.append(i)
    allGrids.append(currentGrid)

    totalAnswer = 0
    totalAnswer2 = 0

    for thisGrid in allGrids:

        grid2d = np.array(thisGrid)
        thisValue = checkGrid(grid2d.copy())
        nrOfColums = len(grid2d[0,:])
        nrOfRows = len(grid2d[:,0])
        breakAll = False

        while True:

            for i in range(nrOfRows):
                for j in range(nrOfColums):

                    newGrid = grid2d.copy()
                    if newGrid[i,j] == 1:
                        newGrid[i,j] = 0
                    else:
                        newGrid[i,j] = 1

                    value2 = checkGrid(newGrid.copy())

                    if len(value2) > 0:

                        if len(value2) == 1:
                            if value2[0] != thisValue[0]:
                                breakAll = True
                                break
                        else:
                            value2.remove(thisValue[0])
                            breakAll = True
                            break

                if breakAll:
                    break

            if breakAll:
                break

        totalAnswer += sum(thisValue)
        totalAnswer2 += sum(value2)

    print(totalAnswer)
    print(totalAnswer2)