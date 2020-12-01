import numpy as np

x = np.loadtxt("input.txt")

for i in range(x.size - 2):
    for j in range(i + 1, x.size - 1):
        if x[i] + x[j] == 2020:
            print(f"Ans prob1: {x[i] * x[j]}")
        elif x[i] + x[j] < 2020:
            for k in range(j + 1, x.size):
                if x[i] + x[j] + x[k] == 2020:
                    print(f"Ans prob2: {x[i] * x[j] * x[k]}")
