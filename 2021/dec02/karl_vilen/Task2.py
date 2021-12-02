if __name__ == '__main__':

    f=open("Task2.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(i.split(" "))
    f.close()

    depth = 0
    hori = 0
    aim = 0

    for i in theInput:

        if i[0] == "forward":
            hori += int(i[1])
            depth += int(i[1])*aim
        elif i[0] == "up":
            aim -= int(i[1])
        elif i[0] == "down":
            aim += int(i[1])
        else:
            print("invalid")

    print("Done")
    print(depth*hori)

