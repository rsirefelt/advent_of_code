if __name__ == '__main__':

    f=open("Task16.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        theInput.append(i)
    f.close()

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    height = len(theInput)
    width = len(theInput[0])
    allStartPositions = []

    for i in range(height):
        allStartPositions.append([i, -1, RIGHT])
        allStartPositions.append([i, width, LEFT])
    for j in range(width):
        allStartPositions.append([-1, j, DOWN])
        allStartPositions.append([height, j, UP])

    maxLight = 0

    for thisStart in allStartPositions:

        rays = [thisStart]
        visitedPlaces = dict()

        while len(rays) >= 1:

            for indexI, i in enumerate(rays):

                if i[2] == UP:
                    i[0] -= 1
                elif i[2] == RIGHT:
                    i[1] += 1
                elif i[2] == DOWN:
                    i[0] += 1
                elif i[2] == LEFT:
                    i[1] -= 1

                if i[0] < 0 or i[0] >= height:
                    rays.pop(indexI)
                    break
                elif i[1] < 0 or i[1] >= width:
                    rays.pop(indexI)
                    break

                theString = str(i[0]) + "," + str(i[1])
                if theString not in visitedPlaces.keys():
                    visitedPlaces[theString] = [i[2]]
                else:
                    if i[2] not in visitedPlaces[theString]:
                        visitedPlaces[theString].append(i[2])
                    else:
                        rays.pop(indexI)
                        break

                if theInput[i[0]][i[1]] == "\\":
                    if i[2] == UP:
                        i[2] = LEFT
                    elif i[2] == RIGHT:
                        i[2] = DOWN
                    elif i[2] == DOWN:
                        i[2] = RIGHT
                    elif i[2] == LEFT:
                        i[2] = UP

                elif theInput[i[0]][i[1]] == "/":
                    if i[2] == UP:
                        i[2] = RIGHT
                    elif i[2] == RIGHT:
                        i[2] = UP
                    elif i[2] == DOWN:
                        i[2] = LEFT
                    elif i[2] == LEFT:
                        i[2] = DOWN

                elif theInput[i[0]][i[1]] == "-":
                    if i[2] == UP or i[2] == DOWN:

                        rays.append([i[0],i[1],LEFT])
                        i[2] = RIGHT

                elif theInput[i[0]][i[1]] == "|":
                    if i[2] == RIGHT or i[2] == LEFT:

                        rays.append([i[0],i[1],UP])
                        i[2] = DOWN

            maxLight = max(maxLight, len(visitedPlaces.keys()))

    print(maxLight)

