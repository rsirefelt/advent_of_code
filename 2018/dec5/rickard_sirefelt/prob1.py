with open("dec5/rickard_sirefelt/input.txt") as f:
    polymer = f.readline().rstrip()

polymer_ord = [ord(unit) for unit in polymer]
i = 0
while i + 1 < len(polymer_ord):
    if abs(polymer_ord[i] - polymer_ord[i + 1]) == 32:
        del polymer_ord[i:i + 2]
        i -= 1
    else:
        i += 1

print(len(polymer_ord))
