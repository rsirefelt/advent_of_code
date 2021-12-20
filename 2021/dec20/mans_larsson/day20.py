import numpy as np
from scipy.ndimage import convolve

conversion = []
image = []
read_im = False
with open('inputs/day20') as f:
    for line in f:
        if len(line) == 1:
            read_im = True
        elif not read_im:
            conversion.append(np.array([c == '#' for c in line.rstrip()]))
        else:
            image.append(np.array([c == '#' for c in line.rstrip()]))

conversion = np.concatenate(conversion)
image = np.stack(image)

binary_decoding_filer = np.array([2**i for i in range(9)], dtype=np.int32).reshape((3, 3))

n_iterations = 50
padding_value = 0
for i in range(n_iterations):
    image = np.pad(image, 1, mode='constant', constant_values=padding_value)
    keys = convolve(image.astype(np.int32), binary_decoding_filer, mode='constant', cval=padding_value)
    image = conversion[keys.flatten()].reshape(image.shape)

    padding_value = conversion[0] if padding_value == 0 else conversion[-1]
    if i == 1:
        print(np.sum(image))
print(np.sum(image))
