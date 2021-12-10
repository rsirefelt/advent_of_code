if __name__ == '__main__':

    f=open("Task10.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    inValidChars = []
    corruptedLines = []

    for iIndex, i in enumerate(theInput):
        investigated = []
        for jIndex, j in enumerate(i):

            tofind = ""

            if j == ">":
                toFind = "<"
            elif j == ")":
                toFind = "("
            elif j == "]":
                toFind = "["
            elif j == "}":
                toFind = "{"
            else:
                continue

            investigated.append(jIndex)
            for k in range(jIndex,-1,-1):

                if k not in investigated:
                    if i[k] == toFind:
                        investigated.append(k)
                        break
                    else:
                        investigated.append(k)
                        inValidChars.append(j)
                        corruptedLines.append(iIndex)
                        break

    syntaxValue = 0
    for i in inValidChars:
        if i == ">":
            syntaxValue += 25137
        elif i == ")":
            syntaxValue += 3
        elif i == "]":
            syntaxValue += 57
        elif i == "}":
            syntaxValue += 1197

    print("Part 1")
    print(syntaxValue)

    input2 = []
    for iIndex, i in enumerate(theInput):
        if iIndex not in corruptedLines:
            input2.append(i)

    allValues = []
    for iIndex, i in enumerate(input2):
        paired = []
        part2Value = 0
        for jIndex in range(len(i)-1,-1,-1):
        
            j = i[jIndex]

            tofind = ""

            if j == ">":
                toFind = "<"
            elif j == ")":
                toFind = "("
            elif j == "]":
                toFind = "["
            elif j == "}":
                toFind = "{"
            else:
                continue

            for k in range(jIndex,-1,-1):

                if k not in paired:
                    if i[k] == toFind:
                        paired.append(jIndex)
                        paired.append(k)
                        break

        incomplete = []
        for jIndex, j in enumerate(i):

            if jIndex not in paired:
                incomplete.append(j)

        for jIndex in range(len(incomplete)-1,-1,-1):
            part2Value *= 5
            
            j = incomplete[jIndex]

            if j == "<":
                part2Value += 4
            elif j == "(":
                part2Value += 1
            elif j == "[":
                part2Value += 2
            elif j == "{":
                part2Value += 3

        allValues.append(part2Value)

    allValues.sort()

    answer = allValues[len(allValues)//2]

    print("Part 2")
    print(answer)
