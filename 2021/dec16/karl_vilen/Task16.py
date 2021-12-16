totalVersion = 0

def hexToBinString(theHex):
    a = str(bin(int(theHex, base=16)))
    a = a[2:]
    theLength = 4-len(a)
    for i in range((theLength)):
        a = "0" + a
    return a

def literalToValue(binaryString):
    continueRead = True
    pointer = 0
    thisBinary = ""
    while continueRead == True:
        if binaryString[pointer] == "0":
            continueRead = False
        thisBinary += binaryString[pointer+1:pointer+5]
        pointer += 5
    thisValue = int(thisBinary,2)

    return [thisValue, pointer]

def evaluate(theOperator, values):

    if theOperator == "000":
        theAnswer = sum(values)
    elif theOperator == "001":
        theAnswer = 1
        for i in values:
            theAnswer *= i
    elif theOperator == "010":
        theAnswer = min(values)
    elif theOperator == "011":
        theAnswer = max(values)
    elif theOperator == "101":
        theAnswer = 0
        if values[0] > values[1]:
            theAnswer = 1
    elif theOperator == "110":
        theAnswer = 0
        if values[0] < values[1]:
            theAnswer = 1
    elif theOperator == "111":
        theAnswer = 0
        if values[0] == values[1]:
            theAnswer = 1

    return theAnswer


def operator(binaryString):  

    theVersion = binaryString[:3]
    global totalVersion
    totalVersion += int(theVersion,2)
    theOperator = binaryString[3:6]
    pointer = 6

    if theOperator == "100":
        theBinaryString = binaryString[pointer:]
        [a,b] = literalToValue(theBinaryString)
        pointer += b
        return [a, pointer]
    else:
        theOperatorID = binaryString[pointer]
        pointer += 1
        if theOperatorID == "1":
            amountOfMessages = int(binaryString[pointer: pointer + 11],2)
            pointer += 11
            theValues = []

            for i in range(amountOfMessages):

                [theValue, movePointer] = operator(binaryString[pointer:])
                theValues.append(theValue)
                pointer += movePointer

            evaluationAnswer = evaluate(theOperator, theValues)
            return [evaluationAnswer, pointer]
        else:
            thisBinaryMessage = binaryString[pointer:pointer+15]
            pointer += 15
            messageLength = int(thisBinaryMessage,2)
            theMessageOriginal = binaryString[pointer:pointer+messageLength]
            lengthInvestigated = 0
            theValues = []

            while lengthInvestigated < messageLength:

                theMessage = theMessageOriginal[lengthInvestigated:]
                [theValue, movePointer] = operator(theMessage)
                lengthInvestigated += movePointer
                theValues.append(theValue)
                pointer += movePointer

            evaluationAnswer = evaluate(theOperator, theValues)
            return [evaluationAnswer, pointer]


if __name__ == '__main__':

    f=open("Task16.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput = i
    f.close()

    fullBinaryMessage = ""

    for i in theInput:
        fullBinaryMessage += hexToBinString(i)

    thePointer = 0

    while thePointer < len(fullBinaryMessage):

        [theValue, toMove] = operator(fullBinaryMessage[thePointer:])

        if "1" in fullBinaryMessage[thePointer:]:
            break

        thePointer += toMove

    print("Done")
    print(totalVersion)
    print("Part2")
    print(theValue)
