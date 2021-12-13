import numpy as np

if __name__ == '__main__':

    f=open("Task13.txt","r")
    lines=f.readlines()
    theInput = []
    folds = []

    maxX = 0
    maxY = 0

    for i in lines:
        i = i.rstrip()

        if "," in i:
            i = i.split(",")
            theInput.append([int(i[0]),int(i[1])])
            maxX = max(maxX, int(i[0]))
            maxY = max(maxY, int(i[1]))
        elif "=" in i:
            i = i.split(" ")
            i = i[2].split("=")
            folds.append([i[0],int(i[1])])
    f.close()

    if maxY % 2 == 1:
        if maxX % 2 == 1:
            thePaper = np.zeros((maxX+2,maxY+2))
        else:
            thePaper = np.zeros((maxX+1,maxY+2))
    else:
        if maxX % 2 == 1:
            thePaper = np.zeros((maxX+2,maxY+1))
        else:
            thePaper = np.zeros((maxX+1,maxY+1))

    for i in theInput:
        thePaper[i[0],i[1]] = 1

    for i in folds:

        if i[0] == "y":
            theFold = thePaper[:,i[1]+1:]
            theFold = np.flip(theFold,1)
            thePaper = thePaper[:,:i[1]] + theFold

        elif i[0] == "x":
            theFold = thePaper[i[1]+1:,:]
            theFold = np.flip(theFold,0)
            thePaper = thePaper[:i[1],:] + theFold

    print("Done")

    print("\n".join(["".join(["#" if x else "." for x in row]) for row in thePaper]))


    
