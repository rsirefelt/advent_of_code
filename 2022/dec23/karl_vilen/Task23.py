def checkIfTryMove(elfPosX, elfPosY, elfTiles):

    theString = str(elfPosX-1) + "," + str(elfPosY-1)
    if theString in elfTiles:
        return True
    theString = str(elfPosX) + "," + str(elfPosY-1)
    if theString in elfTiles:
        return True
    theString = str(elfPosX+1) + "," + str(elfPosY-1)
    if theString in elfTiles:
        return True
    theString = str(elfPosX-1) + "," + str(elfPosY)
    if theString in elfTiles:
        return True
    theString = str(elfPosX+1) + "," + str(elfPosY)
    if theString in elfTiles:
        return True
    theString = str(elfPosX-1) + "," + str(elfPosY+1)
    if theString in elfTiles:
        return True
    theString = str(elfPosX) + "," + str(elfPosY+1)
    if theString in elfTiles:
        return True
    theString = str(elfPosX+1) + "," + str(elfPosY+1)
    if theString in elfTiles:
        return True

    return False

def checkIfElf(elfPosX, elfPosY, theOrder, elfTiles):

    if theOrder == 1:
        thisString1 = str(elfPosX-1) + "," + str(elfPosY-1)
        thisString2 = str(elfPosX) + "," + str(elfPosY-1)
        thisString3 = str(elfPosX+1) + "," + str(elfPosY-1)
    elif theOrder == 2:
        thisString1 = str(elfPosX-1) + "," + str(elfPosY+1)
        thisString2 = str(elfPosX) + "," + str(elfPosY+1)
        thisString3 = str(elfPosX+1) + "," + str(elfPosY+1)
    elif theOrder == 3:
        thisString1 = str(elfPosX-1) + "," + str(elfPosY-1)
        thisString2 = str(elfPosX-1) + "," + str(elfPosY)
        thisString3 = str(elfPosX-1) + "," + str(elfPosY+1)
    elif theOrder == 4:
        thisString1 = str(elfPosX+1) + "," + str(elfPosY-1)
        thisString2 = str(elfPosX+1) + "," + str(elfPosY)
        thisString3 = str(elfPosX+1) + "," + str(elfPosY+1)

    if thisString1 in elfTiles or thisString2 in elfTiles or thisString3 in elfTiles:
        return True, "Nothing"
    else:
        return False, thisString2

if __name__ == '__main__':

    f=open("Task23.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    elves = dict()

    elfId = 0

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):

            if j == "#":

                elves[elfId] = [jIndex, iIndex, 1]
                elfId += 1

    for thisRound in range(0,50000):

        elvesNotMoved = 0

        contestedTiles = dict()
        tilesWithElves = dict()

        for theId, elfInfo in elves.items():
            thisString = str(elfInfo[0]) + "," + str(elfInfo[1])
            tilesWithElves[thisString] = 1

        for theId, elfInfo in elves.items():

            tryMove = checkIfTryMove(elfInfo[0], elfInfo[1], tilesWithElves.keys())
            if tryMove == False:
                elvesNotMoved += 1
                elves[theId][2] += 1
                if elves[theId][2] == 5:
                    elves[theId][2] = 1
                continue

            thisDir = elfInfo[2]

            for i in range (0,4):

                hasElf, gotoTile = checkIfElf(elfInfo[0], elfInfo[1], thisDir, tilesWithElves.keys())

                if hasElf == False:
                    if gotoTile not in contestedTiles.keys():
                        contestedTiles[gotoTile] = [1, theId]
                    else:
                        contestedTiles[gotoTile] = [2, -1]
                    break
                else:
                    thisDir += 1
                    if thisDir == 5:
                        thisDir = 1
                    continue

            elves[theId][2] += 1
            if elves[theId][2] == 5:
                elves[theId][2] = 1

        for gotoString, content in contestedTiles.items():

            if content[0] == 1:

                gotoInt = gotoString.split(",")
                gotoIntX = int(gotoInt[0])
                gotoIntY = int(gotoInt[1])

                elves[content[1]][0] = gotoIntX
                elves[content[1]][1] = gotoIntY

        if elvesNotMoved == len(elves.keys()):
            print("RoundNotMoved:", thisRound + 1)
            break


    minX = 50000
    minY = 50000
    maxX = -50000
    maxY = -50000

    for theKey, content in elves.items():

        thisX = content[0]
        thisY = content[1]

        minX = min(thisX, minX)
        minY = min(thisY, minY)
        maxX = max(thisX, maxX)
        maxY = max(thisY, maxY)

    area = ((maxX - minX) + 1) * ((maxY - minY) + 1)

    amountOfElves = len(elves.keys())

    print("Answer")
    print(area - amountOfElves)










