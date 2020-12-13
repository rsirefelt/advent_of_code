if __name__ == '__main__':

    f=open("Task13.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("x","0")
        i = i.split(",")
        theInput.append(i)
    f.close()

    a = theInput[0]
    b = []

    for index, i in enumerate(a):
        if int(i) != 0:
            b.append([int(i),index])

    thisTime = 0
    denominator = 1

    for thisBus, theOffset in b:

        while (thisTime + theOffset) % thisBus != 0:
            thisTime += denominator
        denominator *= thisBus

    print("Done")
    print(thisTime)