import numpy as np

max_cal = 0
curr_cal = 0
with open("input") as f:
    for i in f:
        if i != "\n":
            curr_cal += int(i)
        else:
            if(curr_cal > max_cal):
                max_cal = curr_cal
            curr_cal = 0

print(max_cal)
