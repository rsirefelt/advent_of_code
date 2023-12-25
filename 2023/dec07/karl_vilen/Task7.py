def valueOfCard(theCard):

    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    returnValue = 0
    if theCard in numbers:
        returnValue = int(theCard)
    elif theCard == "A":
        returnValue = 14
    elif theCard == "K":
        returnValue = 13
    elif theCard == "Q":
        returnValue = 12
    #elif theCard == "J":
    #    returnValue = 11
    elif theCard == "J":
        returnValue = 1
    elif theCard == "T":
        returnValue = 10
    return returnValue

def sortFunction(theCards):

    returnValue = 0

    for index, i in enumerate(theCards):

        returnValue += valueOfCard(i) * (pow(0xFFFFF,5-index))

    return returnValue

def classifyHand(theHand):

    thisHand = theHand
    fives = 0
    fours = 0
    threes = 0
    twos = 0

    maxCounts = 0
    maxChars = "J"

    for i in theHand:
        if i == "J":
            continue
        thisAmount = thisHand.count(i)
        if thisAmount > maxCounts:
            maxChars = i
            maxCounts = thisAmount
    thisHand = thisHand.replace("J",maxChars)

    while len(thisHand) > 0:

        thisCard = thisHand[0]

        copies = thisHand.count(thisCard)

        thisHand = thisHand.replace(thisCard, "")

        if copies == 5:
            fives +=1
            return 6
        elif copies == 4:
            fours +=1
            return 5
        elif copies == 3:
            threes +=1
        elif copies == 2:
            twos +=1

    if threes == 1:
        if twos == 1:
            return 4
        else:
            return 3

    if twos == 2:
        return 2
    elif twos == 1:
        return 1

    return 0


if __name__ == '__main__':

    f=open("Task7.txt","r")
    lines=f.readlines()
    cards = []
    bets = dict()

    for i in lines:
        i = i.strip()
        i = i.split(" ")
        cards.append(i[0])
        bets[i[0]] = int(i[1])
    f.close()

    fiveKind = []
    fourKind = []
    house = []
    threeKind = []
    twoPair = []
    onePair = []
    highCard = []

    for i in cards:

        thisHand = classifyHand(i)
        if thisHand == 6:
            fiveKind.append(i)
        elif thisHand == 5:
            fourKind.append(i)
        elif thisHand == 4:
            house.append(i)
        elif thisHand == 3:
            threeKind.append(i)
        elif thisHand == 2:
            twoPair.append(i)
        elif thisHand == 1:
            onePair.append(i)
        elif thisHand == 0:
            highCard.append(i)

    sortedFiveKind = sorted(fiveKind, key = sortFunction, reverse = True)
    sortedFourKind = sorted(fourKind, key = sortFunction, reverse = True)
    sortedHouse = sorted(house, key = sortFunction, reverse = True)
    sortedThreeKind = sorted(threeKind, key = sortFunction, reverse = True)
    sortedTwoPair = sorted(twoPair, key = sortFunction, reverse = True)
    sortedOnePair = sorted(onePair, key = sortFunction, reverse = True)
    sortedHighCard = sorted(highCard, key = sortFunction, reverse = True)

    finalHand = []
    finalHand.extend(sortedFiveKind)
    finalHand.extend(sortedFourKind)
    finalHand.extend(sortedHouse)
    finalHand.extend(sortedThreeKind)
    finalHand.extend(sortedTwoPair)
    finalHand.extend(sortedOnePair)
    finalHand.extend(sortedHighCard)

    answer = 0
    thisRank = len(finalHand)

    for i in finalHand:
        answer += thisRank * bets[i]
        thisRank -= 1

    print(answer)
