import numpy as np
from scipy.ndimage import convolve

energies = []
with open('inputs/day11') as f:
    for line in f:
        energies.append(np.array([c for c in line.rstrip()]).astype(np.int32))
energies = np.stack(energies)

kernel = np.ones((3, 3), np.int32)
kernel[1, 1] = 0

flashing_sum = 0
sync_step = None
sum_a = None
for step in range(10000000):
    energies += 1
    new_flash_indices = energies > 9
    flash_indices = np.zeros_like(new_flash_indices)
    while np.sum(new_flash_indices) > 0:
        energies[new_flash_indices] = 0
        flash_indices |= new_flash_indices
        flash_increases = convolve(new_flash_indices.astype(np.int32), kernel, mode='constant', cval=0)
        flash_increases[flash_indices] = 0
        energies += flash_increases
        new_flash_indices = energies > 9

    flashing_sum += np.sum(flash_indices)

    if step == 99:
        sum_a = flashing_sum
    if np.all(flash_indices):
        sync_step = step + 1

    if sum_a is not None and sync_step is not None:
        break

print(sum_a)
print(sync_step)
