import numpy as np

adapters = np.loadtxt('inputs/day10', dtype=np.int)
adapters.sort()
adapters = np.insert(adapters, 0, 0)
diffs = np.diff(adapters)

print(f'a) {(diffs==1).sum()*((diffs==3).sum() + 1)}')

combinations = np.zeros_like(adapters)
combinations[0] = 1
for i in range(1, len(adapters)):
    for j in range(i-3, i):
        if j >= 0 and adapters[i] - adapters[j] <= 3:
            combinations[i] += combinations[j]

print(f'b) {combinations[-1]}')
