import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

lines = [line[:-1] for line in lines]
lines.append('')

food_supplies = []
curr_elf = []
for line in lines:
    if line == '':
        food_supplies.append(curr_elf)
        curr_elf = []
    else:
        curr_elf.append(int(line))

food_supplies = [np.array(elf) for elf in food_supplies]
total_foods = [np.sum(elf) for elf in food_supplies]

print("Part 1: " + str(np.max(total_foods)))

print("Part 2: " + str(np.sum(np.sort(total_foods)[-3:])))

xxx = 3