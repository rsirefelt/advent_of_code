import re

num_overlap = 0
with open("input") as f:
    for line in f:
        [min1, max1, min2, max2] = [int(x) for x in re.findall("[0-9]+", line)]
        if (min1 >= min2 and max1 <= max2) or (min2 >= min1 and max2 <= max1):
            num_overlap += 1

print(num_overlap)
