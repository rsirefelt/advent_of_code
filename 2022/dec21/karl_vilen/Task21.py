if __name__ == '__main__':

    f=open("Task21.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace(":", "")
        i = i.split(" ")
        theInput.append(i)
    f.close()

    monkeys = dict()

    allMonkeys = []

    for i in theInput:

        if len (i) > 2:
            monkeys[i[0]] = [i[1], i[2], i[3]]
        else:
            monkeys[i[0]] = float(i[1])

        allMonkeys.append(i[0])

    startMonkeys = monkeys.copy()

    monkeys["humn"] = 0.0

    toAdd = 0.0
    exponent = -1

    lastValueTested = 0
    startExtra = 0.0

    restart = True
    while restart == True:

        monkeys = startMonkeys.copy()
        monkeys["humn"] = startExtra + toAdd
        anyChange = True

        while anyChange == True:
            anyChange = False

            for i in allMonkeys:

                if isinstance(monkeys[i], float) == True:
                    continue
                else:
                    monkey1 = monkeys[i][0]
                    monkey2 = monkeys[i][2]

                    if isinstance(monkeys[monkey1], float) == True and isinstance(monkeys[monkey2], float) == True:

                        if i == "root":
                            monkeys[i] = eval(str(monkeys[monkey1]) + "==" + str(monkeys[monkey2]))
                            
                            if monkeys[i] == False:
                                restart = True

                                if monkeys[monkey1] < monkeys[monkey2]:
                                    exponent = 0
                                    startExtra = lastValueTested
                                else:
                                    lastValueTested = monkeys["humn"]
                                    exponent += 1

                                toAdd = float(2 ** exponent)

                            else:
                                restart = False

                            anyChange = False
                            
                            break
                        else:
                            monkeys[i] = eval(str(monkeys[monkey1]) + monkeys[i][1] + str(monkeys[monkey2]))

                        anyChange = True

    print("Answer")
    print(monkeys["humn"])


