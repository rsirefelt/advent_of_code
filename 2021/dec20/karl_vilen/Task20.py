if __name__ == '__main__':

    f=open("Task20.txt","r")
    lines=f.readlines()
    theInput = []

    for index, i in enumerate(lines):
        i = i.rstrip()

        if index == 0:
            enhancement = i
        elif index > 1:
            theInput.append(i)
    f.close()

    theWidth = len(theInput[0])
    theHeight = len(theInput)

    pixels = dict()

    for i in range(theHeight):
        for j in range(theWidth):

            if theInput[j][i] == "#":
                theKey = str(i)+"|"+str(j)
                pixels[theKey] = 1

    minX = 0
    maxX = theWidth-1
    minY = 0
    maxY = theHeight-1

    for iterations in range(50):

        minX -= 1
        maxX += 1
        minY -= 1
        maxY += 1

        newPixels = dict()

        infiniteSign = "1"
        if iterations % 2 == 0:
            infiniteSign = "0"

        for i in range(minX,maxX+1):
            for j in range(minY,maxY+1):

                binaryString = ""
                newKey = str(i) + "|" + str(j)

                for l in range(-1,2):
                    for k in range(-1,2):

                        thisKey = str(i+k) + "|" + str(j+l)

                        if (i+k <= minX) or (i+k >= maxX) or (j+l <= minY) or (j+l >= maxY):
                            binaryString += infiniteSign
                        else:
                            if thisKey in pixels.keys():
                                binaryString += "1"
                            else:
                                binaryString += "0"

                theIndex = int(binaryString,2)

                if enhancement[theIndex] == "#":
                    newPixels[newKey] = 1

        pixels = newPixels.copy()

    print("Done")
    print(len(pixels))

    
