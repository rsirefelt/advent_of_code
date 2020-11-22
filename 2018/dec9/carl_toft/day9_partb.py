numPlayers = 428
lastMarble = 7082500

# Create a doubly linked list class 
class Item: 
    def __init__(self, value):
        self.nextItem = None
        self.prevItem = None 
        self.value = value 

    def insertItemAfter(self, newItem): 
        self.nextItem.prevItem = newItem 
        newItem.nextItem = self.nextItem
        self.nextItem = newItem
        newItem.prevItem = self 
    
    # Removes the current item from the list, by joining
    # the next and previous items 
    def removeCurrentItem(self): 
        self.prevItem.nextItem = self.nextItem 
        self.nextItem.prevItem = self.prevItem

        return (self.value, self.nextItem) 

    # Returns the item n steps in forwards of the current
    # item 
    def goForwards(self, n):
        item = self.nextItem
        for k in range(n-1): 
            item = item.nextItem 
        return item 

    # Returns the item n steps behind of the current
    # item 
    def goBackwards(self, n): 
        item = self.prevItem
        for k in range(n-1): 
            item = item.prevItem 
        return item


def printList(item, currentItem): 
    firstItem = item 
    isDone = False 

    fullStr = '' 
    if item is currentItem:
        fullStr += '(' + str(item.value) + ') '
    else:
        fullStr += str(item.value) + ' '

    while not isDone: 
        item = item.nextItem
        if item is None or item is firstItem:
            isDone = True 

        if (item is currentItem):
            fullStr += '(' + str(item.value) + ') '
        else:
            fullStr += str(item.value) + ' '    
    
    print(fullStr)

def printListBackwards(item, currentItem): 
    firstItem = item 
    isDone = False 

    fullStr = '' 
    if item is currentItem:
        fullStr += '(' + str(item.value) + ') '
    else:
        fullStr += str(item.value) + ' '

    while not isDone: 
        item = item.prevItem
        if item is None or item is firstItem:
            isDone = True 

        if (item is currentItem):
            fullStr += '(' + str(item.value) + ') '
        else:
            fullStr += str(item.value) + ' '    
    
    print(fullStr)

# Initialize the circle 
firstMarble = Item(0) 
firstMarble.nextItem = firstMarble
firstMarble.prevItem = firstMarble 

# Initialize the pointer to the current marble 
currentMarble = firstMarble 
nextMarbleNumber = 1 

# Initialize player scores 
currPlayer = 0
playerScores = [0 for x in range(numPlayers)] 

while True: 
    # Perform action for next marble 
    if (nextMarbleNumber % 23 != 0): 
        # Just add the new marble two steps ahead of the current marble 
        newMarble = Item(nextMarbleNumber)
        currentMarble.nextItem.insertItemAfter(newMarble) 
        currentMarble = newMarble 
    else: 
        playerScores[currPlayer] += nextMarbleNumber 
        sevenBehindMarble = currentMarble.goBackwards(7)
        (score, nextMarble) = sevenBehindMarble.removeCurrentItem() 
        playerScores[currPlayer] += score 
        currentMarble = nextMarble
    
    nextMarbleNumber += 1

    # Switch game to next player 
    currPlayer += 1
    if (currPlayer == numPlayers):
        currPlayer = 0
    
    # Check if the game is over 
    if (nextMarbleNumber > lastMarble): 
        print('Game is over. Winning elf has score ' + str(max(playerScores)))
        break 

