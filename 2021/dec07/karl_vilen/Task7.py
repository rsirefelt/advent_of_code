if __name__ == '__main__':

    f=open("Task7.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput = i.split(",")
    f.close()

    theInput = [int(i) for i in theInput]

    minFuel = max(theInput)*len(theInput)*len(theInput)

    fuelToThisPos = dict()

    for i in range(min(theInput),max(theInput)):

        positions = theInput.copy()

        fuels = [0 for i in theInput]

        for jIndex, j in enumerate(positions):

            sumTo = abs(positions[jIndex] - i)
            thisFuel = (sumTo * (sumTo+1))//2

            fuels[jIndex] = thisFuel

        totalFuel = sum(fuels)

        if totalFuel < minFuel:
            minFuel = totalFuel
        else:
            break

    print("Done")
    print(minFuel)
