import numpy as np

expenses = []
with open('inputs/day1') as f:
    for line in f:
        expenses.append(int(line.rstrip()))

expenses = np.array(expenses)

sums = np.expand_dims(expenses, axis=-1) + np.expand_dims(expenses, axis=0)
sums = np.triu(sums, k=1)
indices = np.argwhere(sums == 2020)

assert len(indices) == 1
print(f'a) product {expenses[indices[0][0]] * expenses[indices[0][1]]}')


triple_sums = np.expand_dims(sums, axis=-1) + np.expand_dims(expenses, axis=(0, 1))
triple_indices = np.argwhere(triple_sums == 2020)

# should be a triple permutation of set of indices
assert len(triple_indices) == 3

print(f'b) product {expenses[triple_indices[0][0]] * expenses[triple_indices[0][1]] * expenses[triple_indices[0][2]]}')
