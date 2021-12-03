import numpy as np
import operator

data = np.loadtxt('input_day3.txt', dtype=str)
bits = np.array([np.fromstring(' '.join(row), sep=' ', dtype=int) for row in data])

# Part I
nrows = bits.shape[0]
gamma = np.sum(bits, axis=0) > 0.5*bits.shape[0]
epsilon = ~gamma
gamma = int(''.join(gamma.astype(int).astype(str)), 2)
epsilon = int(''.join(epsilon.astype(int).astype(str)), 2)
print(gamma * epsilon)

# Part II
ratings = []
for op in [operator.ge, operator.lt]:
    bits_sel = bits.copy()
    j = 0
    while len(bits_sel) > 1:
        mask = op(np.sum(bits_sel, axis=0), 0.5*bits_sel.shape[0])
        bits_sel = bits_sel[bits_sel[:, j] == mask[j]]
        j += 1
    ratings.append(int(''.join(bits_sel[0].astype(str)), 2))
print(np.product(ratings))
