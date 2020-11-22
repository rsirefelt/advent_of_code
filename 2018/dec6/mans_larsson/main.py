import sys
import os
import numpy as np
import re

def calcdist(x,y,coords):
    dist = 0
    for coord in coords:
        dist += abs(coord['xy'][0]-x) + abs(coord['xy'][1]-y)
    return dist         

def add_neighbours_to_list(starting_coords):
    starting_coords_xp = starting_coords.copy()
    starting_coords_xp[:,0] += 1

    starting_coords_xm = starting_coords.copy()
    starting_coords_xm[:,0] -= 1

    starting_coords_yp = starting_coords.copy()
    starting_coords_yp[:,1] += 1

    starting_coords_ym = starting_coords.copy()
    starting_coords_ym[:,1] -= 1

    coords = np.concatenate((starting_coords, starting_coords_xp, starting_coords_xm, starting_coords_yp, starting_coords_ym), axis=0)
    coords = np.unique(coords, axis=0)

    indstokeep = (coords[:,0] >= 0) & (coords[:,0] < 400) & (coords[:,1] >= 0) & (coords[:,1] < 400)
    isinf = ~indstokeep.all()
    return isinf, coords[indstokeep,:]

pat = re.compile(r"^(\d+), (\d+)")

grid = np.zeros((400,400), dtype=int)
coords = []
count = 1
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        mm = pat.match(line)
        coords.append({'id': count, 'done': False,'xy': np.array([int(mm.group(1)), int(mm.group(2))]), 'all': np.array([[int(mm.group(1)), int(mm.group(2))], [int(mm.group(1)), int(mm.group(2))]])})
        count +=1  

#part1
while (grid == 0).sum() > 0:
    for coord in coords:
        if not coord['done']:
            coord['isinf'], coord['all'] = add_neighbours_to_list(coord['all'])
            indstochange = grid[tuple(coord['all'].T)] == 0
            if indstochange.any():
                grid[tuple(coord['all'][indstochange,:].T)] = coord['id']
            else:
                coord['done'] = True

maxcount = 0
for coord in coords:
    count = (grid == coord['id']).sum()
    if count > maxcount and ~coord['isinf']:
        maxcount = count
print(maxcount)   

#part2
dists = 10000*np.ones((400,400), dtype=int)      
for x in range(400):
    for y in range(400): 
         dists[x,y] = calcdist(x,y,coords)

print((dists < 10000).sum()) 

  




        