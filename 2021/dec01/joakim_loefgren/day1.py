import numpy as np

depths = np.loadtxt('input_day1.txt')

# Part I
count = np.sum(np.diff(depths) > 0)
print(count)

# Part II
win_size = 3
count = 0
old = int(1e10)
for i in range(len(depths) - win_size + 1):
    new = np.sum(depths[i:i + win_size])
    if new > old:
        count += 1
    old = new

print(count)
