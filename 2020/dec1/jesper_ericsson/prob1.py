import csv
import numpy as np
from collections import defaultdict


def main():
    sum = 0
    # input_data = np.genfromtxt('testdata.csv', delimiter=',')
    input_data = np.genfromtxt('data.csv', delimiter=',')
    print(input_data)
    for ind, value in enumerate(input_data):
        for i in range(ind,len(input_data)):
            if value+input_data[i] == 2020:
                print(value+input_data[i])
                print(value*input_data[i])
            

if __name__ == "__main__": main()
	