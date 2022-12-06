def generate_elf_set(elf):
  elf = [int(e) for e in elf.split("-")]
  if elf[0] == elf[1]:
    elf = set([int(elf[0])])
  else:
    elf = set(range(elf[0], elf[1] + 1))
  return elf

enclosed_sets = 0
overlapping_sets = 0
with open("input.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    elf1, elf2 = line.split(",")
    elf1 = generate_elf_set(elf1)
    elf2 = generate_elf_set(elf2)
    inters = elf1.intersection(elf2)
    if len(inters) > 0:
      overlapping_sets += 1
    if len(inters) == min(len(elf1), len(elf2)):
      enclosed_sets += 1
print(enclosed_sets)
print(overlapping_sets)