import networkx as nx
import numpy as np

if __name__ == '__main__':

    f=open("Task12.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    gridWidth = len(theInput[0])
    gridHeight = len(theInput)

    theGrid = np.ones((gridHeight, gridWidth))
    theGraph = nx.grid_2d_graph(*theGrid.shape, create_using=nx.DiGraph)

    input2 = []

    allStarts = []

    for iIndex, i in enumerate(theInput):
        input2.append([0]*gridWidth)
        for jIndex, j in enumerate(i):
            if j == "S":
                start = (iIndex,jIndex)
                theInput[iIndex][jIndex].replace("S","a")
                input2[iIndex][jIndex] = "a"
                allStarts.append(start)
            elif j == "E":
                end = (iIndex,jIndex)
                input2[iIndex][jIndex] = "z"
            else:
                input2[iIndex][jIndex] = theInput[iIndex][jIndex]
                if j == "a":
                    allStarts.append((iIndex,jIndex))

    for iIndex, i in enumerate(input2):
        for jIndex, j in enumerate(i):
            
            thisHeight = ord(j) - ord("a")

            if iIndex + 1 < gridHeight:
                if (ord(input2[iIndex+1][jIndex]) - ord("a")) - thisHeight > 1:
                    theGraph.remove_edge((iIndex,jIndex), (iIndex+1,jIndex))
            
            if iIndex - 1 >= 0:
                if (ord(input2[iIndex-1][jIndex]) - ord("a")) - thisHeight > 1:
                    theGraph.remove_edge((iIndex,jIndex), (iIndex-1,jIndex))
            
            if jIndex + 1 < gridWidth:
                if (ord(input2[iIndex][jIndex+1]) - ord("a")) - thisHeight > 1:
                    theGraph.remove_edge((iIndex,jIndex), (iIndex,jIndex+1))
            
            if jIndex - 1 >= 0:
                if (ord(input2[iIndex][jIndex-1]) - ord("a")) - thisHeight > 1:
                    theGraph.remove_edge((iIndex,jIndex), (iIndex,jIndex-1))

    for a, b, c in theGraph.edges(data=True):
        c["weight"] = theGrid[b]

    print("Answer 1")
    print(nx.shortest_path_length(theGraph,start,end, weight = "weight"))

    shortest = 100000
    for i in allStarts:
        thisLength = 100000
        try:
            thisLength = nx.shortest_path_length(theGraph,i,end, weight = "weight")
            shortest = min(shortest, thisLength)
        except:
            continue

    print("Answer 2")
    print(shortest)
