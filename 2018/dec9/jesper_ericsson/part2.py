import numpy as np
from collections import deque

def addNewMarble(circle, marbleCount):
    circle.rotate(-1)
    circle.append(marbleCount)

    
def removeMarbles(circle, playerScores, marbleCount, player):
    circle.rotate(7)
    playerScores[player] += circle.pop() + marbleCount
    circle.rotate(-1)
    
def main():
    lastMarble = 7103500
    numberOfPlayers = 479

    circle = deque([0])
    marbleCount = 1
    currentIndex = 0
    playerScores = np.zeros(numberOfPlayers)
    iPlayer = 0
    for marbleCount in range(1, lastMarble+1):

        if marbleCount%23 != 0:
            addNewMarble(circle, marbleCount)
        else:
            removeMarbles(circle, playerScores, marbleCount, iPlayer)
        iPlayer = (iPlayer+1)%numberOfPlayers
        
        # print(circle)
    print(np.max(playerScores))

    
if __name__ == "__main__": main()
    
