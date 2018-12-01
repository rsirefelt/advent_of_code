import numpy as np


data = np.loadtxt("dec1/input.txt")
sum = 0
sum_dict = {0: 1}

found = False
while(True):
    for change in data:
        sum += change
        if sum in sum_dict:
            found = True
            break
        else:
            sum_dict[sum] = 1

    if found:
        break

print(sum)
