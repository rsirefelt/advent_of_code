import numpy as np

if __name__ == '__main__':

    f=open("Task5.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace(" ","")
        i = i.replace("->",",")
        i = i.split(",")
        theInput.append(i)
    f.close()

    theInput = ( [list( map(int,i) ) for i in theInput] )

    theMax = (np.amax(theInput))

    theGrid = np.zeros((theMax+1, theMax+1))

    for i in theInput:
        if i[0] == i[2]:
            for j in range(min(i[1],i[3]), max(i[1],i[3])+1):

                theGrid[i[0]][j] += 1

        elif i[1] == i[3]:
            for j in range(min(i[0],i[2]), max(i[0],i[2])+1):

                theGrid[j][i[1]] += 1

        else:

            if i[0] < i[2]:
                theMinX = i[0]
                theMaxX = i[2]
                startY = i[1]
                if i[1] < i[3]:
                    changeK = 1
                else:
                    changeK = -1
            else:
                theMinX = i[2]
                theMaxX = i[0]
                startY = i[3]
                if i[1] < i[3]:
                    changeK = -1
                else:
                    changeK = 1

            k = 0

            for j in range(theMinX,theMaxX+1):
                theGrid[j][startY+k] += 1
                k+=changeK


    print("Done")
    print(np.count_nonzero(theGrid >= 2))
