prevAmount = 25
theInput = []

def calcPairSums(startI):
    sums = []

    for i in range(startI, prevAmount+startI):
        for j in range(i+1, prevAmount+startI):
            sums.append(theInput[i]+theInput[j])

    return sums

if __name__ == '__main__':

    pairSums = []

    f=open("Task9.txt","r")
    lines=f.readlines()

    for i in lines:
        i= i.rstrip()
        theInput.append(int(i))
    f.close()

    for i in range(prevAmount, len(theInput)):
        pairSums = calcPairSums(i - prevAmount)
        if theInput[i] not in pairSums:
            weakness = theInput[i]
            break

    answerI = 0
    answerJ = 0

    for i in range(0, len(theInput)):
        theSum = theInput[i]
        for j in range(i+1, len(theInput)):
            theSum += theInput[j]
            if (theSum) > weakness:
                break
            elif theSum == weakness:
                answerI = i
                answerJ = j
                break
        if answerI != answerJ:
            break

    theMin = 99999999999999
    theMax = 0

    for i in range(answerI, answerJ):
        theMin = min(theMin, theInput[i])
        theMax = max(theMax, theInput[i])

    print("Done")
    print("Task 1")
    print(weakness)
    print("Task 2")
    print(theMin+theMax)
