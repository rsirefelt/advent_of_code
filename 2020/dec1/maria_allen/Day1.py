import numpy as np
list2 = np.genfromtxt('mynumbers.txt', delimiter=', ')

n = len(list2)

# Uppgift 1

for i in range(0, n):
    for j in range(i + 1, n):
        if list2[i] + list2[j] == 2020:
            print("Svar uppgift 1:", list2[i] * list2[j])
            break

# Uppgift 2

for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if list2[i] + list2[j] + list2[k] == 2020:
                print("Svar uppgift 2:", list2[i] * list2[j] * list2[k])
                break
