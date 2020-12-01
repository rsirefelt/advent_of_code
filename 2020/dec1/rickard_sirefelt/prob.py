import numpy as np

x = np.loadtxt("input.txt")

for i in range(x.size - 2):
    for j in range(i + 1, x.size - 1):
        sum1 = x[i] + x[j]
        if sum1 == 2020:
            print(f"Ans prob1: {sum1}")
        elif sum1 < 2020:
            for k in range(j + 1, x.size):
                if sum1 + x[k] == 2020:
                    print(f"Ans prob2: {sum1 * x[k]}")
