import os
import sys

def fully_react(clist):
    ind = 0
    while ind+1 < len(clist):
        if clist[ind].upper() == clist[ind+1].upper():
            if clist[ind] != clist[ind+1]:
                clist.pop(ind)
                clist.pop(ind)
                if ind > 0:
                    ind -= 1
            else:
                ind += 1                
        else:
            ind += 1  
    return clist

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    cont = f.read()
    clist = list(cont[:-1])

out = fully_react(clist.copy())                             
print(len(out))

allc = 'abcdefghijklmnopqrstuvwxyz'
plength = []
for cthis in allc:   
    list1 = [a for a in clist if a.upper() != cthis.upper()]
    list1 = fully_react(list1)
    plength.append(len(list1))

print(min(plength))
