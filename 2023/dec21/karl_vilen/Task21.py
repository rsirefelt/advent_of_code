import networkx as nx

if __name__ == '__main__':

    f=open("Task21.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        theInput.append(i)
    f.close()

    theGraph = nx.Graph()

    height = len(theInput)
    width = len(theInput[0])

    for indexI, i in enumerate(theInput):
        for indexJ, j in enumerate(i):

            thisStringStart = str(indexI) + "," + str(indexJ)

            
            if j in "S.":

                if j == "S":
                    startI = indexI
                    startJ = indexJ
                    startPos = thisStringStart

                if indexI - 1 >= 0:
                    thisStringEnd = str(indexI-1) + "," + str(indexJ)
                    if theInput[indexI-1][indexJ] in "S.":
                        theGraph.add_edge(thisStringStart, thisStringEnd, weight = 1)
                        theGraph.add_edge(thisStringEnd, thisStringStart, weight = 1)
                if indexI + 1 < height:
                    thisStringEnd = str(indexI+1) + "," + str(indexJ)
                    if theInput[indexI+1][indexJ] in "S.":
                        theGraph.add_edge(thisStringStart, thisStringEnd, weight = 1)
                        theGraph.add_edge(thisStringEnd, thisStringStart, weight = 1)
                if indexJ - 1 >= 0:
                    thisStringEnd = str(indexI) + "," + str(indexJ-1)
                    if theInput[indexI][indexJ-1] in "S.":
                        theGraph.add_edge(thisStringStart, thisStringEnd, weight = 1)
                        theGraph.add_edge(thisStringEnd, thisStringStart, weight = 1)
                if indexJ + 1 < width:
                    thisStringEnd = str(indexI) + "," + str(indexJ+1)
                    if theInput[indexI][indexJ+1] in "S.":
                        theGraph.add_edge(thisStringStart, thisStringEnd, weight = 1)
                        theGraph.add_edge(thisStringEnd, thisStringStart, weight = 1)

    reachableNodesSquareEven = 0
    reachableNodesSquareOdd = 0
    reachableNodesTriangleEven = 0
    reachableNodesTriangleOdd = 0

    maxSteps = 26501365
    maxLengthAcross = 130
    maxLengthCorner = 65

    thePathLength = nx.shortest_path_length(theGraph,source = startPos, weight = "weight")

    for key, value in thePathLength.items():
        if value <= maxLengthAcross and value % 2 == 0:
            reachableNodesSquareEven += 1
        if value <= maxLengthAcross and value % 2 == 1:
            reachableNodesSquareOdd += 1

        if value <= maxLengthCorner and value % 2 == 0:
            reachableNodesTriangleEven += 1
        if value <= maxLengthCorner and value % 2 == 1:
            reachableNodesTriangleOdd += 1

    triangleOdd = reachableNodesSquareOdd - reachableNodesTriangleOdd
    triangleEven = reachableNodesSquareEven - reachableNodesTriangleEven

    repeatedGrids = int((maxSteps - (width - 1)/2)/width)

    evenSquares = repeatedGrids*repeatedGrids
    oddSquares = (repeatedGrids+1) * (repeatedGrids+1)

    evenCorners = repeatedGrids
    oddCorners = repeatedGrids+1

    totalAnswer = evenSquares * reachableNodesSquareEven + oddSquares * reachableNodesSquareOdd + triangleEven * evenCorners - triangleOdd * oddCorners

    print(totalAnswer)
