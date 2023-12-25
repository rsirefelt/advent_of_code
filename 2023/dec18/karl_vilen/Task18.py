if __name__ == '__main__':

    f=open("Task18.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("(#", "")
        i = i.replace(")", "")
        i = i.split(" ")
        theInput.append(i)
    f.close()

    coordinates = []
    currentI = 0
    currentJ = 0

    dotsOnEdge = 0

    for i in theInput:

        theHex = int(i[2][:5],16)
        theDir = i[2][5]

        #theHex = int(i[1])
        #theDir = i[0]

        if theDir == "3" or theDir == "U":
            currentI -= theHex
            coordinates.append([currentI, currentJ])
        elif theDir == "1" or theDir == "D":
            currentI += theHex
            coordinates.append([currentI, currentJ])
        elif theDir == "0" or theDir == "R":
            currentJ += theHex
            coordinates.append([currentI, currentJ])
        elif theDir == "2" or theDir == "L":
            currentJ -= theHex
            coordinates.append([currentI, currentJ])

        dotsOnEdge += theHex

    totalArea = 0

    for i in range(len(coordinates)):

        x = coordinates[i][0]
        if i-1 >= 0:
            y1 = coordinates[i-1][1]
        else:
            y1 = coordinates[len(coordinates)-1][1]
        
        if i+1 < len(coordinates):
            y2 = coordinates[i+1][1]
        else:
            y2 = coordinates[0][1]

        thisArea = x * (y2-y1)
        totalArea += thisArea

    totalArea = abs(totalArea) / 2
    theI = totalArea - dotsOnEdge / 2 + 1
    answer = theI + dotsOnEdge
    print(answer)

