allValues = dict()

def addValueToMemory(value, thisAdress):


    countX = thisAdress.count("X")
    if countX == 0:

        allValues[int("".join(thisAdress),2)] = value

    else:

        newAdress0 = thisAdress.copy()
        newAdress1 = thisAdress.copy()

        newAdress0[newAdress0.index("X")] = "1"
        newAdress1[newAdress1.index("X")] = "0"

        addValueToMemory(value, newAdress0)
        addValueToMemory(value, newAdress1)

if __name__ == '__main__':

    f=open("Task14.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace(" =","")
        i = i.replace("["," ")
        i = i.replace("]","")
        i = i.split(" ")
        theInput.append(i)
    f.close()


    for i in theInput:
        if i[0] == "mask":
            currentMask = i[1]
        else:
            thisInput = format(int(i[1]),"b")
            thisAdress = ["0"] * (len(currentMask)-len(thisInput))
            thisAdress.extend(thisInput)

            for index, j in enumerate(currentMask):
            
                if j == "1":
                    thisAdress[index] = "1"
                if j == "X":
                    thisAdress[index] = "X"

            addValueToMemory(int(i[2]), thisAdress)

    theSum = 0

    for i in allValues:
        theSum += allValues[i]

    print("Done")
    print(theSum)