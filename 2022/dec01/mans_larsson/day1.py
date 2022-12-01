all_elves = []
with open('inputs/day1') as f:
    this_elf = []
    for line in f:
        data = line.rstrip()
        if len(data) == 0:
            all_elves.append(this_elf)
            this_elf = []
        else:
            this_elf.append(int(data))

cal_per_elf = [sum(elf) for elf in all_elves]
print(max(cal_per_elf))
print(sum(sorted(cal_per_elf)[-3:]))
