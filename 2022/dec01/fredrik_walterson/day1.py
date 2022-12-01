
with open("input.txt", "r") as f:
  lines = f.readlines()
  elf_counter = 0
  elfs = {}
  for line in lines:
    if line == '\n':
      elf_counter += 1
    else:
      calories = int(line.split("\n")[0])
      if elf_counter in elfs:
        elfs[elf_counter] += calories
      else:
        elfs[elf_counter] = calories

sorted_elfs = dict(sorted(elfs.items(), key=lambda item: item[1], reverse=True))
elf_vals = list(sorted_elfs.values())

# Part 1.
print(elf_vals[0])

# Part 2.
print(sum(elf_vals[0:3]))
