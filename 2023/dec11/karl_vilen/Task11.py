import numpy as np

if __name__ == '__main__':

    f=open("Task11.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("#","1")
        i = i.replace(".","0")
        i = list(i)
        for j in range(0, len(i)):
            i[j] = int(i[j])
        theInput.append(i)
    f.close()

    theGrid = np.array(theInput)

    addColumns = []
    addRows = []

    for i in range(len(theGrid[:,i])):

        thisColumn = theGrid[:,i]
        if sum(thisColumn) == 0:
            addColumns.append(i)

    for i in range(len(theGrid[i,:])):

        thisRow = theGrid[i,:]
        if sum(thisRow) == 0:
            addRows.append(i)

    galaxies = np.argwhere(theGrid == 1)
    totalDist = 0
    expansion = 1000000-1

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):

            xDist = abs(galaxies[i][0] - galaxies[j][0])
            yDist = abs(galaxies[i][1] - galaxies[j][1])
            addX = 0
            addY = 0

            for k in addRows:
                if min(galaxies[i][0], galaxies[j][0]) < k < max(galaxies[i][0], galaxies[j][0]):
                    addY += 1

            for l in addColumns:
                if min(galaxies[i][1], galaxies[j][1]) < l < max(galaxies[i][1], galaxies[j][1]):
                    addX += 1

            thisDist = xDist + addX * expansion + yDist + addY * expansion
            totalDist += thisDist

    print(totalDist)