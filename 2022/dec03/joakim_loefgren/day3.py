from string import ascii_lowercase, ascii_uppercase

prios = {c: i + 1 for i, c in enumerate(ascii_lowercase)}
prios.update({c: i + 27 for i, c in enumerate(ascii_uppercase)})

# part I
prio_sum = 0
with open('./input.txt') as fp:
    lines = fp.read().splitlines()

for line in lines:
    line = line.strip()
    bag1 = set(line[:len(line)//2])
    bag2 = set(line[len(line)//2:])
    common = set.intersection(bag1, bag2).pop()
    prio_sum += prios[common]

print(prio_sum)

# part II
prio_sum = 0
groups = list(zip(*(iter(lines),) * 3))
for group in groups:
    bags = [set(s) for s in group]
    common = set.intersection(*bags).pop()
    prio_sum += prios[common]

print(prio_sum)
    
