import numpy as np

fabric = np.zeros((1000, 1000), dtype=int)
claims = np.zeros((1323, 7), dtype=int)
with open("dec3/rickard_sirefelt/input.txt", 'r') as f:
    for i, line in enumerate(f):
        line = line.split('@')[1]
        x1 = int(line.split(',')[0].lstrip())
        y1 = int(line.split(',')[1].split(':')[0])
        w = int(line.split(':')[1].split('x')[0].lstrip())
        h = int(line.split('x')[1].rstrip())
        x2 = x1 + w - 1
        y2 = y1 + h - 1
        claims[i, :] = [i, x1, y1, w, h, x2, y2]
        fabric[x1:x2 + 1, y1:y2 + 1] += 1

fabric = (fabric == 1)

for i, x1, y1, w, h, x2, y2 in claims:
    if sum(sum(fabric[x1:x2 + 1, y1:y2 + 1])) == w * h:
        print(i + 1)
        break
