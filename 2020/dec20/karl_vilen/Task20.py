import numpy as np
from copy import deepcopy
import math

if __name__ == '__main__':

    f=open("Task20.txt","r")
    lines=f.readlines()
    theInput = []

    allTiles = dict()

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    for i in theInput:

        if "Tile" in i:
            a = i
            a = a.replace("Tile ","")
            a = a.replace(":","")
            thisTile = int(a)
            yCoord = 0
            thisGrid = np.zeros((10,10))
            continue
        elif i == "":
            allTiles[thisTile] = (thisGrid)
            continue
        else:
            xCoord = 0
            for j in i:
                if j == "#":
                    thisGrid[xCoord][yCoord] = 1
                xCoord += 1

            yCoord += 1

    borderFits = dict()
    borders = dict()
    rotations = dict()
    for key, value in allTiles.items():
        emptyList = []
        borderFits[key] = deepcopy(emptyList)
        borders[key] = deepcopy(emptyList)
        rotations[key] = deepcopy(emptyList)

    for key, value in allTiles.items():
        a = deepcopy(value)

        thisBorders = []
        thisBorders.append(a[:,0])
        thisBorders.append(a[:,9])
        thisBorders.append(a[0,:])
        thisBorders.append(a[9,:])
        a = np.flip(a)
        thisBorders.append(a[:,0])
        thisBorders.append(a[:,9])
        thisBorders.append(a[0,:])
        thisBorders.append(a[9,:])

        for i in range(8):

            if len(borderFits[key]) == 4:
                break
            thisBorder = thisBorders[i]

            for key2, value2 in allTiles.items():
                b = deepcopy(value2)

                thatBorders = []
                thatBorders.append(b[:,0])
                thatBorders.append(b[:,9])
                thatBorders.append(b[0,:])
                thatBorders.append(b[9,:])
                b = np.flip(b)
                thatBorders.append(b[:,0])
                thatBorders.append(b[:,9])
                thatBorders.append(b[0,:])
                thatBorders.append(b[9,:])

                if len(borderFits[key2]) == 4:
                    continue
                elif key == key2:
                    continue
                else:
                    
                    for j in range(8):

                        thatBorder = thatBorders[j]

                        similar = True

                        for k in range(10):
                            if thisBorder[k] != thatBorder[k]:
                                similar = False
                                break

                        if similar == True:
                            if key2 not in borderFits[key]:
                                borderFits[key].append(key2)
                                borderFits[key2].append(key)
                                borders[key].append(thisBorder)
                                borders[key2].append(thatBorder)
                                rotations[key].append(i)
                                rotations[key2].append(j)
                            break

    theAnswer = 1

    for key, value in borderFits.items():

        if len(value) == 2:
            theAnswer *= key

    print("Done1")
    print(theAnswer)

    aBuffer = deepcopy(allTiles)
    newTiles = dict()

    for key, value in aBuffer.items():
        newTiles[key] = value[1:-1, 1:-1]

    for key, value in borderFits.items():
        if len(value) == 2:
            startTile = key
            break

    gridSize = math.sqrt(len(allTiles))
    gridSize = round(gridSize)

    tileGrid = np.zeros((gridSize,gridSize))

    
    tileGrid[0][0] = startTile

    thisTile = startTile
    requiredNewNeighbours = 3
    foundTiles = []
    foundTiles.append(thisTile)

    nextTile = [1,0]

    for i in range(gridSize-1):
        for j in range(1):

            requiredNewNeighbours = 3

            if i == gridSize - 2:
                requiredNewNeighbours = 2

            candidates = borderFits[thisTile]

            for k in candidates:
                if len(borderFits[k]) == requiredNewNeighbours and k not in foundTiles:
                    foundTiles.append(k)
                    tileGrid[nextTile[0]][nextTile[1]] = k
                    thisTile = k
                    nextTile[0] += 1
                    break

    nextTile = [0,1]
    thisTile = startTile
    
    for i in range(1):
        for j in range(gridSize-1):

            requiredNewNeighbours = 3

            if j == gridSize - 2:
                requiredNewNeighbours = 2

            candidates = borderFits[thisTile]

            for k in candidates:
                if len(borderFits[k]) == requiredNewNeighbours and k not in foundTiles:
                    foundTiles.append(k)
                    tileGrid[nextTile[0]][nextTile[1]] = k
                    thisTile = k
                    nextTile[1] += 1
                    break

    for i in range(1,gridSize):
        for j in range(1,gridSize):

            firstKeys = borderFits[tileGrid[i-1][j]]
            secondKeys = borderFits[tileGrid[i][j-1]]

            for k in firstKeys:
                if k in secondKeys and k not in foundTiles:
                    tileGrid[i][j] = k
                    foundTiles.append(k)

    firstTile = tileGrid[0][0]
    secondTile = tileGrid[1][0]

    thisTile = allTiles[firstTile]
    thatTile = allTiles[secondTile]

    for i in range(8):
        for j in range(8):

            thisBorder = thisTile[9,:]
            thatBorder = thatTile[0,:]

            correctBorder = True

            for k in range(10):
                if thisBorder[k] != thatBorder[k]:
                    correctBorder = False
                    break

            if correctBorder:
                break
            else:
                if j != 3:
                    thatTile = np.rot90(thatTile)
                else:
                    thatTile = np.fliplr(thatTile)

        if correctBorder:
            reqRots = i
        else:
            if i != 3:
                thisTile = np.rot90(thisTile)
            else:
                thisTile = np.fliplr(thisTile)

    fixedTiles = deepcopy(allTiles)

    for i in range(reqRots):
        if i != 3:
            fixedTiles[firstTile] = np.rot90(fixedTiles[firstTile])
        else:
            fixedTiles[firstTile] = np.fliplr(fixedTiles[firstTile])

    for k in range(1,gridSize):

        beginTile = tileGrid[k-1][0]
        endTile = tileGrid[k][0]

        thisTile = fixedTiles[beginTile]
        thatTile = fixedTiles[endTile]

        thisBorder = thisTile[9,:]

        thisRotation = 0

        for i in range(8):

            thatBorder = thatTile[0,:]

            correctBorder = True

            for j in range(10):
                if thisBorder[j] != thatBorder[j]:
                    correctBorder = False
                    break

            if correctBorder:
                break
            else:
                if i != 3:
                    thatTile = np.rot90(thatTile)
                else:
                    thatTile = np.fliplr(thatTile)

                thisRotation += 1


        for i in range(thisRotation):
            if i != 3:
                fixedTiles[endTile] = np.rot90(fixedTiles[endTile])
            else:
                fixedTiles[endTile] = np.fliplr(fixedTiles[endTile])


    for k in range(0,gridSize):
        for l in range(1,gridSize):

            beginTile = tileGrid[k][l-1]
            endTile = tileGrid[k][l]

            thisTile = fixedTiles[beginTile]
            thatTile = fixedTiles[endTile]

            thisBorder = thisTile[:,9]

            thisRotation = 0

            for i in range(8):

                thatBorder = thatTile[:,0]

                correctBorder = True

                for j in range(10):
                    if thisBorder[j] != thatBorder[j]:
                        correctBorder = False
                        break

                if correctBorder:
                    break
                else:
                    if i != 3:
                        thatTile = np.rot90(thatTile)
                    else:
                        thatTile = np.fliplr(thatTile)

                    thisRotation += 1


            for i in range(thisRotation):
                if i != 3:
                    fixedTiles[endTile] = np.rot90(fixedTiles[endTile])
                else:
                    fixedTiles[endTile] = np.fliplr(fixedTiles[endTile])

    fixedPictures = deepcopy(fixedTiles)

    totalPicture = np.zeros((gridSize*8,gridSize*8))

    for i in range(gridSize):
        for j in range(gridSize):

            thisKey = tileGrid[i][j]

            a = fixedPictures[thisKey][1:-1, 1:-1]

            for k in range(8):
                for l in range(8):
                    totalPicture[i*8+k][j*8+l] = a[k][l]

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

    monster = [[0,18],[1,0],[1,5],[1,6],[1,11],[1,12],[1,17],[1,18],[1,19],[2,1],[2,4],[2,7],[2,10],[2,13],[2,16]]

    totalMonsters = 0

    for w in range(8):

        for i in range(len(totalPicture)-19):
            for j in range(len(totalPicture)-2):

                monsterFound = True

                for k in monster:
                    if totalPicture[i+k[1]][j+k[0]] == 0:
                        monsterFound = False

                if monsterFound == True:
                    totalMonsters += 1

                    for k in monster:
                        totalPicture[i+k[1]][j+k[0]] = 0

        if w != 3:
            totalPicture = np.rot90(totalPicture)
        else:
            totalPicture = np.fliplr(totalPicture)



    print("Done2")
    print(totalMonsters)
    print(sum(sum(totalPicture)))
