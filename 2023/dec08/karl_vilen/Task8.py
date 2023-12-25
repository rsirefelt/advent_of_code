import numpy as np

if __name__ == '__main__':

    f=open("Task8.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace(" = (",",")
        i = i.replace(")","")
        i = i.replace(" ","")
        i = i.split(",")
        theInput.append(i)
    f.close()

    direction = ""
    paths = dict()

    for index, i in enumerate(theInput):
        if index == 0:
            direction = i[0]
            continue
        elif index == 1:
            continue

        paths[i[0]] = [i[1], i[2]]

    directionIndex = -1
    length = 0

    currentPositions = []
    currentFinishes = []

    for i in paths.keys():
        if i[-1] == "A":
            currentPositions.append(i)
            currentFinishes.append(-1)

    hasFoundFinish = 0

    while 1 > 0:

        length += 1
        directionIndex += 1

        for index, i in enumerate(currentPositions):

            if directionIndex >= len(direction):
                directionIndex = 0
            newDirection = direction[directionIndex]

            if newDirection == "L":
                currentPositions[index] = paths[i][0]
            elif newDirection == "R":
                currentPositions[index] = paths[i][1]

        for index, i in enumerate(currentPositions):
            if i[-1] == "Z":
                
                if currentFinishes[index] == -1:
                    currentFinishes[index] = length
                    hasFoundFinish += 1

        if hasFoundFinish == len(currentPositions):
            break

    a = np.lcm.reduce(currentFinishes,dtype='int64')
    print(a)


