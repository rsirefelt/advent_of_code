import math

if __name__ == '__main__':

    f=open("Task20.txt","r")
    lines=f.readlines()
    theInput = []

    cValues = dict()
    cTypes = dict()
    cTo = dict()
    cFrom = dict()

    for i in lines:
        i = i.strip()
        i = i.replace(" ","")
        i = i.split("->")
        cValues[i[0][1:]] = 0
        cTypes[i[0][1:]] = i[0][0]
        cTo[i[0][1:]] = i[1].split(",")
        cFrom[i[0][1:]] = dict()
        theInput.append(i)
    f.close()

    cTypes["button"] = "button"
    cValues["rx"] = 0
    cTypes["rx"] = "rx"

    for i in theInput:

        for j in i[1].split(","):

            if cTypes[j] == "&":

                cFrom[j][i[0][1:]] = 0

    lows = 0
    highs = 0

    toInvestigate = []

    lowkd = 0
    lowzf = 0
    lowvg = 0
    lowgs = 0
    totalFound = 0
    breakAll = False

    for counter in range(1000000):

        toInvestigate = ["button"]

        nextToInvestigate = []

        while len(toInvestigate) > 0:

            for i in toInvestigate:

                if cTypes[i] == "button":
                    nextToInvestigate.append("roadcaster")
                    cValues["roadcaster"] = 0
                    lows += 1

                elif cTypes[i] == "b":

                    for j in cTo["roadcaster"]:
                        if cTypes[j] == "%":
                            nextToInvestigate.append(j)
                            lows+= 1
                            if cValues[j] == 1:
                                cValues[j] = 0
                            else:
                                cValues[j] = 1
                        elif cTypes[j] == "&":
                            nextToInvestigate.append(j)
                            lows+= 1
                            cFrom[j]["roadcaster"] = 0
                        elif cTypes[j] == "rx":
                            lows+= 1


                elif cTypes[i] == "%":

                    for j in cTo[i]:

                        if cTypes[j] == "%":
                            if cValues[i] == 1:
                                highs += 1
                            else:
                                lows+= 1
                                cValues[j] = (cValues[j]+1)%2
                                nextToInvestigate.append(j)
                        elif cTypes[j] == "&":
                            if cValues[i] == 1:
                                highs += 1
                            else:
                                lows+= 1
                            cFrom[j][i] = cValues[i]
                            nextToInvestigate.append(j)
                        elif cTypes[j] == "rx":
                            if cValues[i] == 1:
                                highs += 1
                            else:
                                lows+= 1

                elif cTypes[i] == "&":

                    noOfInputs = len(cFrom[i].keys())
                    theSum = 0

                    for j in cFrom[i].keys():
                        theSum += cFrom[i][j]

                    toSend = 1

                    if theSum == noOfInputs:
                        toSend = 0
                    
                    for j in cTo[i]:

                        if cTypes[j] == "%":
                            if toSend == 1:
                                highs += 1
                            else:
                                lows += 1
                                nextToInvestigate.append(j)
                                cValues[j] = (cValues[j]+1)%2

                        elif cTypes[j] == "&":
                            if j == "rg" and toSend == 1:
                                if i == "gs":
                                    if lowgs == 0:
                                        lowgs = counter
                                        totalFound += 1
                                elif i == "kd":
                                    if lowkd == 0:
                                        lowkd = counter
                                        totalFound += 1
                                elif i == "vg":
                                    if lowvg == 0:
                                        lowvg = counter
                                        totalFound += 1
                                elif i == "zf":
                                    if lowzf == 0:
                                        lowzf = counter
                                        totalFound += 1

                                if totalFound == 4:
                                    breakAll = True
                                    break

                            if toSend == 1:
                                highs += 1
                            else:
                                lows+= 1
                            cFrom[j][i] = toSend
                            nextToInvestigate.append(j)

                        elif cTypes[j] == "rx":
                            if toSend == 1:
                                highs += 1
                            else:
                                lows+= 1

                if breakAll:
                    break

            if breakAll:
                break

            toInvestigate = nextToInvestigate.copy()
            nextToInvestigate = []

        if  breakAll:
            break

    print(math.lcm(lowgs+1,lowkd+1,lowvg+1,lowzf+1))