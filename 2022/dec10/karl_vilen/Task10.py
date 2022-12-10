if __name__ == '__main__':

    f=open("Task10.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i.split(" "))
    f.close()

    cycle = 1
    regX = 1
    strengths = []

    for i in theInput:

        if i[0] == "noop":
            if (cycle - 20) % 40 == 0:
                strengths.append(regX * cycle)
            cycle += 1
        elif i[0] == "addx":
            for j in range(2):
                if (cycle - 20) % 40 == 0:
                    strengths.append(regX * cycle)
                cycle += 1
            regX += int(i[1])

    print(sum(strengths[:6]))

    cycle = 1
    regX = 1
    pixels = [0] * 40 * 6
    theRow = 0

    for i in theInput:

        if i[0] == "noop":
            
            if regX - 1 <= (cycle - 1) <= regX + 1:
                pixels[theRow * 40 + cycle - 1] = 1

            if cycle % 40 == 0:
                theRow += 1
                cycle = 0
            cycle += 1
        elif i[0] == "addx":
            for j in range(2):
                if regX - 1 <= (cycle - 1) <= regX + 1:
                    pixels[theRow * 40 + cycle - 1] = 1

                if cycle % 40 == 0:
                    theRow += 1
                    cycle = 0
                cycle += 1
            regX += int(i[1])

    print(pixels)