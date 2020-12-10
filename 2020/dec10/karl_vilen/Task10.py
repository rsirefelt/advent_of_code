if __name__ == '__main__':

    f=open("Task10.txt","r")
    lines=f.readlines()
    theInput = []

    theInput.append(0)

    for i in lines:
        i= i.rstrip()
        theInput.append(int(i))
    f.close()

    theInput.sort()
    theInput.append(theInput[-1]+3)

    combinations = dict()

    combinations[theInput[0]] = 1
    combinations[theInput[1]] = 1
    combinations[theInput[2]] = 1

    if theInput[2] - theInput[0] <= 3:
        combinations[theInput[2]] += 1

    for i in range(3, len(theInput)):
        thisAdapter = theInput[i]
        combinations[thisAdapter] = 0

        for j in theInput[i-3:i]:
            if thisAdapter - j <= 3:
                combinations[thisAdapter] += combinations[j]

    print("Done")
    print(combinations[theInput[-1]])
