if __name__ == '__main__':

    f=open("Task5.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    lowId = 1000
    maxId = 0

    allIds = []

    for i in theInput:

        thisRow = 0
        thisCol = 0

        for j in range(0,7):
            thisInput = i[j]

            if thisInput == "B":
                thisRow += 2 ** (6-j)

        for j in range(7,10):
            thisInput = i[j]

            if thisInput == "R":
                thisCol += 2 ** (9-j)

        thisId = thisRow * 8 + thisCol
        lowId = min(lowId, thisId)
        maxId = max(maxId, thisId)

        allIds.append(thisId)

    print("Answer1")
    print(maxId)

    print("Answer2")
    for i in range(lowId,maxId):
        if i not in allIds:
            print(i)