prio_sum = 0

with open("input") as f:
    for line in f:
        mid = int((len(line) - 1) / 2)
        comp1 = set(line[:mid])
        comp2 = line[mid:]

        for i in comp2:
            if i in comp1:
                if i.isupper():
                    prio_sum += ord(i) - 38
                else:
                    prio_sum += ord(i) - 96
                break

print(prio_sum)
