def nextMinute(maxGeode, stock, production, needed, timeLeft, maxNeeded, forbidden):

    decisions = []
    decisions.append(0)

    #if production[0] < maxNeeded[0]:
    if  production[0] * timeLeft + stock[0] < timeLeft * maxNeeded[0]:
        if stock[0] >= needed[0][0] and stock[1] >= needed[0][1] and stock[2] >= needed[0][2]:
            decisions.append(1)

    #if production[1] < maxNeeded[1]:
    if  production[1] * timeLeft + stock[1] < timeLeft * maxNeeded[1]:
        if stock[0] >= needed[1][0] and stock[1] >= needed[1][1] and stock[2] >= needed[1][2]:
            decisions.append(2)

    #if production[2] < maxNeeded[2]:
    if  production[2] * timeLeft + stock[2] < timeLeft * maxNeeded[2]:
        if stock[0] >= needed[2][0] and stock[1] >= needed[2][1] and stock[2] >= needed[2][2]:
            decisions.append(3)

    if stock[0] >= needed[3][0] and stock[1] >= needed[3][1] and stock[2] >= needed[3][2]:
        decisions.append(4)

    #if len(decisions) == 4 and production[3] == 0:
    #    decisions = [1,2,3]
    if len(decisions) == 4 and production[2] == 0:
        decisions = [1,2,3]

    if 4 in decisions:
        decisions = [4]

    #if ((timeLeft * (timeLeft+1)) // 2) + production[2] + stock[2] < needed[3][2]:
        #decisions = [0]

    #if ((timeLeft * (timeLeft+1)) // 2) + production[3]*timeLeft <= maxGeode:
    #    return maxGeode

    #if needed[0][0] > needed[1][0] and production[1] == 0:
    #    if stock[0] > needed[1][0]:
    #        decisions = [1]
    #elif needed[0][0] < needed[1][0] and production[1] == 0:
    #    if stock[0] > needed[0][0]:
    #        decisions = [2]

    if (stock[0] > max(needed[0][0], needed[1][0])) and (production[1] == 0):
        decisions = [1,2]

        
    for i in forbidden:
        if i in decisions:
            decisions.remove(i)

    startSto = stock.copy()
    startProd = production.copy()

    for thisDecision in decisions:

        stock = startSto.copy()
        production = startProd.copy()

        #Nothing
        if thisDecision == 0:

            forbidden = decisions.copy()
            forbidden.remove(0)

            stock[0] += production[0]
            stock[1] += production[1]
            stock[2] += production[2]
            stock[3] += production[3]

            if timeLeft - 1 == 0:
                return max(maxGeode, stock[3])
            else:
                maxGeode = nextMinute(maxGeode, stock.copy(), production.copy(), needed, timeLeft - 1, maxNeeded, forbidden)

        #BuildOre
        elif thisDecision == 1:

            forbidden = []

            stock[0] -= needed[0][0]
            stock[1] -= needed[0][1]
            stock[2] -= needed[0][2]
            production[0] += 1

            stock[0] += production[0] -1
            stock[1] += production[1]
            stock[2] += production[2]
            stock[3] += production[3]

            if timeLeft - 1 == 0:
                return max(maxGeode, stock[3])
            else:
                maxGeode = nextMinute(maxGeode, stock.copy(), production.copy(), needed, timeLeft - 1, maxNeeded, forbidden)

        #BuildClay
        elif thisDecision == 2:

            forbidden = []

            stock[0] -= needed[1][0]
            stock[1] -= needed[1][1]
            stock[2] -= needed[1][2]
            production[1] += 1

            stock[0] += production[0]
            stock[1] += production[1] -1
            stock[2] += production[2]
            stock[3] += production[3]

            if timeLeft - 1 == 0:
                return max(maxGeode, stock[3])
            else:
                maxGeode = nextMinute(maxGeode, stock.copy(), production.copy(), needed, timeLeft - 1, maxNeeded, forbidden)

        #BuildObsidian
        elif thisDecision == 3:

            forbidden = []

            stock[0] -= needed[2][0]
            stock[1] -= needed[2][1]
            stock[2] -= needed[2][2]
            production[2] += 1

            stock[0] += production[0]
            stock[1] += production[1]
            stock[2] += production[2] -1
            stock[3] += production[3]

            if timeLeft - 1 == 0:
                return max(maxGeode, stock[3])
            else:
                maxGeode = nextMinute(maxGeode, stock.copy(), production.copy(), needed, timeLeft - 1, maxNeeded, forbidden)

        #BuildGeode
        elif thisDecision == 4:

            forbidden = []

            stock[0] -= needed[3][0]
            stock[1] -= needed[3][1]
            stock[2] -= needed[3][2]
            production[3] += 1

            stock[0] += production[0]
            stock[1] += production[1]
            stock[2] += production[2]
            stock[3] += production[3] -1

            if timeLeft - 1 == 0:
                return max(maxGeode, stock[3])
            else:
                maxGeode = nextMinute(maxGeode, stock.copy(), production.copy(), needed, timeLeft - 1, maxNeeded, forbidden)


    return maxGeode

if __name__ == '__main__':

    f=open("Task19.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("Blueprint ","")
        i = i.replace(": Each ore robot costs ",",")
        i = i.replace(" ore. Each clay robot costs ",",")
        i = i.replace(" ore. Each obsidian robot costs ",",")
        i = i.replace(" ore and ",",")
        i = i.replace(" clay. Each geode robot costs ", ",")
        i = i.replace(" ore and ", ",")
        i = i.replace(" obsidian.", "")
        i = i.split(",")
        theInput.append(i)
    f.close()

    needed = [[],[],[],[]]

    thisID = 1
    #totalQuality = 0
    totalQuality = 1

    for i in theInput:
        needed[0] = [int(i[1]), 0, 0]
        needed[1] = [int(i[2]), 0, 0]
        needed[2] = [int(i[3]), int(i[4]), 0]
        needed[3] = [int(i[5]), 0, int(i[6])]

        startProductions = [1,0,0,0]

        startStock = [0,0,0,0]

        #totalTimes = 24
        totalTimes = 32

        theMaxGeode = 0

        maxOreNeeded = max(needed[0][0], needed[1][0], needed[2][0], needed[3][0])
        maxClayNeeded = max(needed[0][1], needed[1][1], needed[2][1], needed[3][1])
        maxObsidianNeeded = max(needed[0][2], needed[1][2], needed[2][2], needed[3][2])

        maxNeeded = [maxOreNeeded,maxClayNeeded,maxObsidianNeeded]

        theMaxGeode = nextMinute(theMaxGeode, startStock.copy(), startProductions.copy(), needed, totalTimes, maxNeeded, [])

        #totalQuality += theMaxGeode * thisID
        totalQuality *= theMaxGeode

        print(theMaxGeode)

        thisID += 1

    print("Answer")
    print(totalQuality)



