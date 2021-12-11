import numpy as np

if __name__ == '__main__':

    f=open("Task11.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = [int(j) for j in i]
        theInput.append(list(i))
    f.close()

    theGrid = np.array(theInput)
    oneGrid = np.ones_like(theGrid)

    theGrid = np.pad(theGrid,1,mode='constant')
    oneGrid = np.pad(oneGrid,1,mode='constant')

    theGrid = theGrid + oneGrid

    maxSteps = 300
    amountOfSteps = 0
    totalFlashes = 0

    extraZeroes = len(theGrid)*4-4

    while amountOfSteps < maxSteps-1:

        amountOfSteps += 1

        theGrid = theGrid * oneGrid
        theGrid = theGrid + oneGrid

        hasFlashed = []
        anyNew = True

        while anyNew == True:

            [a, b] = np.where(theGrid > 9)

            c = [list(a),list(b)]

            if len(c[0]) > 0:
                anyNew = True
            else:
                anyNew = False

            for i in range(len(a)):

                x = c[0][i]
                y = c[1][i]

                theGrid[x][y] = 0

                hasFlashed.append([x,y])

                theGrid[x-1][y-1] += 1
                theGrid[x-1][y] += 1
                theGrid[x-1][y+1] += 1
                theGrid[x][y-1] += 1
                theGrid[x][y+1] += 1
                theGrid[x+1][y-1] += 1
                theGrid[x+1][y] += 1
                theGrid[x+1][y+1] += 1

            for i,j in hasFlashed:
                theGrid[i][j] = 0

            theGrid = theGrid * oneGrid

        thisFlashes = theGrid.size - np.count_nonzero(theGrid) - extraZeroes
        if thisFlashes == theGrid.size - extraZeroes:
            answer2 = amountOfSteps+1
            break

        totalFlashes += (thisFlashes)

    print("Done")
    print(totalFlashes)
    print(answer2)
    
