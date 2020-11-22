import sys
import os
import numpy as np
import re

pat = re.compile(r"^#(\d+) @ ([\d]+),([\d]+): (\d+)x(\d+)")
fab = np.zeros((1000,1000), dtype=int)
all_patches = []
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        mm = pat.match(line)
        tmp = {}
        tmp['p_id'] = int(mm.group(1))
        tmp['x_start'] = int(mm.group(2))
        tmp['y_start'] = int(mm.group(3))
        tmp['x_step'] = int(mm.group(4))
        tmp['y_step'] = int(mm.group(5))
        fab[tmp['x_start']:tmp['x_start']+tmp['x_step'], tmp['y_start']:tmp['y_start']+tmp['y_step']] += 1

        all_patches.append(tmp)
        
print((fab > 1).sum()) 

for patch in all_patches:
    if (fab[patch['x_start']:patch['x_start']+patch['x_step'], patch['y_start']:patch['y_start']+patch['y_step']] == 1).all():
        correct_id = patch['p_id']

print(correct_id)        
    