import numpy as np

# Part1
expenses = np.loadtxt("input.txt").reshape(-1, 1)
combinations = expenses + expenses.T
lower = np.tril(combinations, k=-1)

idx1, idx2 = np.where(lower == 2020)
answer = expenses[idx1] * expenses[idx2]
print(idx1, idx2)
print(answer)

# Part2
expenses = expenses.reshape(-1, 1, 1)
combinations = expenses + expenses.T + expenses.transpose((1, 0, 2))
lower = np.tril(combinations, k=-1)
idx1, idx2, idx3 = np.where(lower == 2020)
answer = expenses[idx1[0]] * expenses[idx2[0]] * expenses[idx3[0]]
print(idx1, idx2, idx3)
print(answer)
