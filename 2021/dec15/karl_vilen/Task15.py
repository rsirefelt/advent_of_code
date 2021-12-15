import networkx as nx
import numpy as np

if __name__ == '__main__':

    f=open("Task15.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    theSize = len(theInput)

    theGrid = np.zeros((theSize, theSize))

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):
            theGrid[iIndex, jIndex] = int(j)

    theGraph = nx.grid_2d_graph(*theGrid.shape, create_using=nx.DiGraph) 

    start = (0,0)
    end = (theSize-1,theSize-1)

    for a, b, c in theGraph.edges(data=True):
        c["weight"] = theGrid[b]

    print("Part 1")
    print(nx.shortest_path_length(theGraph,start,end, weight = "weight"))

    newGrid = np.block([[theGrid+i+j for i in range(5)] for j in range(5)])
    newGrid[newGrid > 9] -= 9

    theGraph = nx.grid_2d_graph(*newGrid.shape, create_using=nx.DiGraph) 

    theSize2 = len(theInput*5)
    end = (theSize2-1,theSize2-1)

    for a, b, c in theGraph.edges(data=True):
        c["weight"] = newGrid[b]

    print("Part 2")
    print(nx.shortest_path_length(theGraph,start,end, weight = "weight"))
