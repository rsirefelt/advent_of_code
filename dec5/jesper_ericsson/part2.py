import numpy as np
import string
from datetime import datetime
import operator
def calcLength(input):
    index = 0
    while index+1 < len(input):
        if (input[index] == input[index+1].upper() or\
            input[index] == input[index+1].lower()) and not\
            input[index] == input[index+1]:

            input = input[:index] + input[index+2:]
            index -= 1
            if index < 0:
                index = 0
        else:
            index += 1
            
    return(len(input))


def main():
    input = []

    # with open('testdata.csv', 'r') as f:
    with open('input.txt', 'r') as f:
        for line in f:
            input = line.rstrip().lstrip()
    minLength = len(input)    
    for c,C in zip(string.ascii_lowercase,string.ascii_uppercase):
        testPolymore = input.replace(c,'').replace(C,'')
        length = calcLength(testPolymore)
        if length < minLength:
            minLength = length
            
    print(minLength)

if __name__ == "__main__": main()
	
