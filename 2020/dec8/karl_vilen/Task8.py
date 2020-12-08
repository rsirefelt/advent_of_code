from copy import deepcopy

if __name__ == '__main__':

    f=open("Task8.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i= i.rstrip()
        i = i.split(" ")
        theInput.append(i)
    f.close()

    cont = True

    for i in range(len(theInput)):
        intructions = deepcopy(theInput)
        accumulator = 0
        execIntrs = []
        instrPoint = 0

        if intructions[i][0] == "jmp":
            intructions[i][0] = "nop"
        elif intructions[i][0] == "nop":
            intructions[i][0] = "jmp"
        else:
            continue

        while cont:

            if instrPoint not in execIntrs:
                execIntrs.append(instrPoint)
            else:
                break

            if instrPoint > len(intructions)-1:
                cont = False
                break

            if intructions[instrPoint][0] == "acc":
                accumulator += int(intructions[instrPoint][1])
            elif intructions[instrPoint][0] == "jmp":
                instrPoint += int(intructions[instrPoint][1]) - 1

            instrPoint += 1

        if cont == False:
            break

    print("Done")
    print(accumulator)
