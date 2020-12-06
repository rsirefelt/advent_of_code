if __name__ == '__main__':

    f=open("Task6.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i= i.rstrip()
        theInput.append(i)
    f.close()

    emptyDict = dict()

    allDicts = []
    allDicts.append(emptyDict.copy())
    firstEntry = True

    for i in theInput:

        if i == "":
            allDicts.append(emptyDict.copy())
            firstEntry = True
        else:
            if firstEntry == True:
                for j in i:
                    allDicts[len(allDicts)-1][j] = 1
            else:
                for j in list(allDicts[len(allDicts)-1].keys()):
                    if j not in i:
                        allDicts[len(allDicts)-1].pop(j, None)
            firstEntry = False
    
    theSum = 0
    for i in allDicts:
        theSum += len(i)

    print("Done")
    print(theSum)
