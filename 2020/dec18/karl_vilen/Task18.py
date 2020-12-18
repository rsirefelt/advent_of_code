if __name__ == '__main__':

    f=open("Task18.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace(" ","")
        theInput.append(list(i))
    f.close()

    answer = 0

    for i in theInput:

        thisLine = i

        while (True):

            if thisLine.count("(") > 0:
                startP = len(thisLine) - 1 - thisLine[::-1].index("(")
                endP = startP + thisLine[startP:].index(")")

                toCompute = thisLine[startP+1:endP]
                thisString = str("".join(toCompute))
                operators = []

                for j in thisString:
                    if j == "+":
                        operators.append("+")
                    elif j == "*":
                        operators.append("*")

                thisString = thisString.replace("+","*")
                thisString = thisString.split("*")

                lowerIndex = 0

                for j in operators:
                    if j == "+":
                        thisAmount = int(thisString[lowerIndex+1]) + int(thisString[lowerIndex])
                        thisString[lowerIndex] = str(thisAmount)
                        thisString.pop(lowerIndex+1)
                    else:
                        lowerIndex += 1

                thisAmount = 1
                for j in thisString:
                    thisAmount *= int(j)

                for j in range(endP+1-startP):
                    thisLine.pop(startP)

                thisLine.insert(startP, str(thisAmount))

            else:

                toCompute = thisLine
                thisString = str("".join(toCompute))
                operators = []

                for j in thisString:
                    if j == "+":
                        operators.append("+")
                    elif j == "*":
                        operators.append("*")

                thisString = thisString.replace("+","*")
                thisString = thisString.split("*")

                lowerIndex = 0

                for j in operators:
                    if j == "+":
                        thisAmount = int(thisString[lowerIndex+1]) + int(thisString[lowerIndex])
                        thisString[lowerIndex] = str(thisAmount)
                        thisString.pop(lowerIndex+1)
                    else:
                        lowerIndex += 1

                thisAmount = 1
                for j in thisString:
                    thisAmount *= int(j)

                break

        answer += thisAmount

    print("Done")
    print(answer)
