import sys

def findWater (maxX, maxY, maxZ, thisX, thisY, thisZ, fullCube, depth, potentialWater):

    if thisX < maxX:
        
        theString = str(thisX+1) + "," + str(thisY) + "," + str(thisZ)
        if theString in potentialWater:

            if fullCube[thisX+1][thisY][thisZ] == 0:
                fullCube[thisX+1][thisY][thisZ] = 2
                fullCube = findWater(maxX, maxY, maxZ, thisX+1, thisY, thisZ, fullCube, depth+1, potentialWater)

    if thisY < maxY:
        theString = str(thisX) + "," + str(thisY+1) + "," + str(thisZ)
        if theString in potentialWater:

            if fullCube[thisX][thisY+1][thisZ] == 0:
                fullCube[thisX][thisY+1][thisZ] = 2
                fullCube = findWater(maxX, maxY, maxZ, thisX, thisY+1, thisZ, fullCube, depth+1, potentialWater)
    
    if thisZ < maxZ:
        theString = str(thisX) + "," + str(thisY) + "," + str(thisZ+1)
        if theString in potentialWater:

            if fullCube[thisX][thisY][thisZ+1] == 0:
                fullCube[thisX][thisY][thisZ+1] = 2
                fullCube = findWater(maxX, maxY, maxZ, thisX, thisY, thisZ+1, fullCube, depth+1, potentialWater)
    
    if thisX > 0:    
        theString = str(thisX-1) + "," + str(thisY) + "," + str(thisZ)
        if theString in potentialWater:

            if fullCube[thisX-1][thisY][thisZ] == 0:
                fullCube[thisX-1][thisY][thisZ] = 2
                fullCube = findWater(maxX, maxY, maxZ, thisX-1, thisY, thisZ, fullCube, depth+1, potentialWater)

    if thisY > 0:        
        theString = str(thisX) + "," + str(thisY-1) + "," + str(thisZ)
        if theString in potentialWater:

            if fullCube[thisX][thisY-1][thisZ] == 0:
                fullCube[thisX][thisY-1][thisZ] = 2
                fullCube = findWater(maxX, maxY, maxZ, thisX, thisY-1, thisZ, fullCube, depth+1, potentialWater)

    if thisZ > 0:
        theString = str(thisX) + "," + str(thisY) + "," + str(thisZ-1)
        if theString in potentialWater:

            if fullCube[thisX][thisY][thisZ-1] == 0:
                fullCube[thisX][thisY][thisZ-1] = 2
                fullCube = findWater(maxX, maxY, maxZ, thisX, thisY, thisZ-1, fullCube, depth+1, potentialWater)

    return fullCube

import numpy as np

if __name__ == '__main__':

    f=open("Task18.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.split(",")
        theInput.append(i)
    f.close()

    maxX = 0
    maxY = 0
    maxZ = 0

    surfaceArea = 0

    for i in theInput:

        num1 = int(i[0])
        num2 = int(i[1])
        num3 = int(i[2])

        maxX = max(maxX, num1)
        maxY = max(maxY, num2)
        maxZ = max(maxZ, num3)

    theCube = np.zeros((maxX+2,maxY+2,maxZ+2))

    for i in theInput:

        num1 = int(i[0])
        num2 = int(i[1])
        num3 = int(i[2])

        theCube[num1][num2][num3] = 1

    potentialWater = dict()


    for i in theInput:

        num1 = int(i[0])
        num2 = int(i[1])
        num3 = int(i[2])

        if theCube[num1+1][num2][num3] == 0:
            surfaceArea += 1
            thisString = str(num1+1) + "," + str(num2) + "," + str(num3)
            potentialWater[thisString] = 1

        if theCube[num1-1][num2][num3] == 0:
            surfaceArea += 1
            thisString = str(num1-1) + "," + str(num2) + "," + str(num3)
            potentialWater[thisString] = 1
                
        if theCube[num1][num2+1][num3] == 0:
            surfaceArea += 1
            thisString = str(num1) + "," + str(num2+1) + "," + str(num3)
            potentialWater[thisString] = 1

        if theCube[num1][num2-1][num3] == 0:
            surfaceArea += 1
            thisString = str(num1) + "," + str(num2-1) + "," + str(num3)
            potentialWater[thisString] = 1

        if theCube[num1][num2][num3+1] == 0:
            surfaceArea += 1
            thisString = str(num1) + "," + str(num2) + "," + str(num3+1)
            potentialWater[thisString] = 1

        if theCube[num1][num2][num3-1] == 0:
            surfaceArea += 1
            thisString = str(num1) + "," + str(num2) + "," + str(num3-1)
            potentialWater[thisString] = 1

    potentialWater2 = potentialWater.copy()

    for i in potentialWater.keys():

        coords = i.split(",")

        num1 = int(coords[0])
        num2 = int(coords[1])
        num3 = int(coords[2])

        if num1 <= maxX:
            if theCube[num1+1][num2][num3] == 0:
                theString = str(num1+1) + "," + str(num2) + "," + str(num3)
                potentialWater2[theString] = 1
        
        if num1 > 0:
            if theCube[num1-1][num2][num3] == 0:
                theString = str(num1-1) + "," + str(num2) + "," + str(num3)
                potentialWater2[theString] = 1

        if num2 <= maxY:
            if theCube[num1][num2+1][num3] == 0:
                theString = str(num1) + "," + str(num2+1) + "," + str(num3)
                potentialWater2[theString] = 1
        
        if num2 > 0:
            if theCube[num1][num2-1][num3] == 0:
                theString = str(num1) + "," + str(num2-1) + "," + str(num3)
                potentialWater2[theString] = 1
        
        if num3 <= maxZ:
            if theCube[num1][num2][num3+1] == 0:
                theString = str(num1) + "," + str(num2) + "," + str(num3+1)
                potentialWater2[theString] = 1

        if num3 > 0:
            if theCube[num1][num2][num3-1] == 0:
                theString = str(num1) + "," + str(num2) + "," + str(num3-1)
                potentialWater2[theString] = 1

    print(len(potentialWater))
    print(len(potentialWater2))
    sys.setrecursionlimit(4000)

    theStart = list(potentialWater2.keys())
    startWater = theStart[80].split(",")

    for i in theStart:
        thisString = i.split(",")

        if int(thisString[0]) == 0 or int(thisString[1]) == 0 or int(thisString[2]) == 0:


            startX = int(thisString[0])
            startY = int(thisString[1])
            startZ = int(thisString[2])

    theCube[startX][startY][startZ] = 2

    theCube = findWater(maxX+1, maxY+1, maxZ+1, startX,startY,startZ,theCube,0, list(potentialWater2.keys()))

    surfaceArea2 = 0

    for i in theInput:

        num1 = int(i[0])
        num2 = int(i[1])
        num3 = int(i[2])

        if theCube[num1+1][num2][num3] == 2:
            surfaceArea2 += 1
        if theCube[num1-1][num2][num3] == 2:
            surfaceArea2 += 1
        if theCube[num1][num2+1][num3] == 2:
            surfaceArea2 += 1
        if theCube[num1][num2-1][num3] == 2:
            surfaceArea2 += 1
        if theCube[num1][num2][num3+1] == 2:
            surfaceArea2 += 1
        if theCube[num1][num2][num3-1] == 2:
            surfaceArea2 += 1

    
    print("Answer")
    print(surfaceArea)
    print(surfaceArea2)
    
