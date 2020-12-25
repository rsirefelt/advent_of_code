if __name__ == '__main__':
    
    f=open("Task23.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput = list(i)
    f.close()

    allCups = []

    listLength = len(theInput)

    for i in range(listLength):
        allCups.append([0,0])
    allCups.append([0,0])

    reqLength = 1000000 + 1

    for i in range(10,reqLength):
        allCups.append([0,0])

    for i in range(1,listLength-1):
        allCups[int(theInput[i])][0] = int(theInput[i-1])
        allCups[int(theInput[i])][1] = int(theInput[i+1])

    allCups[10][0] = int(theInput[-1])
    allCups[10][1] = 11

    for i in range(11,reqLength):
        allCups[i][0] = i-1
        allCups[i][1] = i+1

    allCups[int(theInput[0])][1] = int(theInput[1])

    allCups[int(theInput[0])][0] = len(allCups)
    allCups[len(allCups)-1][1] = int(theInput[0])

    allCups[int(theInput[-1])][0] = int(theInput[-2])
    allCups[int(theInput[-1])][1] = len(theInput)+1

    currentCup = int(theInput[0])

    theAnswer = []
    nextPointer = 1
    for i in range(9):
        theAnswer.append(nextPointer)
        nextPointer = allCups[nextPointer][1]

    listLength = len(allCups)-1

    for i in range(10000000):

        toMove1 = allCups[currentCup][1]
        after = toMove1
        toMove2 = allCups[after][1]
        after2 = toMove2
        toMove3 = allCups[after2][1]
        nextCup = allCups[toMove3][1]

        allMove = [toMove1, toMove2, toMove3]

        destination = currentCup
        while True:
            destination -= 1
            if destination <= 0:
                destination = listLength
            if destination not in allMove:
                break

        allCups[currentCup][1] = nextCup

        connectAgainInto = allCups[destination][1]

        allCups[destination][1] = allMove[0]
        allCups[allMove[0]][0] = destination

        allCups[allMove[0]][1] = allMove[1]
        allCups[allMove[1]][0] = allMove[0]

        allCups[allMove[1]][1] = allMove[2]
        allCups[allMove[2]][0] = allMove[1]

        allCups[allMove[2]][1] = connectAgainInto
        allCups[connectAgainInto][0] = allCups[allMove[2]][1]

        theNext = 1

        result = []

        for j in range(9):
            result.append(theNext)
            theNext = allCups[theNext][1]

        currentCup = nextCup

        if i % 100000 == 0:
            print(i)

    print("Done")

    a = allCups[1][1]
    b = allCups[allCups[1][1]][1]

    print(a)
    print(b)
    print(a*b)