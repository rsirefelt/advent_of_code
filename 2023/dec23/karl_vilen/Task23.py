import networkx as nx

def calculateLength(shortPaths, startNode, endNode):

    for i in shortPaths:
        if i[0] == startNode and i[1] == endNode:
            return i[2]

    return 99999999999999999999

if __name__ == '__main__':

    f=open("Task23.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("^",".")
        i = i.replace("v",".")
        i = i.replace("<",".")
        i = i.replace(">",".")
        theInput.append(i)
    f.close()

    theGraph = nx.Graph()
    height = len(theInput)
    width = len(theInput[0])

    startingPos = 0
    endingPos = 0

    junctions = []

    for indexI, i in enumerate(theInput):
        for indexJ, j in enumerate(i):

            if indexI == 0 and j == ".":
                startingPos = str(indexI) + "," + str(indexJ)
            elif indexI == height-1 and j == ".":
                endingPos = str(indexI) + "," + str(indexJ)

            startPos = str(indexI) + "," + str(indexJ)

            possiblePaths = 0

            if j == ".":
                if indexI - 1 >= 0:
                    if theInput[indexI-1][indexJ] in ".^":
                        endPos = str(indexI-1) + "," + str(indexJ)
                        theGraph.add_edge(startPos, endPos, weight = 1)
                        possiblePaths+=1
                if indexI + 1 < height:
                    if theInput[indexI+1][indexJ] in ".v":
                        endPos = str(indexI+1) + "," + str(indexJ)
                        theGraph.add_edge(startPos, endPos, weight = 1)
                        possiblePaths+=1
                if indexJ - 1 >= 0:
                    if theInput[indexI][indexJ-1] in ".<":
                        endPos = str(indexI) + "," + str(indexJ-1)
                        theGraph.add_edge(startPos, endPos, weight = 1)
                        possiblePaths+=1
                if indexJ + 1 > 0:
                    if theInput[indexI][indexJ+1] in ".>":
                        endPos = str(indexI) + "," + str(indexJ+1)
                        theGraph.add_edge(startPos, endPos, weight = 1)
                        possiblePaths+=1

            if possiblePaths > 2:
                junctions.append(startPos)

            elif j == "^":
                if indexI - 1 >= 0:
                    if theInput[indexI-1][indexJ] in ".^":
                        endPos = str(indexI-1) + "," + str(indexJ)
                        theGraph.add_edge(startPos, endPos, weight = 1)
            elif j == "v":
                if indexI + 1 < height:
                    if theInput[indexI+1][indexJ] in ".v":
                        endPos = str(indexI+1) + "," + str(indexJ)
                        theGraph.add_edge(startPos, endPos, weight = 1)
            elif j == "<":
                if indexJ - 1 >= 0:
                    if theInput[indexI][indexJ-1] in ".<":
                        endPos = str(indexI) + "," + str(indexJ-1)
                        theGraph.add_edge(startPos, endPos, weight = 1)
            elif j == ">":
                if indexJ - 1 < width:
                    if theInput[indexI][indexJ+1] in ".>":
                        endPos = str(indexI) + "," + str(indexJ+1)
                        theGraph.add_edge(startPos, endPos, weight = 1)

    junctionsStartEnd = junctions.copy()
    junctionsStartEnd.append(startingPos)
    junctionsStartEnd.append(endingPos)

    shortPaths = []

    for i in junctionsStartEnd:
        for j in junctionsStartEnd:

            if str(i) == str(j):
                continue

            thesePaths = nx.all_simple_paths(theGraph,source = i, target=j, cutoff = 700)

            pathsFound = 0
            for thisPath in thesePaths:

                junctionsCrossed = 0

                for k in junctionsStartEnd:
                    if k in thisPath:
                        junctionsCrossed += 1

                if junctionsCrossed == 2:
                    shortPaths.append([i,j,len(thisPath)-1])

    theGraph2 = nx.Graph()
    for i in shortPaths:

        theGraph2.add_edge(i[0], i[1], weight = i[2])

    thisPath = nx.all_simple_paths(theGraph2,source = startingPos, target=endingPos)

    allPaths = list(thisPath)

    maxLength = 0

    for i in allPaths:
        theLength = 0        
        for indexJ in range(len(i) - 1):

            theLength += calculateLength(shortPaths, i[indexJ], i[indexJ+1])

        maxLength = max(maxLength, theLength)

    print(maxLength)

