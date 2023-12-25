def nextDir(currentDir, currentPipe):

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    if currentPipe == "|" or currentPipe == "-":
        return currentDir

    elif currentPipe == "F":
        if currentDir == UP:
            return RIGHT
        else:
            return DOWN

    elif currentPipe == "7":
        if currentDir == RIGHT:
            return DOWN
        else:
            return LEFT

    elif currentPipe == "L":
        if currentDir == DOWN:
            return RIGHT
        else:
            return UP

    elif currentPipe == "J":
        if currentDir == RIGHT:
            return UP
        else:
            return LEFT

    else:
        print("ERROR")
        print(currentDir)
        print(currentPipe)

if __name__ == '__main__':

    f=open("Task10.txt","r")
    lines=f.readlines()
    theInput = []
    theInput2 = []

    for i in lines:
        i = i.strip()
        theInput.append(i)
        i = i.replace("|",".")
        i = i.replace("-",".")
        i = i.replace("F",".")
        i = i.replace("L",".")
        i = i.replace("J",".")
        i = i.replace("7",".")
        i = i.replace("S",".")
        theInput2.append(list(i))
    f.close()

    startI = 0
    startJ = 0

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):
            if j == "S":
                startI = iIndex
                startJ = jIndex

    upwards = ["|", "7", "F"]
    downwards = ["|", "J", "L"]
    rightwards = ["-", "J", "7"]
    leftwards = ["-", "L", "F"]

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    pos1I = startI
    pos1J = startJ
    pos2I = startI
    pos2J = startJ
    firstDecided = False

    direction1 = 0
    direction2 = 0

    theInput2[pos1I][pos1J] = "J"

    if theInput[startI-1][startJ] in upwards:
        direction1 = UP
        pos1I -=1
        firstDecided = True
    if theInput[startI+1][startJ] in downwards:
        if firstDecided:
            direction2 = DOWN
            pos2I += 1
        else:
            direction1 = DOWN
            pos1I += 1
            firstDecided = True
    if theInput[startI][startJ-1] in leftwards:
        if firstDecided:
            direction2 = LEFT
            pos2J -= 1
        else:
            direction1 = LEFT
            pos2J -= 1
            firstDecided = True
    if theInput[startI][startJ+1] in rightwards:
        direction2 = RIGHT
        pos2J += 1

    steps = 1

    theInput2[pos1I][pos1J] = theInput[pos1I][pos1J]
    theInput2[pos2I][pos2J] = theInput[pos2I][pos2J]

    while pos1I != pos2I or pos1J != pos2J:

        direction1 = nextDir(direction1, theInput[pos1I][pos1J])
        direction2 = nextDir(direction2, theInput[pos2I][pos2J])

        if direction1 == UP:
            pos1I -= 1
        elif direction1 == DOWN:
            pos1I += 1
        elif direction1 == RIGHT:
            pos1J += 1
        elif direction1 == LEFT:
            pos1J -= 1

        if direction2 == UP:
            pos2I -= 1
        elif direction2 == DOWN:
            pos2I += 1
        elif direction2 == RIGHT:
            pos2J += 1
        elif direction2 == LEFT:
            pos2J -= 1

        theInput2[pos1I][pos1J] = theInput[pos1I][pos1J]
        theInput2[pos2I][pos2J] = theInput[pos2I][pos2J]

        steps += 1

    theInput2[pos1I][pos1J] = theInput[pos1I][pos1J]
        
    print(steps)

    inside = 0

    for indexI, i in enumerate(theInput2):
        for indexJ, j in enumerate(i):

            thisCount = 0

            if j == ".":

                for k in range(indexJ,-1,-1):
                    if theInput2[indexI][k] in ["|", "L", "J"]:
                        thisCount += 1

                if thisCount % 2 == 1:
                    inside += 1

    print(inside)

