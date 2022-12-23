import numpy as np

def doShift(inD, inCubeSide):

    if inCubeSide == 1:
        if inD == 1:
            return False
        if inD == 2:
            return False
        if inD == 3:
            return True
        if inD == 4:
            return False

    if inCubeSide == 2:
        if inD == 1:
            return True
        if inD == 2:
            return False
        if inD == 3:
            return False
        if inD == 4:
            return False

    if inCubeSide == 3:
        if inD == 1:
            return False
        if inD == 2:
            return False
        if inD == 3:
            return False
        if inD == 4:
            return False

    if inCubeSide == 4:
        if inD == 1:
            return False
        if inD == 2:
            return False
        if inD == 3:
            return True
        if inD == 4:
            return False

    if inCubeSide == 5:
        if inD == 1:
            return True
        if inD == 2:
            return False
        if inD == 3:
            return False
        if inD == 4:
            return False

    if inCubeSide == 6:
        if inD == 1:
            return False
        if inD == 2:
            return False
        if inD == 3:
            return False
        if inD == 4:
            return False

def calculateWhichCube(x,y, cubeSize):

    if 0 <= y < cubeSize:
        if cubeSize * 1 <= x < cubeSize * 2:
            return 1

        if cubeSize * 2 <= x < cubeSize * 3:
            return 2

    if cubeSize <= y < cubeSize*2:

        if cubeSize * 1 <= x < cubeSize * 2:
            return 3


    if cubeSize * 2 <= y < cubeSize*3:
        if 0 <= x < cubeSize:
            return 4

        if cubeSize * 1 <= x < cubeSize * 2:
            return 5

    if cubeSize * 3 <= y < cubeSize*4:
        if 0 <= x < cubeSize * 1:
            return 6

    print("Error in compute cube")
    print("x,y:",x,y)
    return 0

def topleftOfCube(number, cubeSize):

    if number == 1:
        return [cubeSize*1,0]
    if number == 2:
        return [cubeSize*2,0]
    if number == 3:
        return [cubeSize*1,cubeSize*1]
    if number == 4:
        return [0,cubeSize*2]
    if number == 5:
        return [cubeSize*1,cubeSize*2]
    if number == 6:
        return [0,cubeSize*3]


    return [0,0]



if __name__ == '__main__':

    f=open("Task222.txt","r")
    lines=f.readlines()
    theInput = []
    theInput2 = []

    width = 0
    height = 0

    isMap = True

    for i in lines:
        i = i.rstrip()
        
        if len(i) == 0:
            isMap = False
            continue

        if isMap == True:
            theInput.append(i)
            height += 1
            width = max(width, len(i))
        else:
            theInput2.append(i)
        
    f.close()

    fullMap = np.zeros((width, height))

    startPosX = 0
    startPosY = 0

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):

            if j == ".":
                fullMap[jIndex,iIndex] = 1
                if startPosX == 0:
                    startPosX = jIndex
            elif j == "#":
                fullMap[jIndex,iIndex] = 2

    #fullMap[startPosX,startPosY] = 4

    instrLength = theInput2[0].replace("R", ",")
    instrLength = instrLength.replace("L", ",")
    instrLength = instrLength.split(",")

    instrTurns = []

    for i in theInput2[0]:
        if i == "R" or i == "L":
            instrTurns.append(i)
    
    currentDirection = 1

    currentPosX = startPosX
    currentPosY = startPosY

    #1 == Right
    #2 == Down
    #3 == Left
    #4 == Up

    turnPointer = 0

    toCube = dict()

    sideSize = 50

    toCube["1,1"] = [2,1]
    toCube["1,2"] = [3,2]
    toCube["1,3"] = [4,1]
    toCube["1,4"] = [6,1]

    toCube["2,1"] = [5,3]
    toCube["2,2"] = [3,3]
    toCube["2,3"] = [1,3]
    toCube["2,4"] = [6,4]

    toCube["3,1"] = [2,4]
    toCube["3,2"] = [5,2]
    toCube["3,3"] = [4,2]
    toCube["3,4"] = [1,4]

    toCube["4,1"] = [5,1]
    toCube["4,2"] = [6,2]
    toCube["4,3"] = [1,1]
    toCube["4,4"] = [3,1]

    toCube["5,1"] = [2,3]
    toCube["5,2"] = [6,3]
    toCube["5,3"] = [4,3]
    toCube["5,4"] = [3,4]

    toCube["6,1"] = [5,4]
    toCube["6,2"] = [2,2]
    toCube["6,3"] = [1,2]
    toCube["6,4"] = [4,4]

    theCubeSideSize = 50

    for i in instrLength:

        amountOfWalks = int(i)

        for j in range(0,amountOfWalks):

            bufferPosX = currentPosX
            bufferPosY = currentPosY

            if currentDirection == 1:
                bufferPosX += 1
            elif currentDirection == 2:
                bufferPosY += 1
            elif currentDirection == 3:
                bufferPosX -= 1
            elif currentDirection == 4:
                bufferPosY -= 1
            
            if bufferPosX >= width or bufferPosX < 0 or bufferPosY >= height or bufferPosY < 0 or fullMap[bufferPosX,bufferPosY] == 0:

                thisSide = calculateWhichCube(currentPosX, currentPosY, theCubeSideSize)
                nextCubeWithDir = toCube[str(thisSide) + "," + str(currentDirection)]

                nextCube = nextCubeWithDir[0]
                nextDir = nextCubeWithDir[1]

                shift = doShift(currentDirection,thisSide)
                cubeX, cubeY = topleftOfCube(nextCube, theCubeSideSize)
                aX, aY = topleftOfCube(thisSide, theCubeSideSize)

                if currentDirection == 1 or currentDirection == 3:
                    fromCubeOffset = currentPosY - aY
                else:
                    fromCubeOffset = currentPosX - aX


                if nextDir == 1:
                    startX = cubeX

                    if shift == False:
                        startY = cubeY + fromCubeOffset
                    else:
                        startY = cubeY + theCubeSideSize - 1 - fromCubeOffset
                
                if nextDir == 2:
                    startY = cubeY

                    if shift == False:
                        startX = cubeX + fromCubeOffset
                    else:
                        startX = cubeX + theCubeSideSize - 1 - fromCubeOffset

                if nextDir == 3:
                    startX = cubeX + theCubeSideSize - 1

                    if shift == False:
                        startY = cubeY + fromCubeOffset
                    else:
                        startY = cubeY + theCubeSideSize - 1 - fromCubeOffset

                if nextDir == 4:
                    startY = cubeY + theCubeSideSize - 1

                    if shift == False:
                        startX = cubeX + fromCubeOffset
                    else:
                        startX = cubeX + theCubeSideSize - 1 - fromCubeOffset


                if fullMap[startX, startY] == 1:

                    currentPosX = startX
                    currentPosY = startY
                    currentDirection = nextDir

            elif fullMap[bufferPosX,bufferPosY] == 1:
                currentPosX = bufferPosX
                currentPosY = bufferPosY
            elif fullMap[bufferPosX,bufferPosY] == 2:
                continue



        if turnPointer < len(instrTurns):

            if instrTurns[turnPointer] == "R":
                currentDirection += 1
                if currentDirection > 4:
                    currentDirection = 1
            elif instrTurns[turnPointer] == "L":
                currentDirection -= 1
                if currentDirection < 1:
                    currentDirection = 4
            turnPointer += 1


    answer = 1000 * (currentPosY + 1) + 4 * (currentPosX + 1) + (currentDirection-1)

    print("Answer")
    print(answer)

