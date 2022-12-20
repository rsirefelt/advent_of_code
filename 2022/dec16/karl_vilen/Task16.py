import networkx as nx
import itertools

if __name__ == '__main__':

    f=open("Task16.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("tunnels","tunnel")
        i = i.replace("valves","valve")
        i = i.replace("leads","lead")
        i = i.replace("; tunnel lead to valve ",", ")
        i = i.replace(" has flow rate=",", ")
        i = i.replace("Valve ", "")
        i = i.split(", ")
        theInput.append(i)
    f.close()

    flowRates = dict()
    withFlows = dict()
    connected = dict()

    theGraph = nx.Graph()

    for i in theInput:
        flowRates[i[0]] = int(i[1])

        if int(i[1]) != 0:
            withFlows[i[0]] = int(i[1])


        theGraph.add_node(i[0])

    for i in theInput:
        for j in range(2,len(i)):
            theGraph.add_edge(i[0], i[j])

    tunnelsToVisit = withFlows.keys()
    tunnelsToVisit = list(tunnelsToVisit)

    maxPressureDrop = 0

    allTravelDists = dict()

    withFlowsandAA = list(withFlows.copy())
    withFlowsandAA.append("AA")

    for i in withFlowsandAA:
        for j in withFlowsandAA:

            if i == j:
                continue

            pathLength = nx.shortest_path_length(theGraph,i,j, weight = "weight")
            allTravelDists[i+j] = pathLength

    toMultiply = len(tunnelsToVisit)

    lastMaxPressureDrop = -1
    maxPressureDrop = 0

    reachedMaxStrings = []

    pressureDrops = dict()

    for c in range(1, 8):

        reachedMax = 0
        thisPermMax = 0

        for i in itertools.permutations(tunnelsToVisit,c):

            fromTunnel = "AA"
            timeLeft = 26
            thisPressureDrop = 0

            thisList = list(i)
            thisList = sorted(thisList)
            permString = ','.join(str(m) for m in thisList)

            for j in i:

                searchString = fromTunnel + j
                pathLength = allTravelDists[searchString]
                timeLeft -= pathLength

                if timeLeft <= 0:
                    reachedMax += 1
                    buffer = ','.join(str(m) for m in i)
                    reachedMaxStrings.append(buffer)
                    break

                thisPressureDrop += withFlows[j] * max((timeLeft - 1),0)
                maxPressureDrop = max(maxPressureDrop, thisPressureDrop)
                thisPermMax = max(thisPermMax, thisPressureDrop)

                if timeLeft <= 0:
                    reachedMax +=1
                    buffer = ','.join(str(m) for m in i)
                    reachedMaxStrings.append(buffer)
                    break

                timeLeft -= 1
                fromTunnel = j

            if permString not in pressureDrops.keys():
                pressureDrops[permString] = thisPressureDrop
            else:
                pressureDrops[permString] = max(thisPressureDrop,pressureDrops[permString])


        if lastMaxPressureDrop == maxPressureDrop:
            break
        else:
            lastMaxPressureDrop = maxPressureDrop

    sortedTunnels = sorted(tunnelsToVisit)
    highestDrop = 0
    maxLength = 8

    totalIterations = 0
    nextCombination = 0

    for c in range(1, maxLength):

        print("c:", c)

        for humanTunnels in itertools.combinations(sortedTunnels,c):

            totalIterations += 1

            elephantTunnels = sortedTunnels.copy()

            for i in humanTunnels:
                elephantTunnels.remove(i)

            for c2 in range(1, maxLength):

                for elephant2 in itertools.combinations(elephantTunnels,c2):

                    totalIterations += 1

                    tun1 = sorted(humanTunnels)
                    tun2 = sorted(elephant2)

                    permString1 = ','.join(str(m) for m in tun1)
                    permString2 = ','.join(str(m) for m in tun2)

                    pressure1 = 0
                    pressure2 = 0

                    if permString1 in pressureDrops.keys():
                        pressure1 = pressureDrops[permString1]
                    if permString2 in pressureDrops.keys():
                        pressure2 = pressureDrops[permString2]

                    if highestDrop < pressure1 + pressure2:
                        highestDrop = pressure1 + pressure2

    print("Answer")
    print(highestDrop)
