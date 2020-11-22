import sys
import os
import numpy as np
from PIL import Image

def visualize(x, y, sname):
    xmin = min(x)
    ymin = min(y)
    xmax = max(x)
    ymax = max(y)
    xd = x.copy() - xmin
    yd = y.copy() - ymin
    
    if xmax-xmin > 100 or ymax-ymin > 100:
        return

    canv = np.zeros((ymax-ymin+1, xmax-xmin+1))
    canv[yd,xd] = 1            
    
    im = Image.fromarray(np.uint8(canv*255))
    im.save(sname)

x = np.zeros(327, dtype=int)
y = np.zeros(327, dtype=int)
vx = np.zeros(327, dtype=int)
vy = np.zeros(327, dtype=int)
count = 0
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        a = line.replace('<',',').replace('>',',').split(',')
        
        x[count] = int(a[1].strip())
        y[count] = int(a[2].strip())
        vx[count] = int(a[4].strip())
        vy[count] = int(a[5].strip())
        count += 1
        
for i in range(100000):
    visualize(x,y, '%d.png' % i)
    x += vx        
    y += vy 
        