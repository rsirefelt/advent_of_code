elfs = []

with open("input") as f:
    elf = 0
    for line in f:
        line = line.strip()
        if line:
            elf += int(line)
        else:
            elfs.append(elf)
            elf = 0

elfs = sorted(elfs, reverse=True)
max_elf = elfs[0]
max_3_elfs = elfs[0] + elfs[1] + elfs[2]

print("max_elf=", max_elf)
print("max_3_elfs=", max_3_elfs)
