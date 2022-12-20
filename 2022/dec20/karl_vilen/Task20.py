if __name__ == '__main__':

    f=open("Task20.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(int(i))
    f.close()

    answerList = theInput.copy()
    listLength = len(answerList)

    listIDs = []

    decKey = 811589153

    for iIndex, i in enumerate(answerList):

        if i == 0:
            zeroID = iIndex
        listIDs.append([i*decKey,iIndex])

    for mixes in range(0,10):

        for i in range(0,len(listIDs)):

            for j in range(0,len(listIDs)):

                if listIDs[j][1] == i:
                    startPos = j
                    theValue = listIDs[j][0]
                    break
            
            newPos = (startPos + theValue)
            newPos = newPos % (listLength-1)

            listIDs.remove([theValue,i])
            listIDs.insert(newPos,[theValue,i])

    zeroPos = listIDs.index([0, zeroID])

    pos1 = (zeroPos + 1000) % listLength
    pos2 = (zeroPos + 2000) % listLength
    pos3 = (zeroPos + 3000) % listLength

    answer = listIDs[pos1][0] + listIDs[pos2][0] + listIDs[pos3][0]

    print("Answer")
    print(answer)



