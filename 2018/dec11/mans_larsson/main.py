import numpy as np
import math

def fuel_level(x, y, serial):
    rid = x + 10
    tmp = (rid*y+serial)*rid
    tmp = math.floor(tmp / 100) % 10
    return tmp - 5

inp = 4172

grid = np.zeros((300,300))
for x in range(300):
    for y in range(300):
        grid[y,x] = fuel_level(x,y,inp)

gridsum = np.zeros((300,300))        
for x in range(298):
    for y in range(298):
        gridsum[y,x] = grid[y:y+3,x:x+3].sum()

print(np.unravel_index(gridsum.argmax(), gridsum.shape)[::-1])

gridsum3d = np.zeros((300,300,300))  
for s in range(1,299):
    for x in range(301-s):
        for y in range(301-s):
            gridsum3d[x,y,s] = grid[y:y+s,x:x+s].sum() #notice coordinate change of gridsum3d

print(np.unravel_index(gridsum3d.argmax(), gridsum3d.shape))

