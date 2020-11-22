import sys
import os
import numpy as np


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import utils.misc

freq = 0
change_list = []
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'in.txt')) as f:
    for line in f:
        change_list.append(int(line[:-1]))
        if line[0] == '+':
            freq += int(line[1:-1])
        if line[0] == '-':
            freq -= int(line[1:-1])
            
print(freq) 

freq = 0
list_of_freqs = []
count = 0
while True:
    freq += change_list[count]
    if freq in list_of_freqs:
        break
    else:
        list_of_freqs.append(freq)
    count = (count + 1) % len(change_list)
print(freq)    



