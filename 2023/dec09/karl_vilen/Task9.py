if __name__ == '__main__':

    f=open("Task9.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.split(" ")
        for j in range(0, len(i)):
                i[j] = int(i[j])
        theInput.append(i)
    f.close()

    totalAnswer1 = 0
    totalAnswer2 = 0

    for i in theInput:

        allSequences = []
        allSequences.append(i)
        lastSequence = i
        
        while True:

            nextSequence = []
            for j in range(1,len(lastSequence)):

                nextSequence.append(lastSequence[j] - lastSequence[j-1])

            allSequences.append(nextSequence)

            lastSequence = nextSequence.copy()

            if max(nextSequence) == 0 and min(nextSequence) == 0:
                break

        nextNumber1 = 0
        for i in range(len(allSequences)-1, 0, -1):
            nextNumber1 = nextNumber1 + allSequences[i-1][-1]
        totalAnswer1 += nextNumber1

        nextNumber2 = 0
        for i in range(len(allSequences)-1, 0, -1):
            nextNumber2 =  allSequences[i-1][0] - nextNumber2
        totalAnswer2 += nextNumber2

    print(totalAnswer1)
    print(totalAnswer2)

