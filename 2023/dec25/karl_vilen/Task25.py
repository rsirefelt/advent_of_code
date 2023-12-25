import networkx as nx

if __name__ == '__main__':

    f=open("Task25.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace(":","")
        i = i.split(" ")
        theInput.append(i)
    f.close()

    theGraph = nx.Graph()
    allNodes = []

    for i in theInput:
        for j in i:
            if j not in allNodes:
                allNodes.append(j)
            theGraph.add_edge(i[0], j, capacity = 1)

    breakAll = False
    for i in allNodes:
        for j in allNodes:
            if i == j:
                continue
            cutLength, newSets = nx.minimum_cut(theGraph,i,j)
            if cutLength == 3:
                breakAll = True
                break
        if breakAll:
            break

    print(len(newSets[0]) * len(newSets[1]))
