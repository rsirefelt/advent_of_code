def returnSize(theDirs, theFiles, thisDir):

    thisSize = 0
    if thisDir in theFiles.keys():
        for i in theFiles[thisDir]:
            thisSize += i

    if thisDir in theDirs.keys():
        for i in theDirs[thisDir]:
            thisSize += returnSize(theDirs, theFiles, i)

    return thisSize

if __name__ == '__main__':

    f=open("Task7.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i.split(" "))
    f.close()

    allDirs = dict()
    allDirs["/"] = 0
    dirs = dict()
    files = dict()

    currentDirTree = []

    for i in theInput:

        if i[0] == "$":
            if i[1] == "cd":
                if i[2] == "/":
                    currentDirTree = ["/"]
                elif i[2] == "..":
                    currentDirTree.pop()
                else:
                    currentDirTree.append(i[2])
            elif i[1] == "ls":
                continue

        elif i[0] == "dir":
            thisString = ""
            for j in currentDirTree:
                thisString = thisString + j

            if thisString not in dirs.keys():
                dirs[thisString] = []
            
            thisString2 = thisString + i[1]
            dirs[thisString].append(thisString2)
            if "/" in thisString2:
                allDirs[thisString2] = 0

        else:
            thisString = ""
            for j in currentDirTree:
                thisString = thisString + j
            if thisString not in files.keys():
                files[thisString] = []
            files[thisString].append(int(i[0]))

    allSizes = []
    answerSize = 0

    for i in allDirs.keys():
        thisSize = returnSize(dirs,files,i)
        if thisSize <= 100000:
            answerSize += thisSize
        allSizes.append(thisSize)

    print(answerSize)

    allSizes.sort()
    freeMemory = 70000000 - max(allSizes)
    neededMemory = 30000000

    for i in allSizes:
        if i + freeMemory > neededMemory:
            print(i)
            break 
