def returnIntervals(groups, groupIndex, maxGroupIndex, inInterval, minimumFound):

    resultIntervals = []
    
    for k in range(0, len(inInterval), 2):

        startI = inInterval[k]
        endI = inInterval[k] + inInterval[k+1] - 1
        allFound = False
        newStartInterval = -1

        while allFound == False:

            foundAnyGroup = False
            lowestGroupStartAboveI = 100000000000000000000000000000000

            if newStartInterval != -1:
                startI = newStartInterval

            for i in groups[groupIndex]:

                if i[1] <= startI < i[1] + i[2]:
                    
                    foundAnyGroup = True
                    newIntervalStart = startI

                    if endI <= i[1] + i[2] - 1:
                        newIntervalEnd = endI
                        allFound = True
                    else:
                        newIntervalEnd = i[1] + i[2] - 1

                    newInterval = [i[0] + newIntervalStart - i[1], newIntervalEnd - startI + 1]
                    newStartInterval = newIntervalEnd + 1
                    resultIntervals.append(newInterval)
                    break

                if i[1] > startI:
                    lowestGroupStartAboveI = min(lowestGroupStartAboveI, i[1])

            if foundAnyGroup == False:
                if lowestGroupStartAboveI != 100000000000000000000000000000000:
                    resultIntervals.append([startI, lowestGroupStartAboveI - startI])
                    newStartInterval = lowestGroupStartAboveI
                else:
                    resultIntervals.append([startI, inInterval[k] + inInterval[k+1] - startI])
                    allFound = True

    if groupIndex + 1 > maxGroupIndex:

        toReturn = minimumFound
        for i in resultIntervals:
            toReturn = min(toReturn, i[0])
        return min(minimumFound, toReturn)

    else:

        newResults = []
        toReturn = 99999999999999999999999

        for i in resultIntervals:
            toReturn = min(toReturn, returnIntervals(groups, groupIndex+1, maxGroupIndex, i, minimumFound))
        return toReturn

if __name__ == '__main__':

    f=open("Task5.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("seeds: ","")
        if "map" in i:
            continue
        i = i.split(" ")
        if len(i) > 1:
            for j in range(0, len(i)):
                i[j] = int(i[j])
        theInput.append(i)
    f.close()

    seeds = theInput[0]
    groups = dict()
    groupNumber = 0

    for index, i in enumerate(theInput):

        if index == 0:
            continue

        if len(i) < 2:
            groupNumber += 1
            continue

        if groupNumber not in groups.keys():
            groups[groupNumber] = []
        groups[groupNumber].append(i)

    a = returnIntervals(groups, 1, 7, seeds, 999999999999999999999)
    print(a)
