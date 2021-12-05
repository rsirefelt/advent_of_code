if __name__ == '__main__':

    f=open("Task4.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("  "," ")
        i = i.replace(" ",",")
        i = i.split(",")
        theInput.append(i)
    f.close()

    numbers = theInput[0]

    for i in theInput:
        if len(i) == 6:
            i.remove("")

    boards = []

    currentBoard = 0

    boards.append([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])

    for i in range(2,len(theInput)):
        if (i - 1) % 6 == 0:
            currentBoard += 1
            boards.append([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])
            continue

        for j in range(0,5):
            thisY = i-2 - currentBoard*6
            boards[currentBoard][j][thisY] = int(theInput[i][j])

    theBingos = []

    for i in numbers:

        for jIndex, j in enumerate(boards):

            if jIndex in theBingos:
                continue

            for k in range(0,5):
                for l in range(0,5):
                    if j[k][l] == int(i):
                        j[k][l] = -2


            for k in range(0,5):
                bingo = True
                for l in range(0,5):
                    if j[k][l] != -2:
                        bingo = False
                        break

                if bingo == True:
                    winnerNumber = int(i)
                    winnerBoard = jIndex
                    break


            for k in range(0,5):
                if bingo == True:
                    break
                bingo = True
                for l in range(0,5):
                    if j[l][k] != -2:

                        bingo = False
                        break

                if bingo == True:
                    winnerNumber = int(i)
                    winnerBoard = jIndex
                    break


            if bingo == True:
                theBingos.append(jIndex)

        if len(theBingos) == len(boards):
            break

    theSum = 0

    for i in range(0,5):
        for j in range(0,5):
            if boards[winnerBoard][i][j] != -2:
                theSum += boards[winnerBoard][i][j]

    print("Done")

    print(theSum*winnerNumber)
