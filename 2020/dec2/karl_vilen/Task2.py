

import os, sys, traceback, csv
sys.path.insert(0, os.path.abspath(".."))
import argparse


if __name__ == '__main__':

    f=open("Task2.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.replace("-"," ")
        i = i.replace(":"," ")
        theInput.append(i.split())
    f.close()

    valid = 0

    for i in theInput:

        minimum = int(i[0])
        maximum = int(i[1])
        occur= i[3].count(i[2])

        found = 0

        if i[3][minimum-1] == i[2]:
            found += 1

        if i[3][maximum-1] == i[2]:
            found += 1

        if found == 1:
            valid += 1

        #if minimum <= occur <= maximum:
        #    valid +=1

    print("Done")
    print(valid)



