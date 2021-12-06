import numpy as np
import time


def prob1(fish_array, num_iter):
    for i in range(num_iter):
        num_new = np.sum(fish_array == 0)
        fish_array[fish_array == 0] = 7
        fish_array = np.append(fish_array, 9 * np.ones(num_new))
        fish_array -= 1

    print("Num fish", len(fish_array), "after", num_iter, "iterations")


def prob2(fish_array, num_iter):
    num_of_each_older = np.zeros(10, dtype=int)
    for fish in fish_array:
        num_of_each_older[fish] += 1

    for i in range(num_iter):
        num_of_each_older[9] = num_of_each_older[0]
        num_of_each_older[7] += num_of_each_older[0]

        for age in range(9):
            num_of_each_older[age] = num_of_each_older[age + 1]
        num_of_each_older[9] = 0

    print("Num fish", num_of_each_older.sum(), "after", num_iter, "iterations")


def main():
    input_data = np.genfromtxt("testdata.csv", dtype=int, delimiter=",")
    input_data = np.genfromtxt("data.csv", dtype=int, delimiter=",")

    start = time.time()
    prob1(input_data, 80)
    end = time.time()
    print(["Naive solution: ", end - start])

    start = time.time()
    prob2(input_data, 256)
    end = time.time()
    print(["Speed up: ", end - start])


if __name__ == "__main__":
    main()
