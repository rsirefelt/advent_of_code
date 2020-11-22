import sys
import os
import numpy as np
import re
import datetime

def isfullfilled(req, order):
    isf = True
    for let in req:
        if let not in order:
            isf = False
    return isf            

def addtoworker(workers, let):
    for worker in workers:
        if worker['task'] == let:
            return
    for worker in workers:
        if worker['task'] == '.':
            worker['task'] = let
            worker['timeleft'] = ord(let)-4
            break

def updateworkers(workers):  
    doneletters = []
    for worker in workers:
        if worker['task'] != '.':          
            worker['timeleft'] -= 1
            if worker['timeleft'] == 0:
                doneletters.append(worker['task'])
                worker['task'] = '.'
    return doneletters                



pat = re.compile(r"^Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

allc = 'abcdefghijklmnopqrstuvwxyz'.upper()
reqs = {}
for cc in allc:
    reqs[cc] = []

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        mm = pat.match(line)
        if mm:
            bef = mm.group(1)
            aft = mm.group(2)

            if aft in reqs:
                reqs[aft].append(bef)

order = []
reqs2 = reqs.copy()

while len(reqs) > 0:
    kk = list(reqs.keys())
    kk.sort()
    for k in kk:
        let = k
        req = reqs[k]

        if isfullfilled(req, order):
            order.append(let)
            del reqs[let]
            break

print(''.join(order))

workers = []
for i in range(5):
    workers.append({'task': '.', 'timeleft': 0})

time = 0
order = []
while len(reqs2) > 0:
    kk = list(reqs2.keys())
    kk.sort()
    for k in kk:
        let = k
        req = reqs2[k]
        if isfullfilled(req, order):
            addtoworker(workers, let)
    doneletters = updateworkers(workers)     
    order += doneletters      
    for let in doneletters:
        del reqs2[let]
    time += 1
print(len(order))
print(time)            

