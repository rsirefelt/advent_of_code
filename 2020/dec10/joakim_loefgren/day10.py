""" Advent of Code Day 10 """

import numpy as np
import itertools
from scipy.special import binom

adapters = np.loadtxt('./input_day10.txt', dtype=np.int64)
adapters = np.concatenate(([0], np.sort(adapters), [np.max(adapters) + 3]))
diffs = np.diff(adapters)

# Part I
count1 = (diffs == 1).sum()
count3 = (diffs == 3).sum()
print(count1*count3)

# Part II
# Assuming there are no voltage diffs of 2 in the sorted adapter list.
# For each island of N<=5 adapters with voltage diff = 1, we can drop groups
# of 0, 1 or 2 adapters (if island size allows).
nperms = 1
for diff, group in itertools.groupby(diffs):
    if diff == 1:
        group = list(group)
        nfree = len(group) - 1
        fac = np.sum([binom(nfree, i) for i in [0, 1, 2]])
        if nfree > 3:  # no cases like this in the input...
            raise ValueError('Invalid forumula')
        nperms *= fac

print(int(nperms))
