allBags = dict()

def findBag(bagType):

    returnValue = 1

    if (bool(bagType) == False) or "ootherbag" in bagType[0][0]: #No, that's not a typo. Comes from the assumption that there is less than 10 bags in each bag. 
        return returnValue
    else:
        for i in bagType:
            returnValue += int(i[1]) * findBag(allBags[i[0]])
        return returnValue

if __name__ == '__main__':

    f=open("Task7.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i= i.rstrip()
        i = i.replace("contain",",")
        i = i.replace(" ","")
        i = i.replace(".","")
        i = i.replace("bags","bag")
        i = i.split(",")
        theInput.append(i)
    f.close()

    for i in theInput:
        contains = []
        for jIndex, jValue in enumerate(i):
            if jIndex == 0:
                continue
            contains.append([jValue[1:],jValue[0]]) #Assumes that there is less than 10 bags in each bag. Too lazy to fix this in a more better way with regex
        
        allBags[i[0]] = contains

    print(allBags)

    bagsAmount = 0

    i = allBags["shinygoldbag"]
    bagsAmount += findBag(i)

    print("Done")
    print(bagsAmount-1) #Don't count the gold bag itself
