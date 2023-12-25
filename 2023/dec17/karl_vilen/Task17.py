import networkx as nx

if __name__ == '__main__':

    f=open("Task17.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        theInput.append(i)
    f.close()

    theGraph = nx.DiGraph()

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    height = len(theInput)
    width = len(theInput[0])

    allDirections = [UP, RIGHT, DOWN, LEFT]
    rangeLow = 4
    rangeHigh = 11

    for i in range(rangeLow, rangeHigh):

        endNode = "0," + str(i) + "," + str(RIGHT)
        theWeight = 0
        for j in range(min(i,width-1)):
            theWeight += int(theInput[0][j+1])
        theGraph.add_edge("0,0", endNode, weight = theWeight)

        endNode = str(i) + ",0," + str(DOWN)
        theWeight = 0
        for j in range(min(i,height-1)):
            theWeight += int(theInput[j+1][0])
        theGraph.add_edge("0,0", endNode, weight = theWeight)

    endNode = str(height-1) + "," + str(width-1)

    for i in allDirections:
        theGraph.add_edge(endNode + "," + str(i), endNode, weight = 0)

    for indexI, i in enumerate(theInput):
        for indexJ, j in enumerate(i):

            endPos = str(indexI) + "," + str(indexJ)

            for k in range(rangeLow, rangeHigh):

                endPosFull = endPos + "," + str(UP)
                if indexI + k < height:
                    startPosFull = str(indexI + k) + "," + str(indexJ) + "," + str(LEFT)
                    theWeight = 0
                    for l in range(indexI,indexI+k):
                        theWeight += int(theInput[l][indexJ])
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)
                    startPosFull = str(indexI + k) + "," + str(indexJ) + "," + str(RIGHT)
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)

                endPosFull = endPos + "," + str(RIGHT)
                if indexJ - k >= 0:
                    startPosFull = str(indexI) + "," + str(indexJ-k) + "," + str(UP)
                    theWeight = 0
                    for l in range(indexJ-k+1,indexJ+1):
                        theWeight += int(theInput[indexI][l])
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)
                    startPosFull = str(indexI) + "," + str(indexJ-k) + "," + str(DOWN)
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)

                endPosFull = endPos + "," + str(DOWN)
                if indexI - k >= 0:
                    startPosFull = str(indexI - k) + "," + str(indexJ) + "," + str(LEFT)
                    theWeight = 0
                    for l in range(indexI-k+1,indexI+1):
                        theWeight += int(theInput[l][indexJ])
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)
                    startPosFull = str(indexI - k) + "," + str(indexJ) + "," + str(RIGHT)
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)

                endPosFull = endPos + "," + str(LEFT)
                if indexJ + k < width:
                    startPosFull = str(indexI) + "," + str(indexJ+k) + "," + str(UP)
                    theWeight = 0
                    for l in range(indexJ,indexJ+k):
                        theWeight += int(theInput[indexI][l])
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)
                    startPosFull = str(indexI) + "," + str(indexJ+k) + "," + str(DOWN)
                    theGraph.add_edge(startPosFull, endPosFull, weight = theWeight)


    thePathLength = nx.shortest_path_length(theGraph,"0,0",endNode, weight = "weight")
    print(thePathLength)
