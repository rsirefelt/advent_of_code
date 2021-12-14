def mostCommonAmount(theList, thisIndex):
    theMax = 0
    theDict = dict()
    for i in theList:
        if i not in theDict.keys():
            theDict[i] = 1
        else:
            theDict[i] += 1

        if theDict[i] > theMax:
            if i[0].isupper() == False:
                theMax = theDict[i]

    if thisIndex not in theDict.keys():
        return [theMax, 0]
    else:
        return [theMax, theDict[thisIndex]]

connections = dict()
allPaths = []

def findPaths(thisPath, connected):

    for i in connected:

        canVisitSmall = True
        if i[0].isupper() == False:

            if i == "start" or i == "end":
                canVisitSmall = False
            else:
                smallVisited, thisVisited = mostCommonAmount(thisPath, i)

                if smallVisited == 2 and thisVisited != 0:
                    canVisitSmall = False

        if i == "end":
            b = thisPath.copy()
            b.append(i)
            c = b.copy()
            allPaths.append(c)
            continue

        elif i[0].isupper() == True or canVisitSmall == True:

            b = thisPath.copy()
            b.append(i)
            findPaths(b,connections[i])

        else:
            continue

    return thisPath


if __name__ == '__main__':

    f=open("Task12.txt","r")
    lines=f.readlines()
    theInput = []
    
    for i in lines:
        i = i.rstrip()
        i = i.split("-")
        if i[0] not in connections.keys():
            connections[i[0]] = []
            connections[i[0]].append(i[1])
        else:
            connections[i[0]].append(i[1])

        if i[1] not in connections.keys():
            connections[i[1]] = []
            connections[i[1]].append(i[0])
        else:
            connections[i[1]].append(i[0])

    f.close()

    thisPath = []
    thisPath.append("start")
    newConnections = connections["start"]
    findPaths(thisPath.copy(),newConnections)

    print("Done")
    print(len(allPaths))
