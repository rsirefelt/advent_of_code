if __name__ == '__main__':

    f=open("Task15.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("Sensor at x=","")
        i = i.replace(": closest beacon is at x="," ")
        i = i.replace(", y="," ")
        i = i.replace(" ",",")
        i = i.split(",")
        theInput.append(i)
    f.close()

    rowToInvestigate = 10
    investigated = set()
    beaconsAtRow = set()

    for i in theInput:

        x0 = int(i[0])
        y0 = int(i[1])
        x1 = int(i[2])
        y1 = int(i[3])

        if y1 == rowToInvestigate:
            beaconsAtRow.add(x1)

        distanceBetween = abs(x0 - x1) + abs(y0 - y1)

        if abs(rowToInvestigate - y0) < distanceBetween:

            moveAtRow = distanceBetween - abs(rowToInvestigate - y0)
            investigated.add(x0)

            for j in range(moveAtRow+1):
                investigated.add(x0 + j)
                investigated.add(x0 - j)

    for i in beaconsAtRow:
        if i in investigated:
            investigated.remove(i)

    print("Answer1")
    print(len(investigated))

    maxX = 4000000
    maxY = maxX

    answerFound = False
    for thisRow in range(0,maxY):

        if answerFound == True:
            break

        thisX = 0
        i = 0
        while i < len(theInput):

            j = theInput[i]

            x0 = int(j[0])
            y0 = int(j[1])
            x1 = int(j[2])
            y1 = int(j[3])

            distanceToThisX = abs(x0 - thisX) + abs(y0 - thisRow)
            distanceToBeacon = abs(x0 - x1) + abs(y0 - y1)

            if distanceToThisX <= distanceToBeacon:
                thisX = x0 + distanceToBeacon - abs(y0-thisRow) + 1
                i = 0
                continue

            if thisX >= maxX:
                break

            i += 1
            if i >= len(theInput):
                answer2 = 4000000 * thisX + thisRow
                answerFound = True

    print("Answer 2")
    print(answer2)
