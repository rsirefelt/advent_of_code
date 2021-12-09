import scipy
from scipy.ndimage import label
import numpy as np

if __name__ == '__main__':

    f=open("Task9.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        j = list(i)
        theInput.append(list(map(int,j)))
    f.close()
    
    width = len(theInput[0])
    height = len(theInput)

    minima = []

    for i in range(width):
        for j in range(height):

            thisValue = theInput[j][i]

            if max(0,j-1) == j-1:
                if theInput[j-1][i] <= thisValue:
                    continue
            if min(height-1,j+1) == j+1:
                if theInput[j+1][i] <= thisValue:
                    continue
            if max(0,i-1) == i-1:
                if theInput[j][i-1] <= thisValue:
                    continue
            if min(width-1,i+1) == i+1:
                if theInput[j][i+1] <= thisValue:
                    continue

            minima.append(thisValue)

    #part2
    npInput = np.array(theInput)
    npInput = np.where(npInput == 9, 0, 1)
    a, b = scipy.ndimage.label(npInput)

    sizes = []

    for i in range(1,b+1):
        sizes.append(np.count_nonzero(a == i))

    sizes.sort()

    print("Done")
    print(sizes[-1]*sizes[-2]*sizes[-3])
