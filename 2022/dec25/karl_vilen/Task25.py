def fromFiveBase (inString):

    index = len(inString)
    valueRow = 0
    for j in inString:

        baseValue = 5 ** (index-1)

        if j == "2" or j == "1" or j == "0":
            thisValue = baseValue * int(j)
        elif j == "-":
            thisValue = baseValue * -1
        elif j == "=":
            thisValue = baseValue * -2
        index -= 1

        valueRow += thisValue

    return valueRow

if __name__ == '__main__':

    f=open("Task25.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    totalSum = 0
    
    for i in theInput:
        
        totalSum += fromFiveBase(i)

    theString = list("22222222222222222222222222222222")

    theIndex = 0
    hasFoundFirstNumber = False
    while theIndex < len(theString):

        currentString = ""
        for j in theString:
            currentString += j

        if fromFiveBase(currentString) > totalSum:

            if hasFoundFirstNumber == True:
                if theString[theIndex] == "2":
                    theString[theIndex] = "1"
                elif theString[theIndex] == "1":
                    theString[theIndex] = "0"
                elif theString[theIndex] == "0":
                    theString[theIndex] = "-"
                elif theString[theIndex] == "-":
                    theString[theIndex] = "="
                elif theString[theIndex] == "=":
                    theIndex += 1

            elif hasFoundFirstNumber == False:
                if theString[theIndex] == "2":
                    theString[theIndex] = "1"
                elif theString[theIndex] == "1":
                    theString[theIndex] = "0"
                elif theString[theIndex] == "0":
                    theIndex += 1

        elif fromFiveBase(currentString) == totalSum:
            print("Answer")
            print(currentString)
            break
        else:

            if hasFoundFirstNumber == False:
                if theString[theIndex] == "1":
                    theString[theIndex] = "2"
                    hasFoundFirstNumber = True
                    theIndex += 1
                elif theString[theIndex] == "0":
                    theString[theIndex] = "1"
                    hasFoundFirstNumber = True
                    theIndex += 1
            else:
                if theString[theIndex] == "1":
                    theString[theIndex] = "2"
                    theIndex += 1
                elif theString[theIndex] == "0":
                    theString[theIndex] = "1"
                    theIndex += 1
                elif theString[theIndex] == "-":
                    theString[theIndex] = "0"
                    theIndex += 1
                elif theString[theIndex] == "=":
                    theString[theIndex] = "-"
                    theIndex += 1
