import numpy as np

measurements = []
with open('inputs/day1') as f:
    for line in f:
        measurements.append(int(line.rstrip()))

print(np.sum(np.diff(measurements) > 0))
print(np.sum(np.diff(np.convolve(measurements, [1, 1, 1], 'valid')) > 0))
