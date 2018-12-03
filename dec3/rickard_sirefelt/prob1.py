import numpy as np

fabric = np.zeros((1000, 1000), dtype=int)
with open("dec3/rickard_sirefelt/input.txt", 'r') as f:    
    for line in f:
        line = line.split('@')[1]
        x1 = int(line.split(',')[0].lstrip())
        y1 = int(line.split(',')[1].split(':')[0])
        w = int(line.split(':')[1].split('x')[0].lstrip())
        h = int(line.split('x')[1].rstrip())
        x2 = x1 + w - 1
        y2 = y1 + h - 1

        fabric[x1:x2+1, y1:y2+1] += 1

print(sum(sum(fabric > 1)))
