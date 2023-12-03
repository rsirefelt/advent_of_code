if __name__ == '__main__':

    f=open("Task3.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        theInput.append(list(i))
    f.close()

    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    totalSum = 0

    width = len(theInput[0])

    for indexI, i in enumerate(theInput):

        for indexJ, j in enumerate(i):

            if j == "*":

                adjacentNumbers = []

                for k in range(-1,2,1):
                    for m in range(-1,2,1):

                        if k == 0 and m == 0:
                            continue

                        if theInput[indexI+k][indexJ+m] in numbers:

                            thisNumber = theInput[indexI+k][indexJ+m]
                            theInput[indexI+k][indexJ+m] = "."

                            offset = 0
                            foundDot = False
                            while foundDot == False:

                                offset -= 1
                                if indexJ+m+offset < 0:
                                    foundDot = True
                                    continue

                                if theInput[indexI+k][indexJ+m+offset] in numbers:
                                    thisNumber = theInput[indexI+k][indexJ+m+offset] + thisNumber
                                    theInput[indexI+k][indexJ+m+offset] = "."
                                else: 
                                    foundDot = True

                            offset = 0
                            foundDot = False
                            while foundDot == False:

                                offset += 1

                                if indexJ+m+offset >= width:
                                    foundDot = True
                                    continue

                                if theInput[indexI+k][indexJ+m+offset] in numbers:
                                    thisNumber = thisNumber + theInput[indexI+k][indexJ+m+offset] 
                                    theInput[indexI+k][indexJ+m+offset] = "."
                                else: 
                                    foundDot = True

                            adjacentNumbers.append(int(thisNumber))

                if len(adjacentNumbers) == 2:

                    totalSum += adjacentNumbers[0] * adjacentNumbers[1]

    print(totalSum)

