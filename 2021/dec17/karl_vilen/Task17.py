if __name__ == '__main__':

    f=open("Task17.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("target area: x=", "")
        i = i.replace(" y=", "")
        i = i.replace("..", ",")
        i = i.split(",")
        theInput = i
    f.close()


    hitAreaX = [int(min(theInput[0],theInput[1])),int(max(theInput[0],theInput[1]))]
    hitAreaY = [int(min(theInput[2],theInput[3])),int(max(theInput[2],theInput[3]))]

    minVelX = 0
    maxVelX = hitAreaX[1] + 1

    minVelY = hitAreaY[0]-1
    maxVelY = 500

    totalHits = 0

    maxY = 0

    for i in range(minVelX, maxVelX):

        for j in range(minVelY, maxVelY):

            velocityX = i
            velocityY = j

            thisMaxY = 0

            posX = 0
            posY = 0

            while True:

                posX += velocityX
                posY += velocityY

                thisMaxY = max(thisMaxY, posY)

                if hitAreaX[0] <= posX <= hitAreaX[1] and hitAreaY[0] <= posY <= hitAreaY[1]:
                    maxY = max(maxY, thisMaxY)
                    totalHits += 1
                    break

                if posX > hitAreaX[1]:
                    break

                if posY < hitAreaY[0]:
                    break


                if velocityX > 0:
                    velocityX -= 1
                elif velocityX < 0:
                    velocityX +=1

                velocityY -=1

    print("Part 1")
    print(maxY)
    print("Part 2")
    print(totalHits)
