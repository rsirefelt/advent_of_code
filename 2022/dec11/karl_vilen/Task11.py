if __name__ == '__main__':

    f=open("Task11.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace(",","")
        i = i.replace(":","")
        theInput.append(i.split(" "))
    f.close()

    monkeys = []
    items = []
    operations = []
    divisors = []
    throwTrue = []
    throwFalse = []
    inspections = []

    for i in theInput:

        if len(i) == 1:
            continue

        if i[0] == "Monkey":

            thisMonkey = int(i[1])

            monkeys.append(thisMonkey)
            items.append(thisMonkey)
            operations.append(thisMonkey)
            divisors.append(thisMonkey)
            throwTrue.append(thisMonkey)
            throwFalse.append(thisMonkey)
            inspections.append(0)

        elif i[2] == "Starting":
            items[thisMonkey] = []
            for j in range(4, len(i)):
                items[thisMonkey].append(int(i[j]))

        elif i[2] == "Operation":
            operations[thisMonkey] = []
            operations[thisMonkey].append(i[6])
            operations[thisMonkey].append(i[7])

        elif i[2] == "Test":
            divisors[thisMonkey] = []
            divisors[thisMonkey].append(int(i[5]))

        elif i[5] == "true":
            throwTrue[thisMonkey] = []
            throwTrue[thisMonkey].append(int(i[9]))

        elif i[5] == "false":
            throwFalse[thisMonkey] = []
            throwFalse[thisMonkey].append(int(i[9]))


    newDivisior = 1
    for i in divisors:
        newDivisior = newDivisior * i[0]

    amountOfThrows = 10000
    for i in range(amountOfThrows):
        for j in monkeys:

            while len(items[j]) > 0:
                thisWorry = items[j].pop(0)
                inspections[j] += 1
                
                if operations[j][1] == "old":
                    factor = thisWorry
                else:
                    factor = int(operations[j][1])
                if operations[j][0] == "+":
                    thisWorry = thisWorry + factor
                elif operations[j][0] == "*":
                    thisWorry = thisWorry * factor

                thisWorry = thisWorry % newDivisior

                if thisWorry % divisors[j][0] == 0:
                    items[throwTrue[j][0]].append(thisWorry)
                else:
                    items[throwFalse[j][0]].append(thisWorry)

    inspections.sort()
    theAnswer = inspections[-1] * inspections[-2]
    print(theAnswer)

