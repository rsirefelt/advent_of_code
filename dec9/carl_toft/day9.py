numPlayers = 428
lastMarble = 7082500

# Initialize table and elf scores 
gameTable = [0, 1] 
currPlayer = 1
currMarbleIndex = 1
nextMarbleNumber = 2
playerScores = [0 for x in range(numPlayers)] 

# Returns index of new current marble 
def placeMarble(gameTable, currMarbleIndex, nextMarbleNumber): 
    score = 0
    l = len(gameTable) 

    if (nextMarbleNumber % 23 != 0):
        # Place the marble regularly 
        newCurrMarbleIndex = (currMarbleIndex + 1) % l + 1
        # newCurrMarbleIndex = (currMarbleIndex + 2) % l
        gameTable.insert(newCurrMarbleIndex, nextMarbleNumber)
    else:
        # Do the fancy special placement 
        score += nextMarbleNumber
        indexOfMarbleToRemove = (currMarbleIndex - 7) % l 
        score += gameTable.pop(indexOfMarbleToRemove)

        if (indexOfMarbleToRemove != l-1):
            newCurrMarbleIndex = indexOfMarbleToRemove  
        else:
            newCurrMarbleIndex = 0 
    
    nextMarbleNumber += 1
    
    return (newCurrMarbleIndex, nextMarbleNumber, score)  

def printCurrLayout(gameTable, currMarbleIndex): 
    outputstr = ''
    for k in range(len(gameTable)):
        if k == currMarbleIndex:
            outputstr += '(' + str(gameTable[k]) + ') '
        else:
            outputstr += str(gameTable[k]) + ' '
    print(outputstr)

# Play game 
while True: 
    (currMarbleIndex, nextMarbleNumber, score) = placeMarble(gameTable, currMarbleIndex, nextMarbleNumber) 
    # printCurrLayout(gameTable, currMarbleIndex)
    playerScores[currPlayer] += score 
    #if (score != 0): 
    #    print('Curr score: ' + str(score) + ', max score: ' + str(max(playerScores))) 
    
    if nextMarbleNumber % 10000 == 0:
        print(nextMarbleNumber) 

    if (nextMarbleNumber > lastMarble): 
        # Game is over! 
        print('Game is over! Last marble is worth ' + str(score) + ' and best player has score ' + str(max(playerScores)))
        break 

    # Switch game to next player 
    currPlayer += 1
    if (currPlayer == numPlayers):
        currPlayer = 0

# print(playerScores) 