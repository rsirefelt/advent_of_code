import bisect

max_cal = [0, 0, 0]
curr_cal = 0
with open("input") as f:
    for i in f:
        if i != "\n":
            curr_cal += int(i)
        else:
            if(curr_cal > max_cal[0]):
                bisect.insort(max_cal, curr_cal)
                max_cal.pop(0)
            curr_cal = 0

print(sum(max_cal))
