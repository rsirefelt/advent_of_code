import sys
import os
import numpy as np
import re
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils.misc import keywithmaxval

pat = re.compile(r"^\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)")

guard_info = []

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        mm = pat.match(line)
        aa = datetime.datetime(int(mm.group(1)),int(mm.group(2)), int(mm.group(3)), int(mm.group(4)), int(mm.group(5)))
        
        guard_info.append({'tt': aa, 'ss': mm.group(6)})        
    
# sort    
guard_info = sorted(guard_info, key=lambda k: k['tt']) 

pat = re.compile(r"Guard #(\d+) begins shift")
guard_sleep = {}
guard_sleep_tot = {}
current_guard = None
for cc,gi in enumerate(guard_info):
    mm = pat.match(gi['ss'])
    if mm:
        current_guard = int(mm.group(1))
    if gi['ss'] == 'wakes up':
        when_sleep = np.zeros((60,))
        when_sleep[guard_info[cc-1]['tt'].minute:guard_info[cc]['tt'].minute] = 1
        if current_guard in guard_sleep_tot:
            guard_sleep_tot[current_guard] += int((guard_info[cc]['tt']-guard_info[cc-1]['tt']).total_seconds()/60)
            guard_sleep[current_guard].append(when_sleep)
        else:
            guard_sleep_tot[current_guard] = int((guard_info[cc]['tt']-guard_info[cc-1]['tt']).total_seconds()/60)
            guard_sleep[current_guard] = [when_sleep]


max_key = keywithmaxval(guard_sleep_tot)
min_sum = np.zeros((60,))
for d_sum in guard_sleep[max_key]:
    min_sum += d_sum

sleepy_minute = min_sum.argmax()
print(sleepy_minute*max_key)

guard_sleep_tot = {}
for key, gs in guard_sleep.items():
    min_sum = np.zeros((60,))
    for d_sum in gs:
        min_sum += d_sum

    sleepy_minute = min_sum.argmax()
    tot_sleep = min_sum.max()
    guard_sleep_tot[key] = (tot_sleep, sleepy_minute)      

curr_max = 0
curr_min = None
curr_guard = None
for key, val in guard_sleep_tot.items():
    if val[0] > curr_max:
        curr_max = val[0]
        curr_guard = key
        curr_min =  val[1]

print(curr_min*curr_guard)    