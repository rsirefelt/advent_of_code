prio_sum = 0
rucksacks = [set(), set(), set()]

with open("input") as f:
    for i, line in enumerate(f):
        grp_idx = i % 3
        rucksacks[grp_idx] = set(line.strip())
            
        if grp_idx == 2: # end of group:
            badge = list(rucksacks[0].intersection(rucksacks[1]).intersection(rucksacks[2]))[0]
            if badge.isupper():
                prio_sum += ord(badge) - 38
            else:
                prio_sum += ord(badge) - 96

print(prio_sum)
