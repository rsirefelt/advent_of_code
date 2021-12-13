import numpy as np
from matplotlib import pyplot as plt


dots = []
folds = []
with open('inputs/day13') as f:
    for line in f:
        if 'fold' in line:
            fold_data = line.rstrip()[11:].split('=')
            folds.append((fold_data[0], int(fold_data[1])))
        elif len(line) > 1:            

            dots.append([int(c) for c in line.rstrip().split(',')])

max_x = np.max([d[0] for d in dots]) 
max_y = np.max([d[1] for d in dots])
paper = np.zeros((max_y + 1, max_x + 1), dtype=bool)
for dot in dots:
    paper[dot[1], dot[0]] = True

for i, fold in enumerate(folds, 1):
    if fold[0] == 'y':
        paper = paper[:fold[1]:, :] | paper[-1:fold[1]:-1, :]
    else:
        paper = paper[:,:fold[1]:] | paper[:,-1:fold[1]:-1]

    print(f'points visible after fold {i}: {np.sum(paper)}')

plt.imshow(paper)
plt.show()