import csv
import numpy as np
import itertools

import time
def naive(data):
    for ind, value in enumerate(data):
        for i in range(ind,len(data)):
            for value2 in data:
                if value+data[i]+value2 == 2020:
                    print(value+data[i]+value2)
                    print(value*data[i]*value2)

def work_slack_tips(data):
    all_combinations = itertools.combinations(data,3)
    for values in all_combinations:
        if values[0] + values[1] + values[2] == 2020:
            print(values[0] + values[1] + values[2])
            print(values[0] * values[1] * values[2])
def main():
    # input_data = np.genfromtxt('testdata.csv', delimiter=',')
    input_data = np.genfromtxt('data.csv', delimiter=',')

    start = time.time()
    naive(input_data)
    end = time.time()
    print(['Naive time: ', end - start])

    start = time.time()
    work_slack_tips(input_data)
    end = time.time()
    print(['Speed up time: ', end - start])

if __name__ == "__main__": main()