import networkx as nx

if __name__ == '__main__':

    f=open("Task24.txt","r")
    lines=f.readlines()
    theInput = []

    totalStartString = ""

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
        totalStartString += i
    f.close()

    height = len(theInput)
    width = len(theInput[0])

    startPos = "1,0,0"
    endPos = str(width-2) + "," + str(height-1) + ",0"

    #startPos = "1,0"
    #endPos = str(width-2) + "," + str(height-1)

    #oldField = [[1,0,0], [width-2,height-1,0]]
    oldField = []

    theGraph = nx.DiGraph()

    theGraph.add_node(startPos)

    #for i in theInput:
    #    for j in range(2,len(i)):
    #        theGraph.add_edge(i[0], i[j])

    blizzards = dict()
    blizzardIndex = 0

    emptyField = []

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):
            if j == "^":
                blizzards[blizzardIndex] = [jIndex, iIndex, "up"]
            elif j == ">":
                blizzards[blizzardIndex] = [jIndex, iIndex, "right"]
            elif j == "v":
                blizzards[blizzardIndex] = [jIndex, iIndex, "down"]
            elif j == "<":
                blizzards[blizzardIndex] = [jIndex, iIndex, "left"]
            blizzardIndex += 1

            if j != "#":
                emptyField.append([jIndex, iIndex])

            if j == ".":
                oldField.append([jIndex, iIndex, 0])



    #print(len(blizzards))
    #print(len(emptyField))

    startString = ""

    for keys, values in blizzards.items():
        startString += str(values[0]) + "," + str(values[1]) + ","

    #print(startString)

    i = 0

    

    while True:

        i += 1

        print(i)

        thisField = emptyField.copy()

        for keys, values in blizzards.items():

            if values[2] == "up":
                values[1] -= 1
                if values[1] == 0:
                    values[1] = height - 2
            elif values[2] == "right":
                values[0] += 1
                if values[0] == width - 1:
                    values[0] = 1
            elif values[2] == "down":
                values[1] += 1
                if values[1] == height - 1:
                    values[1] = 1
            elif values[2] == "left":
                values[0] -= 1
                if values[0] == 0:
                    values[0] = width - 2

            if [values[0],values[1]] in thisField:
                thisField.remove([values[0],values[1]])

        for thisFieldCoord in thisField:
            freeCoord = str(thisFieldCoord[0]) + "," + str(thisFieldCoord[1]) + "," + str(i)
            theGraph.add_node(freeCoord)

        for theOldCoord in oldField:

            fromPos = str(theOldCoord[0]) + "," + str(theOldCoord[1]) + "," + str(i - 1)

            if [theOldCoord[0], theOldCoord[1]] in thisField:
                toPos = str(theOldCoord[0]) + "," + str(theOldCoord[1]) + "," + str(i)
                theGraph.add_edge(fromPos, toPos)
            if [theOldCoord[0] - 1, theOldCoord[1]] in thisField:
                toPos = str(theOldCoord[0] - 1) + "," + str(theOldCoord[1]) + "," + str(i)
                theGraph.add_edge(fromPos, toPos)
            if [theOldCoord[0] + 1, theOldCoord[1]] in thisField:
                toPos = str(theOldCoord[0] + 1) + "," + str(theOldCoord[1]) + "," + str(i)
                theGraph.add_edge(fromPos, toPos)
            if [theOldCoord[0], theOldCoord[1] - 1] in thisField:
                toPos = str(theOldCoord[0]) + "," + str(theOldCoord[1] - 1) + "," + str(i)
                theGraph.add_edge(fromPos, toPos)
            if [theOldCoord[0], theOldCoord[1] + 1] in thisField:
                toPos = str(theOldCoord[0]) + "," + str(theOldCoord[1] + 1) + "," + str(i)
                theGraph.add_edge(fromPos, toPos)

            if [theOldCoord[0], theOldCoord[1]] == [1,1]:
                #theGraph.add_edge(fromPos, startPos)
                theGraph.add_edge(fromPos, "START")
            if [theOldCoord[0], theOldCoord[1]] == [width-2,height-2]:
                #theGraph.add_edge(fromPos, endPos)
                theGraph.add_edge(fromPos, "FINISH")

        #print("Edges after i:", i)
        #print(theGraph.edges())
 
        oldField = thisField.copy()

        currentString = ""

        for keys, values in blizzards.items():
            currentString += str(values[0]) + "," + str(values[1]) + ","

        if currentString == startString:
            
            for thisFieldCoord in thisField:
                freeCoord = str(thisFieldCoord[0]) + "," + str(thisFieldCoord[1]) + "," + str(0)
                theGraph.add_node(freeCoord)

            for theOldCoord in oldField:

                fromPos = str(theOldCoord[0]) + "," + str(theOldCoord[1]) + "," + str(i-1)

                if [theOldCoord[0], theOldCoord[1]] in thisField:
                    toPos = str(theOldCoord[0]) + "," + str(theOldCoord[1]) + "," + str(0)
                    theGraph.add_edge(fromPos, toPos)
                if [theOldCoord[0] - 1, theOldCoord[1]] in thisField:
                    toPos = str(theOldCoord[0] - 1) + "," + str(theOldCoord[1]) + "," + str(0)
                    theGraph.add_edge(fromPos, toPos)
                if [theOldCoord[0] + 1, theOldCoord[1]] in thisField:
                    toPos = str(theOldCoord[0] + 1) + "," + str(theOldCoord[1]) + "," + str(0)
                    theGraph.add_edge(fromPos, toPos)
                if [theOldCoord[0], theOldCoord[1] - 1] in thisField:
                    toPos = str(theOldCoord[0]) + "," + str(theOldCoord[1] - 1) + "," + str(0)
                    theGraph.add_edge(fromPos, toPos)
                if [theOldCoord[0], theOldCoord[1] + 1] in thisField:
                    toPos = str(theOldCoord[0]) + "," + str(theOldCoord[1] + 1) + "," + str(0)
                    theGraph.add_edge(fromPos, toPos)

                if [theOldCoord[0], theOldCoord[1]] == [1,1]:
                    #theGraph.add_edge(fromPos, startPos)
                    theGraph.add_edge(fromPos, "START")
                if [theOldCoord[0], theOldCoord[1]] == [width-2,height-2]:
                    #theGraph.add_edge(fromPos, endPos)
                    theGraph.add_edge(fromPos, "FINISH")

            
            repetitionRounds = i
            print("repetitionRounds:", repetitionRounds)
            break



    #pathLength = nx.shortest_path_length(theGraph,"1,0,0","3,5,0", weight = "weight")

    #print("pathLength:", pathLength)

    #thePath = nx.shortest_path(theGraph,"1,0,0","2,5,0", weight = "weight")

    #print("thePath:", thePath)

    #print(theGraph.edges())

    #pathLength1 = nx.shortest_path_length(theGraph,startPos,endPos, weight = "weight")
    pathLength1 = nx.shortest_path_length(theGraph,startPos,"FINISH", weight = "weight")
    print(pathLength1)
    #thePath1 = nx.shortest_path(theGraph,startPos,endPos, weight = "weight")
    thePath1 = nx.shortest_path(theGraph,startPos,"FINISH", weight = "weight")
    print(thePath1)
    
    goBackStartTime2 = (pathLength1 % repetitionRounds)
    print("goBackStartTime2:", goBackStartTime2)
    newStartPos = str(width-2) + "," + str(height-1) + "," + str(goBackStartTime2)
    #pathLength2 = nx.shortest_path_length(theGraph,newStartPos,startPos, weight = "weight")
    pathLength2 = nx.shortest_path_length(theGraph,newStartPos,"START", weight = "weight")
    print(pathLength2)
    #thePath2 = nx.shortest_path(theGraph,newStartPos,startPos, weight = "weight")
    thePath2 = nx.shortest_path(theGraph,newStartPos,"START", weight = "weight")
    print(thePath2)

    goBackStartTime3 = ((pathLength1 + pathLength2) % repetitionRounds)
    print("goBackStartTime3:", goBackStartTime3)
    newStartPos = "1,0," + str(goBackStartTime3)
    #pathLength3 = nx.shortest_path_length(theGraph,newStartPos,endPos, weight = "weight")
    pathLength3 = nx.shortest_path_length(theGraph,newStartPos,"FINISH", weight = "weight")
    print(pathLength3)
    #thePath3 = nx.shortest_path(theGraph,newStartPos,endPos, weight = "weight")
    thePath3 = nx.shortest_path(theGraph,newStartPos,"FINISH", weight = "weight")
    print(thePath3)

    print("Answer")
    print(pathLength1 + pathLength2 + pathLength3)
