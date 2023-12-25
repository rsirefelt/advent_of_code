import numpy as np

def tiltNorth(inputGrid):

    height = len(inputGrid)
    width = len(inputGrid[0])

    for x in range(width):
        lastOpenSpaceY = -1
        previousY = -1
        for y in range(height):

            if inputGrid[y,x] == 0 and previousY in [-1, 1,2]:
                lastOpenSpaceY = y

            if inputGrid[y,x] == 2:
                lastOpenSpaceY = -1

            if inputGrid[y,x] == 1 and lastOpenSpaceY != -1:
                inputGrid[y, x] = 0
                inputGrid[lastOpenSpaceY, x] = 1
                lastOpenSpaceY = lastOpenSpaceY + 1

            previousY = inputGrid[y,x]

    return inputGrid

def tiltSouth(inputGrid):

    height = len(inputGrid)
    width = len(inputGrid[0])

    for x in range(width):
        lastOpenSpaceY = -1
        previousY = -1
        for y in range(height-1,-1,-1):

            if inputGrid[y,x] == 0 and previousY in [-1, 1,2]:
                lastOpenSpaceY = y

            if inputGrid[y,x] == 2:
                lastOpenSpaceY = -1

            if inputGrid[y,x] == 1 and lastOpenSpaceY != -1:
                inputGrid[y, x] = 0
                inputGrid[lastOpenSpaceY, x] = 1
                lastOpenSpaceY = lastOpenSpaceY - 1

            previousY = inputGrid[y,x]

    return inputGrid

def tiltWest(inputGrid):

    height = len(inputGrid)
    width = len(inputGrid[0])

    for y in range(height):
        lastOpenSpaceX = -1
        previousX = -1
        for x in range(width):

            if inputGrid[y,x] == 0 and previousX in [-1, 1,2]:
                lastOpenSpaceX = x

            if inputGrid[y,x] == 2:
                lastOpenSpaceX = -1

            if inputGrid[y,x] == 1 and lastOpenSpaceX != -1:
                inputGrid[y, x] = 0
                inputGrid[y, lastOpenSpaceX] = 1
                lastOpenSpaceX = lastOpenSpaceX + 1

            previousX = inputGrid[y,x]

    return inputGrid

def tiltEast(inputGrid):

    height = len(inputGrid)
    width = len(inputGrid[0])

    for y in range(height):
        lastOpenSpaceX = -1
        previousX = -1
        for x in range(width-1,-1,-1):

            if inputGrid[y,x] == 0 and previousX in [-1, 1,2]:
                lastOpenSpaceX = x

            if inputGrid[y,x] == 2:
                lastOpenSpaceX = -1

            if inputGrid[y,x] == 1 and lastOpenSpaceX != -1:
                inputGrid[y, x] = 0
                inputGrid[y, lastOpenSpaceX] = 1
                lastOpenSpaceX = lastOpenSpaceX - 1

            previousX = inputGrid[y,x]

    return inputGrid

if __name__ == '__main__':

    f=open("Task14.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("#","2")
        i = i.replace("O","1")
        i = i.replace(".","0")
        i = list(i)
        for j in range(0, len(i)):
            i[j] = int(i[j])
        theInput.append(i)
    f.close()

    theGrid = np.array(theInput)

    height = len(theGrid)
    width = len(theGrid[0])

    equalSum = height * width
    allConfigurations = []
    totalRotations = 1000000000

    for rotations in range(totalRotations):

        theGrid = tiltNorth(theGrid)
        theGrid = tiltWest(theGrid)
        theGrid = tiltSouth(theGrid)
        theGrid = tiltEast(theGrid)

        anyFound = False
        for iIndex, i in enumerate(allConfigurations):

            thisSum = sum(sum(np.equal(i, theGrid)))

            if thisSum == equalSum:
                anyFound = True
                break

        if anyFound == False:
            allConfigurations.append(theGrid.copy())
        else:
            break

    moreRotations = (totalRotations - (rotations+1)) % (rotations - iIndex)

    aNewGrid = allConfigurations[iIndex + moreRotations]

    totalSum = 0
    for i in range(height):

        totalSum += sum(aNewGrid[i,:] == 1) * (height - i)

    print(totalSum)


