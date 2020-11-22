import sys
import os
import numpy as np

def resolve_node(data, ind):
    meta = 0
    n_childs = data[ind]
    n_meta = data[ind+1]
    child_ind = ind+2 # first child ind
    for i in range(n_childs): #resolve all childs
        child_ind, meta_plus = resolve_node(data, child_ind)
        meta += meta_plus
    for i in range(n_meta):
        meta += data[child_ind+i]
    
    return child_ind + n_meta, meta        

def resolve_node2(data, ind):
    meta = 0
    n_childs = data[ind]
    n_meta = data[ind+1]
    child_ind = ind+2 # first child ind

    if n_childs == 0:
        for i in range(n_meta):
            meta += data[child_ind+i]    
        return child_ind + n_meta, meta        

    child_vals = []
    for i in range(n_childs): #resolve all childs
        child_ind, meta_plus = resolve_node2(data, child_ind)
        child_vals.append(meta_plus)
        
    for i in range(n_meta):
        if data[child_ind+i]-1 < len(child_vals) and data[child_ind+i]-1 >= 0:
            meta += child_vals[data[child_ind+i]-1]
    return child_ind + n_meta, meta            

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    inp = f.read().rstrip()
    data = [int(d) for d in inp.split(' ')]

#p1
cind, meta = resolve_node(data, 0)
print(meta)    

#p2
cind, meta = resolve_node2(data, 0)
print(meta)    
