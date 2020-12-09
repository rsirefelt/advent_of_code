import numpy as np
lines = np.loadtxt("input.txt")

# Part 1
n_pre = 25
for idx in range(len(lines)):
  preamble = lines[idx:idx + n_pre].reshape(1, -1)
  next_val = lines[idx + n_pre]

  lower = np.tril(preamble + preamble.T, k=-1)
  idx1, idx2 = np.where(lower == next_val)
  if not idx1.size:
    print(next_val)
    break


# Part 2
def hack(lines):
  for i in range(len(lines)):
    idxs = []
    sum_val = 0
    for j in range(len(lines)):
      val = lines[i + j]
      sum_val += val
      idxs.append(val)

      if sum_val == next_val:
        return idxs

      if sum_val > next_val:
        break


idxs = hack(lines)
print(idxs)
print(min(idxs) + max(idxs))
