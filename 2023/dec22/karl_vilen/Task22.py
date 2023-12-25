import copy

if __name__ == '__main__':

    f=open("Task22.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.split("~")
        theInput.append(i)
    f.close()

    blocks = dict()

    for indexI, i in enumerate(theInput):

        coord1 = i[0].split(",")
        coord2 = i[1].split(",")

        x1 = int(coord1[0])
        x2 = int(coord2[0])
        y1 = int(coord1[1])
        y2 = int(coord2[1])
        z1 = int(coord1[2])
        z2 = int(coord2[2])

        coordinates = [[min(x1,x2),min(y1,y2),min(z1,z2)], [max(x1,x2),max(y1,y2),max(z1,z2)]]
        blocks[str(indexI)] = dict()

        blocks[str(indexI)]["coords"] = coordinates.copy()
        blocks[str(indexI)]["minZ"] = min(z1,z2)
        blocks[str(indexI)]["maxZ"] = max(z1,z2)

    anythingChanged = True

    while anythingChanged:

        anythingChanged = False
        blocksResting = dict()

        for keyI, blockI in blocks.items():

            blocksResting[keyI] = []

            anythingBelow = False
            newZ = 1
            resting = False

            for keyJ, blockJ in blocks.items():

                if keyI == keyJ:
                    continue

                if blockI["minZ"] < blockJ["maxZ"]+1:
                    continue

                x1I = blockI["coords"][0][0]
                x2I = blockI["coords"][1][0]
                y1I = blockI["coords"][0][1]
                y2I = blockI["coords"][1][1]

                x1J = blockJ["coords"][0][0]
                x2J = blockJ["coords"][1][0]
                y1J = blockJ["coords"][0][1]
                y2J = blockJ["coords"][1][1]

                withinX = (x1I <= x1J <= x2I) or (x1I <= x2J <= x2I) or (x1J <= x1I <= x2J) or (x1J <= x2I <= x2J)
                withinY = (y1I <= y1J <= y2I) or (y1I <= y2J <= y2I) or (y1J <= y1I <= y2J) or (y1J <= y2I <= y2J)

                if withinX and withinY:

                    if blockI["minZ"] == blockJ["maxZ"]+1:
                        resting = True
                        blocksResting[keyI].append(keyJ)
                        continue

                    newZ = max(blockJ["maxZ"]+1,newZ)
                    anythingBelow = True
                    continue

            if resting == False:
                if anythingBelow or blockI["minZ"] > 1:

                    blockI["maxZ"] = blockI["maxZ"] - (blockI["minZ"] - newZ)
                    blockI["minZ"] = newZ
                    blockI["coords"][0][2] = blockI["minZ"]
                    blockI["coords"][1][2] = blockI["maxZ"]
                    anythingChanged = True

    restingOn = dict()
    canBeRemoved = 0
    stableBricks = []

    for i in range(len(blocksResting)):

        toAdd = 1
        for key, value in blocksResting.items():

            if str(i) in value:
                if len(value) == 1:
                    toAdd = 0
                    break
        if toAdd == 0:
            stableBricks.append(i)
        canBeRemoved += toAdd

    totalFall = 0

    for i in stableBricks:

        falling = [str(i)]
        blocksResting2 = copy.deepcopy(blocksResting)
        
        while len(falling) > 0:

            toAdd = []

            for key, values in blocksResting2.items():

                amountRest = len(values)
                amountRemoved = 0

                for j in falling:

                    if j in values:
                        amountRemoved += 1
                        values.remove(j)

                if amountRemoved == amountRest and amountRest > 0:
                    toAdd.append(key)

            falling = toAdd.copy()
            totalFall += len(falling)

    print(totalFall)

