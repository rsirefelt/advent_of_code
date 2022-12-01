if __name__ == '__main__':

    f=open("Task1.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(i)
    f.close()

    elves = []
    elves.append(0)
    counter = 0

    for i in theInput:
        if i == "\n":
            elves.append(0)
            counter += 1
        else:
            elves[counter] += int(i)

    elves.sort()

    print(elves[-1])
    print(elves[-1] + elves[-2] + elves[-3])
