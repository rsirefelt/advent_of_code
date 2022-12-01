import numpy as np


def prob1(filename):
    calorie_list = []
    with open(filename, "r") as f:
        data_lines = f.readlines()
        sum = 0
        for string in data_lines:
            if string.rstrip() != "":
                sum += int(string.rstrip())
            else:
                calorie_list.append(sum)
                sum = 0
        calorie_list.append(sum)
        print(f"First problem: {np.max(calorie_list)}")
        print(f"Second problem: {np.sum(sorted(calorie_list)[-3:])}")


def main():
    filename = "testdata.csv"
    filename = "data.csv"

    prob1(filename)


if __name__ == "__main__":
    main()
