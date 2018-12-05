with open("dec5/rickard_sirefelt/input.txt") as f:
    polymer = f.readline().rstrip()

polymer_ord = [ord(unit) for unit in polymer]
min_length = len(polymer_ord)
for c in range(65, 91):
    c_polymer_ord = polymer_ord.copy()
    i = 0
    while i < len(c_polymer_ord):
        if c_polymer_ord[i] == c or c_polymer_ord[i] == (c + 32):
            del c_polymer_ord[i]
        else:
            i += 1

    i = 0
    while i + 1 < len(c_polymer_ord):
        if abs(c_polymer_ord[i] - c_polymer_ord[i + 1]) == 32:
            del c_polymer_ord[i:i + 2]
            i -= 1
        else:
            i += 1

    min_length = len(
        c_polymer_ord) if len(c_polymer_ord) < min_length else min_length

print(min_length)
