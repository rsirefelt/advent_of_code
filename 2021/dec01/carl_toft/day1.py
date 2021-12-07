import numpy as np
x = np.loadtxt("input.txt")

# Part 1
num_increasing = 0
for k in range(1, x.size):
    if x[k] > x[k-1]:
        num_increasing = num_increasing + 1
print("Part 1:", num_increasing)

# Part 2
num_increasing = 0
for k in range(1, x.size-2):
    if np.sum(x[k:k+3]) > np.sum(x[k-1:k+2]):
        num_increasing = num_increasing + 1
print("Part 2:", num_increasing)
xxx = 3