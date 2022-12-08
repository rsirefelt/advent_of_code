if __name__ == '__main__':

    f=open("Task8.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    height = len(theInput)
    width = len(theInput[0])

    totalVisible = 0

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):

            if iIndex == 0 or jIndex == 0 or iIndex == height-1 or jIndex == width-1:
                totalVisible += 1
                continue

            visible = True
            invisibility = 0

            for k in range(0,iIndex):
                if theInput[k][jIndex] >= j:
                    invisibility += 1
                    break

            for k in range(iIndex+1,width):
                if theInput[k][jIndex] >= j:
                    invisibility += 1
                    break

            for k in range(0,jIndex):
                if theInput[iIndex][k] >= j:
                    invisibility += 1
                    break

            for k in range(jIndex+1,height):
                if theInput[iIndex][k] >= j:
                    invisibility += 1
                    break

            if invisibility < 4:
                totalVisible += 1


    print("Answer")
    print(totalVisible)

    maxScore = 0

    for iIndex, i in enumerate(theInput):
        for jIndex, j in enumerate(i):

            scores = [0,0,0,0]

            thisScore = 0
            for k in range(iIndex-1,-1,-1):
                thisScore += 1
                if theInput[k][jIndex] >= j:
                    break
            scores[0] = thisScore

            thisScore = 0
            for k in range(iIndex+1, width):
                thisScore += 1
                if theInput[k][jIndex] >= j:                    
                    break
            scores[1] = thisScore

            thisScore = 0
            for k in range(jIndex-1, -1,-1):
                thisScore += 1
                if theInput[iIndex][k] >= j:
                    break
            scores[2] = thisScore

            thisScore = 0
            for k in range(jIndex+1,height):
                thisScore += 1
                if theInput[iIndex][k] >= j:
                    break
            scores[3] = thisScore

            theScore = scores[0] * scores[1] * scores[2] * scores[3]

            maxScore = max(maxScore,theScore)


    print(maxScore)
