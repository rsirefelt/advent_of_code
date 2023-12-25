if __name__ == '__main__':

    f=open("Task4.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        #i = i[8:]
        i = i[10:]
        i = i.replace("  "," ")
        i = i.replace(" | ","|")
        i = i.replace(" ",",")
        i = i.replace(" ",",")
        i = i.split("|")
        i[0] = i[0].split(",")
        i[1] = i[1].split(",")

        theInput.append(i)
    f.close()

    score = 0

    totalCards = []

    for i in range(len(theInput)):
        totalCards.append(1)

    for indexI, i in enumerate(theInput):

        thisWins = 0

        for j in i[1]:

            if j in i[0]:

                thisWins += 1

        if thisWins > 0:
            score += pow(2,thisWins-1)

        for indexJ, j in enumerate(range(thisWins)):
            if indexI+indexJ+1 < len(theInput):
                totalCards[indexI+indexJ+1] += totalCards[indexI]

    print(score)

    print(sum(totalCards))
    

