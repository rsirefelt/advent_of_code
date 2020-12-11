import numpy as np
from copy import deepcopy

if __name__ == '__main__':

    f=open("Task11.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    theChairs = np.zeros((len(theInput),len(theInput[0])))
    newChairs = deepcopy(theChairs)

    oldOccupied = 1000

    noChair = 0
    freeChair = 1
    occupiedChair = 2

    stable = False

    for i in range(len(theInput)):
        for j in range(len(theInput[0])):
            if theInput[i][j] == ".":
                theChairs[i][j] = noChair
            elif theInput[i][j] == "L":
                theChairs[i][j] = freeChair
            elif theInput[i][j] == "#":
                theChairs[i][j] = occupiedChair

    directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    while stable == False:

        for i in range(len(theChairs)):
            for j in range(len(theChairs[i])):
                if theChairs[i][j] != noChair:

                    sumOccupied = 0

                    for k in directions:
                        
                        anyFound = False
                        sightLength = 1

                        while anyFound == False:

                            thisX = i+sightLength*k[0]
                            thisY = j+sightLength*k[1]

                            if thisX < 0 or thisY < 0:
                                break

                            elif thisX > len(theInput)-1 or thisY > len(theInput[0])-1:
                                break

                            thisSight = theChairs[thisX][thisY]
                            if thisSight == occupiedChair:
                                sumOccupied +=1
                                anyFound = True
                            elif thisSight == freeChair:
                                anyFound = True
                            else:
                                sightLength += 1

                    if theChairs[i][j] == freeChair:
                        if sumOccupied == 0:
                            newChairs[i][j] = occupiedChair
                    elif theChairs[i][j] == occupiedChair:
                        if sumOccupied >= 5:
                            newChairs[i][j] = freeChair

        newOccupied = np.count_nonzero(newChairs == occupiedChair)

        if oldOccupied == newOccupied:
            stable = True

        oldOccupied = newOccupied

        theChairs = deepcopy(newChairs)

    print("Done")
    print(oldOccupied)
