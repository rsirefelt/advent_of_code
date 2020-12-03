

import os, sys, traceback, csv
sys.path.insert(0, os.path.abspath(".."))
import argparse


if __name__ == '__main__':

    f=open("Task3.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(i.rstrip())
    f.close()

    width = len(theInput[0])
    height = len(theInput)

    directions = [[1,1],[3,1],[5,1],[7,1],[1,2]]

    totalTrees = []

    for i in directions:

        j = 0
        trees = 0
        xPos = 0

        while j < height:

            k = theInput[j]
            if k[xPos] == "#":
                trees +=1

            xPos += i[0]
            xPos = xPos % width

            j += i[1]

        totalTrees.append(trees)

    answer = 1

    for i in totalTrees:
        answer = answer * i


    print("Done")
    print(totalTrees)
    print(answer)



