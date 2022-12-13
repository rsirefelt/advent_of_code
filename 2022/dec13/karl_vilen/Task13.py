def checkCorrectOrder(theRow1, theRow2):

    if isinstance(theRow1, int) == True:
        theRow1 = [theRow1]
    if isinstance(theRow2, int) == True:
        theRow2 = [theRow2]

    maxLength = max(len(theRow1), len(theRow2))

    for i in range(0,maxLength):

        if i >= len(theRow1):
            return True, True
        elif i >= len(theRow2):
            return True, False

        if isinstance(theRow1[i],list) == True or isinstance(theRow2[i], list) == True:
            hasDetermined, value = checkCorrectOrder(theRow1[i],theRow2[i])
            if hasDetermined == True:
                return True, value

        elif theRow1[i] < theRow2[i]:
            return True, True
        elif theRow1[i] > theRow2[i]:
            return True, False

    return False, False


if __name__ == '__main__':

    f=open("Task13.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    rightIndexes = []

    for i in range(0,len(theInput),3):
        row1 = eval(theInput[i])
        row2 = eval(theInput[i+1])

        isOrdered = checkCorrectOrder(row1, row2)

        if isOrdered[1] == True:
            rightIndexes.append(i//3 + 1)

    print("Answer 1")
    print(sum(rightIndexes))

    newInput = []
    newInput.append("[[2]]")
    newInput.append("[[6]]")

    for i in theInput:
        if i == "":
            continue
        newInput.append(i)

    i = 0
    while i < len(newInput)-1:

        row1 = eval(newInput[i])
        row2 = eval(newInput[i+1])
        isOrdered = checkCorrectOrder(row1,row2)

        if isOrdered[1] == False:
            buffer = newInput[i]
            newInput[i] = newInput[i+1]
            newInput[i+1] = buffer
            i = max(i-2,-1)
        i += 1

    answer2 = 1
    for i in range(len(newInput)):
        if newInput[i] == "[[2]]":
            answer2 *= (i+1)
        elif newInput[i] == "[[6]]":
            answer2 *= (i+1)

    print("Answer 2")
    print(answer2)
