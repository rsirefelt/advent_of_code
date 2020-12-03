

import os, sys, traceback, csv
sys.path.insert(0, os.path.abspath(".."))
import argparse


if __name__ == '__main__':

    f=open("Task1.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(int(i))
    f.close()

    print(theInput)

    found = False

    for xIndex, xVal in enumerate(theInput):
        for yIndex, yVal in enumerate(theInput[xIndex:]):
            for zIndex, zVal in enumerate(theInput[yIndex:]):
                if xVal+yVal+zVal == 2020:
                    print("Found")
                    found = True
                    break

            if found == True:
                break
        if found == True:
                break

    print(xVal)
    print(yVal)
    print(zVal)
    print(xVal*yVal*zVal)



