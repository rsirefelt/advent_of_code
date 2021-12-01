import numpy as np

def prob1(data):
    diff = np.diff(data)
    negative = diff > 0
    print(np.sum(negative))

def prob2(data):
    sliding_sums = np.convolve(data,np.ones(3,dtype=int),'valid')
    diff = np.diff(sliding_sums)
    negative = diff > 0
    print(np.sum(negative))

def main():
    input_data = np.genfromtxt('testdata.csv', delimiter=',')
    input_data = np.genfromtxt('data.csv', delimiter=',')

    prob1(input_data)
    prob2(input_data)


            

if __name__ == "__main__": main()
	
