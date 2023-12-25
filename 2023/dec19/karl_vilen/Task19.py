import re

def checkValue(theLetter, intervals):

    if theLetter == "A":
        thisSpan = ((intervals["maxX"] - intervals["minX"])+1) * ((intervals["maxM"] - intervals["minM"])+1) * ((intervals["maxA"] - intervals["minA"])+1) * ((intervals["maxS"] - intervals["minS"])+1)
        return thisSpan

    elif theLetter == "R":
        return 0

def checkCombination(allInstr, currentInstr, intervals):

    thisInstr = allInstr[currentInstr]
    combinationValue = 0
    nextInterval = None 

    for i in thisInstr:

        if nextInterval == None:
            nextInterval = intervals.copy()

        if ":" in i:

            theIntervalLetter = i[0]
            sendTo = i.split(":")[1]
            theValue = int(re.search("[0-9]+", i)[0])
            
            if theIntervalLetter == "x":

                if ">" in i:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["minX"] = theValue + 1
                    nextInterval["maxX"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)
                else:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["maxX"] = theValue - 1
                    nextInterval["minX"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)

            elif theIntervalLetter == "m":

                if ">" in i:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["minM"] = theValue + 1
                    nextInterval["maxM"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)
                else:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["maxM"] = theValue - 1
                    nextInterval["minM"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)

            elif theIntervalLetter == "a":

                if ">" in i:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["minA"] = theValue + 1
                    nextInterval["maxA"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)
                else:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["maxA"] = theValue - 1
                    nextInterval["minA"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)

            elif theIntervalLetter == "s":

                if ">" in i:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["minS"] = theValue + 1
                    nextInterval["maxS"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)
                else:
                    aNewInterval = nextInterval.copy()
                    aNewInterval["maxS"] = theValue - 1
                    nextInterval["minS"] = theValue
                    if sendTo in "AR":
                        combinationValue += checkValue(sendTo, aNewInterval)
                    else:
                        combinationValue += checkCombination(allInstr, sendTo, aNewInterval)

        else:

            if i == "A":
                thisSpan = ((nextInterval["maxX"] - nextInterval["minX"])+1) * ((nextInterval["maxM"] - nextInterval["minM"])+1) * ((nextInterval["maxA"] - nextInterval["minA"])+1) * ((nextInterval["maxS"] - nextInterval["minS"])+1)
                combinationValue += thisSpan
            elif i == "R":
                combinationValue += 0
            else:
                combinationValue += checkCombination(allInstr, i, nextInterval.copy())

    return combinationValue

if __name__ == '__main__':

    f=open("Task19.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        theInput.append(i)
    f.close()

    spaceFound = False
    instructions = dict()
    gears = []

    for i in theInput:

        if spaceFound == False:
            if len(i) == 0:
                spaceFound = True
            else:
                a = i.replace("}","")
                a = a.split("{")

                theName = a[0]
                instructions[theName] = a[1].split(",")

        else:
            a = i.replace("{", "")
            a = a.replace("}", "")
            a = a.replace("x=", "")
            a = a.replace("m=", "")
            a = a.replace("a=", "")
            a = a.replace("s=", "")
            a = a.split(",")

            gears.append([int(a[0]),int(a[1]),int(a[2]),int(a[3])])

    intervals = dict()
    intervals["minX"] = 1
    intervals["minM"] = 1
    intervals["minA"] = 1
    intervals["minS"] = 1

    intervals["maxX"] = 4000
    intervals["maxM"] = 4000
    intervals["maxA"] = 4000
    intervals["maxS"] = 4000

    totalValue = checkCombination(instructions, "in", intervals.copy())

    print(totalValue)
