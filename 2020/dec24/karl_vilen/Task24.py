if __name__ == '__main__':
    
    f=open("Task24.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    directions = dict()
    directions["e"] = [1,0]
    directions["se"] = [1,-1]
    directions["sw"] = [0,-1]
    directions["w"] = [-1,0]
    directions["nw"] = [-1,1]
    directions["ne"] = [0,1]

    
    allDirections = []

    allTiles = dict()

    for i in theInput:
        j = 0
        theseDirections = []
        while j < len(i):
            thisString = ""
            if i[j] == "e" or i[j] == "w":
                thisString = i[j]
                j += 1
            else:
                thisString = i[j]+i[j+1]
                j += 2

            theseDirections.append(thisString)

        allDirections.append(theseDirections)

    flippedTiles = dict()

    for i in allDirections:
        position = [0,0]
        for j in i:
            position[0] += directions[j][0]
            position[1] += directions[j][1]

        thePosition = str(position)
        thePosition = thePosition.replace("[","")
        thePosition = thePosition.replace("]","")
        thePosition = thePosition.replace(" ","")

        if thePosition not in flippedTiles:
            flippedTiles[thePosition] = 1
        else:
            flippedTiles[thePosition] += 1
            flippedTiles[thePosition] = flippedTiles[thePosition] % 2

    theSum = 0
    for keys, values in flippedTiles.items():
        theSum += values

    print("Done")
    print(theSum)

    toRemove = []
    for key in flippedTiles.keys():
        if flippedTiles[key] == 0:
            toRemove.append(key)

    for i in toRemove:
        flippedTiles.pop(i)

    for i in range(100):
        toInvestigate = []
        for key, value in flippedTiles.items():
            if value == 1:
                if key not in toInvestigate:
                    toInvestigate.append(key)

                numbers = key.split(",")
                number1 = int(numbers[0])
                number2 = int(numbers[1])

                for keys, values in directions.items():
                    key1 = number1 + values[0]
                    key2 = number2 + values[1]
                    theString = str(key1) + "," + str(key2)
                    if theString not in toInvestigate:
                        toInvestigate.append(theString)

        toFlip = []

        for j in toInvestigate:

            neighbours = 0
            numbers = j.split(",")
            number1 = int(numbers[0])
            number2 = int(numbers[1])

            for key, value in directions.items():

                a = number1 + value[0]
                b = number2 + value[1]

                theString = str(a) + "," + str(b)

                if theString in flippedTiles.keys():
                    neighbours += 1

            if j not in flippedTiles:
                if neighbours == 2:
                    toFlip.append(j)
            elif flippedTiles[j] == 0:
                if neighbours == 2:
                    toFlip.append(j)
            else:
                if neighbours == 0 or neighbours > 2:
                    toFlip.append(j)


        for j in toFlip:
            if j not in flippedTiles:
                flippedTiles[j] = 1
            elif flippedTiles[j] == 0:
                flippedTiles[j] = 1
            else:
                flippedTiles[j] = 0

        toRemove = []
        for key in flippedTiles.keys():
            if flippedTiles[key] == 0:
                toRemove.append(key)

        for i in toRemove:
            flippedTiles.pop(i)

        theSum = 0
        for keys, values in flippedTiles.items():
            theSum += values

    theSum = 0
    for keys, values in flippedTiles.items():
        theSum += values
    print("Done2")
    print(theSum)
