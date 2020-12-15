if __name__ == '__main__':

    f=open("Task15.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.split(",")
        theInput = list(map(int,i))
    f.close()

    numbers = dict()

    for index, i in enumerate(theInput):
        numbers[i] = index
        prevNumber = i

    thisTurn = len(numbers)

    iterations = 30000000-len(numbers)

    for i in range(iterations):

        if prevNumber in numbers:
            newNumber = thisTurn - numbers[prevNumber] - 1 
        else:
            newNumber = 0

        numbers[prevNumber] = thisTurn - 1
        prevNumber = newNumber

        thisTurn += 1

        if i % 1000000 == 0:
            print(i)


    print("Done")
    print(newNumber)