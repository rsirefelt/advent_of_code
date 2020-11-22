import sys
import os
import numpy as np

def contains23(line):
    dd = {}
    for i in range(len(line)-1):
        if line[i] in dd:
            dd[line[i]] += 1
        else:
            dd[line[i]] = 1
    a=0
    b=0            
    for k,v in dd.items():
        if v == 2:
            a = 1
        if v == 3:
            b = 1
    return a,b                        

def checkmatch(id1, id2):

    strr = ''
    for a,b in zip(id1,id2):
        if a == b:
            strr += a

    if len(strr) + 1 == len(id1):
        return strr
    else:
        return None

count2 = 0
count3 = 0
all_ids = []
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        a,b = contains23(line)
        count2 += a
        count3 += b

        all_ids.append(line[:-1])

print(count2*count3)   

for i in range(len(all_ids)):
    for j in range(len(all_ids)):
        if i != j:
            match = checkmatch(all_ids[i], all_ids[j])
            if match:                
                break
    if match:                
        break                
                
print(match)
