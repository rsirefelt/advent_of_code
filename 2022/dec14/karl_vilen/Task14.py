import numpy as np

if __name__ == '__main__':

    f=open("Task14.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.split(" -> ")
        theInput.append(i)
    f.close()

    theGrid = np.zeros((1000,1000))
    lowestGridY = -1
    
    for i in theInput:
        for j in i:
            newCoords = j.split(",")
            newCoords2 = [int(newCoords[0]),int(newCoords[1])]
            lowestGridY = max(lowestGridY, newCoords2[1])

    newString = ["0,"+str(lowestGridY + 2), "999,"+str(lowestGridY + 2)]
    theInput.append(newString)

    for i in theInput:
        
        oldCoords = [0,0]

        for j in i:

            if oldCoords == [0,0]:
                coords = j.split(",")
                oldCoords = [int(coords[0]),int(coords[1])]
                continue

            newCoords = j.split(",")
            newCoords2 = [int(newCoords[0]),int(newCoords[1])]

            if oldCoords[1] < newCoords2[1]:
                for k in range(oldCoords[1], newCoords2[1]+1):
                    theGrid[oldCoords[0]][k] = 1
            elif oldCoords[1] > newCoords2[1]:
                for k in range(newCoords2[1], oldCoords[1]+1):
                    theGrid[oldCoords[0]][k] = 1

            if oldCoords[0] < newCoords2[0]:
                for k in range(oldCoords[0], newCoords2[0]+1):
                    theGrid[k][oldCoords[1]] = 1
            elif oldCoords[0] > newCoords2[0]:
                for k in range(newCoords2[0], oldCoords[0]+1):
                    theGrid[k][oldCoords[1]] = 1

            oldCoords = newCoords2.copy()

    stopDrop = False
    startDropPos = [500,0]
    thisDropPos = startDropPos.copy()
    answer1 = 0

    if theGrid[500,0] == 2:
        stopDrop = True

    while stopDrop == False:

        newDropPosDown = [thisDropPos[0],thisDropPos[1]+1]
        newDropPosLeft = [thisDropPos[0]-1,thisDropPos[1]+1]
        newDropPosRight = [thisDropPos[0]+1,thisDropPos[1]+1]

        if thisDropPos[1]+1 > lowestGridY:
            if answer1 == 0:
                answer1 = np.count_nonzero(theGrid==2)

        if theGrid[500,0] == 2:
            break

        if theGrid[newDropPosDown[0],newDropPosDown[1]] == 0:
            thisDropPos = newDropPosDown.copy()
        elif theGrid[newDropPosLeft[0],newDropPosLeft[1]] == 0:
            thisDropPos = newDropPosLeft.copy()
        elif theGrid[newDropPosRight[0],newDropPosRight[1]] == 0:
            thisDropPos = newDropPosRight.copy()
        else:
            theGrid[thisDropPos[0],thisDropPos[1]] = 2
            thisDropPos = startDropPos.copy()

    print("Answer 1")
    print(answer1)

    print("Answer 2")
    print(np.count_nonzero(theGrid==2))
