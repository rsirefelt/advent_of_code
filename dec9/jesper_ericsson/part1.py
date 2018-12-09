import numpy as np

def addNewMarble(circle, currentIndex, marbleCount):
    nextIndex = currentIndex + 2       
    if nextIndex > len(circle):
        nextIndex = 1
    circle.insert(nextIndex, marbleCount)
    return nextIndex
    
def removeMarbles(circle, playerScores, currentIndex,\
                    marbleCount, player):
    removeIndex = currentIndex - 7
    if removeIndex < 0:
        removeIndex = len(circle) + removeIndex
        
    playerScores[player] += circle.pop(removeIndex) + marbleCount
    return removeIndex
    
def main():
    lastMarble = 71035
    numberOfPlayers = 479

    circle = [0]
    marbleCount = 1
    currentIndex = 0
    playerScores = np.zeros(numberOfPlayers)
    while marbleCount <= lastMarble:
    
        for iPlayer in range(numberOfPlayers):
            if marbleCount%23 != 0:
                currentIndex = addNewMarble(circle, currentIndex, marbleCount)
            else:
                currentIndex = removeMarbles(circle, playerScores,\
                currentIndex, marbleCount, iPlayer)
            
            marbleCount += 1
            if marbleCount > lastMarble:
                break
    # print(playerScores)
    print(np.max(playerScores))

    
if __name__ == "__main__": main()
    
