if __name__ == '__main__':

    f=open("Task12.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append([i[0],int(i[1:])])
    f.close()

    position = [0,0]
    wayPos = [10,1]

    for i in theInput:
        if i[0] == "N":
            wayPos[1] += i[1]
        elif i[0] == "S":
            wayPos[1] -= i[1]
        elif i[0] == "E":
            wayPos[0] += i[1]
        elif i[0] == "W":
            wayPos[0] -= i[1]
        elif i[0] == "R":
            for i in range(i[1]//90):
                oldX = wayPos[0]
                oldY = wayPos[1]
                wayPos[0] = oldY
                wayPos[1] = -oldX
        elif i[0] == "L":
            for i in range(i[1]//90):
                oldX = wayPos[0]
                oldY = wayPos[1]
                wayPos[0] = -oldY
                wayPos[1] = oldX
        elif i[0] == "F":
            position[0] += wayPos[0] * i[1]
            position[1] += wayPos[1] * i[1]

    print("Done")
    print(abs(position[0])+abs(position[1]))
