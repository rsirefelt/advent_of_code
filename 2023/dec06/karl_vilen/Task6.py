import re

if __name__ == '__main__':

    f=open("Task6.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = re.findall("[0-9]+", i)
        theInput.append(i)
    f.close()

    allLonger = [] 

    thisTime = int("".join(theInput[0]))
    thisDistance = int("".join(theInput[1]))

    longer = 0

    for i in range(thisTime):

        totalDistance = (thisTime - i) * i

        if totalDistance > thisDistance:
            longer += 1

    allLonger.append(longer)

    point = 1

    for i in allLonger:
        point = point * i

    print(point)
