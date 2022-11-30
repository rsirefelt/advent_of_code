import numpy as np


def prob1(data):
    pass


def prob2(data):
    pass


def main():
    input_data = np.genfromtxt("testdata.csv", delimiter=",")
    input_data = np.genfromtxt("data.csv", delimiter=",")

    prob1(input_data)
    prob2(input_data)


if __name__ == "__main__":
    main()
