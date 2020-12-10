import numpy as np
from collections import defaultdict
lines = np.loadtxt("input.txt")
lines.sort()
lines = np.insert(lines, 0, 0)
lines = np.append(lines, lines[-1] + 3)

diffs = np.diff(lines)
print((diffs == 1).sum() * (diffs == 3).sum())

combs = defaultdict(int)
combs[0] = 1
for i in range(len(lines)):
  for j in range(i - 3, i):
    if lines[i] - lines[j] <= 3:
      combs[i] += combs[j]

print(combs)
