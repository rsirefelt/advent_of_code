def charToHash(theChar, startValue):

    thisValue = startValue
    thisValue += ord(theChar)
    thisValue = thisValue * 17
    thisValue = thisValue % 256

    return thisValue


if __name__ == '__main__':

    f=open("Task15.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.split(",")
        theInput.append(i)
    f.close()

    for i in theInput:
        finalValue = 0
        for j in i:
            currentValue = 0
            for k in j:
                currentValue = charToHash(k,currentValue)
            finalValue += currentValue
    print(finalValue)

    boxes = []
    for i in range(256):
        boxes.append(dict())

    for i in theInput:
        for j in i:

            toAddOrChange = False

            if "=" in j:
                a = j.split("=")
                number = int(a[1])
                toAddOrChange = True
            elif "-" in j:
                a = j.split("-")

            label = a[0]

            currentValue = 0
            for k in label:
                currentValue = charToHash(k,currentValue)

            if toAddOrChange:
                boxes[currentValue][label] = number
            else:
                if label in boxes[currentValue].keys():
                    boxes[currentValue].pop(label)

    totalValue = 0
    for iIndex, i in enumerate(boxes):
        theKeys = list(i.keys())
        for jIndex, j in enumerate(theKeys):
            totalValue += (iIndex + 1) * (jIndex + 1) * i[j]

    print(totalValue)

