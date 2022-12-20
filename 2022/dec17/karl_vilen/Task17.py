import numpy as np
import time

if __name__ == '__main__':

    f=open("Task17.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()

        theInput.append(i)
    f.close()

    numOfRocks = 1010
    
    theGrid = np.zeros((7, numOfRocks * 4))


    numOfRockTypes = 5

    #print(theGrid)

    highestPoint = -1

    jetPosition = 0

    gustLength = len(theInput[0])

    for i in range(1,numOfRocks+1):

        #print("jetPosition:", jetPosition)
        #time.sleep(0.01)

        if i == 1760:
            print("StartHeight:")
            print(i)
            print(highestPoint)

        if i == 1760+995:
            print("Height at 1760+995:")
            print(i)
            print(highestPoint)


        if jetPosition == 2:
            if i % numOfRockTypes == 0:
                print("i:", i)
                print("highestPoint:",highestPoint)

        if i % numOfRockTypes == 1:

            rockPos1 = [2,highestPoint + 4]
            rockPos2 = [3,highestPoint + 4]
            rockPos3 = [4,highestPoint + 4]
            rockPos4 = [5,highestPoint + 4]

            rockPositions = [rockPos1,rockPos2,rockPos3,rockPos4]
        elif i % numOfRockTypes == 2:

            rockPos1 = [3,highestPoint + 4]
            rockPos2 = [2,highestPoint + 5]
            rockPos3 = [3,highestPoint + 5]
            rockPos4 = [4,highestPoint + 5]
            rockPos5 = [3,highestPoint + 6]

            rockPositions = [rockPos1,rockPos2,rockPos3,rockPos4, rockPos5]
        elif i % numOfRockTypes == 3:

            rockPos1 = [2,highestPoint + 4]
            rockPos2 = [3,highestPoint + 4]
            rockPos3 = [4,highestPoint + 4]
            rockPos4 = [4,highestPoint + 5]
            rockPos5 = [4,highestPoint + 6]

            rockPositions = [rockPos1,rockPos2,rockPos3,rockPos4, rockPos5]
        elif i % numOfRockTypes == 4:

            rockPos1 = [2,highestPoint + 4]
            rockPos2 = [2,highestPoint + 5]
            rockPos3 = [2,highestPoint + 6]
            rockPos4 = [2,highestPoint + 7]

            rockPositions = [rockPos1,rockPos2,rockPos3,rockPos4]
        elif i % numOfRockTypes == 0:

            rockPos1 = [2,highestPoint + 4]
            rockPos2 = [3,highestPoint + 4]
            rockPos3 = [2,highestPoint + 5]
            rockPos4 = [3,highestPoint + 5]

            rockPositions = [rockPos1,rockPos2,rockPos3,rockPos4]

        #print(rockPositions)

        #print("rockPositions1:",rockPositions)
        #print("jetPosition1:", jetPosition)
        #print("theInput[jetPosition]:", theInput[0][jetPosition])

        if theInput[0][jetPosition] == "<":
            doPush = True
            for i in rockPositions:
                if i[0] - 1 < 0:
                    doPush = False
                    break
                elif theGrid[i[0]-1][i[1]] == 1:
                    doPush = False
                    break
            if doPush == True:
                newPositions = []
                for j in rockPositions:
                    newPositions.append([j[0]-1,j[1]])
                rockPositions = newPositions.copy()
        elif theInput[0][jetPosition] == ">":
            doPush = True
            for i in rockPositions:
                if i[0] + 1 > 6:
                    doPush = False
                    break
                elif theGrid[i[0]+1][i[1]] == 1:
                    doPush = False
                    break
            if doPush == True:
                newPositions = []
                for j in rockPositions:
                    newPositions.append([j[0]+1,j[1]])
                rockPositions = newPositions.copy()

        jetPosition += 1
        jetPosition = jetPosition % gustLength

        toContinue = True
        while toContinue == True:

            for j in rockPositions:

                if j[1] == 0:
                    toContinue = False
                    break
                elif theGrid[j[0]][j[1] - 1] == 1:
                    toContinue = False
                    break

            if toContinue == False:
                for j in rockPositions:
                    theGrid[j[0]][j[1]] = 1
                    highestPoint = max(highestPoint, j[1])
            else:
                newPositions = []
                for j in rockPositions:
                    newPositions.append([j[0],j[1]-1])

                rockPositions = newPositions.copy()

                #print("rockPositions2:",rockPositions)
                #print("jetPosition2:", jetPosition)
                #print("theInput[jetPosition]:", theInput[0][jetPosition])
                if theInput[0][jetPosition] == "<":
                    doPush = True
                    for i in rockPositions:
                        if i[0] - 1 < 0:
                            doPush = False
                            break
                        elif theGrid[i[0]-1][i[1]] == 1:
                            doPush = False
                            break
                    if doPush == True:
                        newPositions = []
                        for j in rockPositions:
                            newPositions.append([j[0]-1,j[1]])
                        rockPositions = newPositions.copy()
                elif theInput[0][jetPosition] == ">":
                    doPush = True
                    for i in rockPositions:
                        if i[0] + 1 > 6:
                            doPush = False
                            break
                        elif theGrid[i[0]+1][i[1]] == 1:
                            doPush = False
                            break
                    if doPush == True:
                        newPositions = []
                        for j in rockPositions:
                            newPositions.append([j[0]+1,j[1]])
                        rockPositions = newPositions.copy()

                jetPosition += 1
                jetPosition = jetPosition % gustLength

        #print(theGrid)
        #print("highestPoint:",highestPoint)
        #print(np.rot90(theGrid))
    print("Answer")
    print(np.count_nonzero(theGrid))
    print(highestPoint+1)

    #And then some manual math
