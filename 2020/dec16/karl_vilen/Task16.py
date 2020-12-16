from copy import deepcopy

if __name__ == '__main__':

    f=open("Task16.txt","r")
    lines=f.readlines()
    theInput = []

    fields = []
    myTicket = []
    nearbyTickets = []

    j = 0

    for i in lines:
        i = i.rstrip()
        i = i.replace(" or ", ":")
        i = i.replace("-", ":")
        i = i.replace(":",",")
        i = i.replace(" ", "")
        i = i.split(",")
        theInput.append(i)

        if i == ["yourticket",""] or i == ["nearbytickets",""]:
            j+=1
            continue
        elif i == [""]:
            continue

        if j == 0:
            fields.append(i)
        elif j == 1:
            myTicket.append(i)
        else:
            nearbyTickets.append(i)

    f.close()

    myTicket = myTicket[0]

    invalidNumbers = []
    indexInvalid = []

    for index, i in enumerate(nearbyTickets):
        for j in i:
            isValid = False
            for k in fields:
                if (int(k[1]) <= int(j) <= int(k[2])) or (int(k[3]) <= int(j) <= int(k[4])):
                    isValid = True
                    break
            if isValid == False:
                invalidNumbers.append(int(j))
                indexInvalid.append(index)

    print("Answer task 1")
    print(sum(invalidNumbers))

    validTickets = deepcopy(nearbyTickets)

    for i in reversed(indexInvalid):
        validTickets.pop(i)

    classDict = dict()

    validClasses = []

    for index, i in enumerate(fields):
        validClasses.append(index)

    for i in fields:
        classDict[i[0]] = deepcopy(validClasses)

    for i in validTickets:
        for jIndex, j in enumerate(i):
            for k in fields:
                if not((int(k[1]) <= int(j) <= int(k[2])) or (int(k[3]) <= int(j) <= int(k[4]))):

                    if jIndex in classDict[k[0]]:
                        classDict[k[0]].remove(jIndex)

    toRemove = None

    fieldIndex = dict()

    for i in range(len(fields)):

        for key, value in classDict.items():
            if len(classDict[key]) == 1:
                toRemove = value[0]
                fieldIndex[key] = toRemove
                break

        for key, value in classDict.items():
            if toRemove in value:
                value.remove(toRemove)

    desiredClasses = ["departurelocation","departurestation","departureplatform","departuretrack","departuredate","departuretime"]

    answer = 1

    for i in desiredClasses:
        answer *= int(myTicket[fieldIndex[i]])

    print("Done")
    print(answer)
