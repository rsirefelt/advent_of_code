if __name__ == '__main__':

    f=open("Task9.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i.split(" "))
    f.close()

    lastPositions = dict()

    amountOfKnots = 10

    knots = []
    for i in range(amountOfKnots):
        knots.append([0,0])

    for i in theInput:

        if i[0] == "R":
            moveH = [1,0]
        elif i[0] == "L":
            moveH = [-1,0]
        elif i[0] == "U":
            moveH = [0,1]
        elif i[0] == "D":
            moveH = [0,-1]

        for j in range(int(i[1])):

            knots[0][0] = knots[0][0] + moveH[0]
            knots[0][1] = knots[0][1] + moveH[1]

            for k in range(1,amountOfKnots):

                if knots[k][0] == knots[k-1][0] and knots[k-1][1] - knots[k][1] > 1:
                    knots[k][1] += 1
                elif knots[k][0] == knots[k-1][0] and knots[k-1][1] - knots[k][1] < -1:
                    knots[k][1] -= 1

                elif knots[k][1] == knots[k-1][1] and knots[k-1][0] - knots[k][0] > 1:
                    knots[k][0] += 1
                elif knots[k][1] == knots[k-1][1] and knots[k-1][0] - knots[k][0] < -1:
                    knots[k][0] -= 1

                elif knots[k-1][0] > knots[k][0] and knots[k-1][1] > knots[k][1]:
                    if abs(knots[k-1][0] - knots[k][0]) + abs(knots[k-1][1] - knots[k][1]) > 2:
                        knots[k][0] += 1
                        knots[k][1] += 1
                elif knots[k-1][0] > knots[k][0] and knots[k-1][1] < knots[k][1]:
                    if abs(knots[k-1][0] - knots[k][0]) + abs(knots[k-1][1] - knots[k][1]) > 2:
                        knots[k][0] += 1
                        knots[k][1] -= 1
                elif knots[k-1][0] < knots[k][0] and knots[k-1][1] > knots[k][1]:
                    if abs(knots[k-1][0] - knots[k][0]) + abs(knots[k-1][1] - knots[k][1]) > 2:
                        knots[k][0] -= 1
                        knots[k][1] += 1
                elif knots[k-1][0] < knots[k][0] and knots[k-1][1] < knots[k][1]:
                    if abs(knots[k-1][0] - knots[k][0]) + abs(knots[k-1][1] - knots[k][1]) > 2:
                        knots[k][0] -= 1
                        knots[k][1] -= 1

                if k == amountOfKnots - 1:
                    lastPositions[str(knots[k][0]) + "," + str(knots[k][1])] = 1

    print(len(lastPositions))