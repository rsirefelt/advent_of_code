if __name__ == '__main__':

    f=open("Task3.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(i.rstrip())
    f.close()

    width = len(theInput[0])
    height = len(theInput)

    gamma = ""
    epsilon = ""

    for i in range(width):
        zeros = 0
        ones = 0
        for j in range(height):
            if theInput[j][i] == "1":
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    theGamma = (int(gamma, base=2))
    theEpsilon = (int(epsilon, base=2))

    print("Done1")
    print(theGamma*theEpsilon)

    candidates = ([list(range(height)),list(range(height))])

    for i in range(width):

        theSum = [0,0]

        for kIndex, k in enumerate(candidates):
            for j in k:
                if theInput[j][i] == "1":
                    theSum[kIndex]+=(kIndex*-2)+1
                else:
                    theSum[kIndex]+=(kIndex*2)-1

        toRemove = ([],[])

        for kIndex, k in enumerate(candidates):

            if len(k) != 1:

                for j in k:

                    if (theSum[kIndex]*((kIndex*-2)+1)) >= 0:
                        if theInput[j][i] == str(kIndex):
                            toRemove[kIndex].append(j)
                    else:
                        if theInput[j][i] == str((kIndex*-1)+1):
                            toRemove[kIndex].append(j)

            for l in toRemove[kIndex]:
                k.remove(l)

        if len(candidates[0]) == 1 and len(candidates[1]) == 1:
            break

    oxygen = (int(theInput[candidates[0][0]], base=2))
    co2 = (int(theInput[candidates[1][0]], base=2))

    print("Done2")
    print(oxygen*co2)


