import re
import numpy as np

with open("input.txt", "r") as f:
    input_ = f.read().split("\n\n")

p_rule = re.compile(r"([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")

rules = []
for line in input_[0].split("\n"):
    t, l1, h1, l2, h2 = re.match(p_rule, line).groups()
    rules.append([t, [int(l1), int(h1)], [int(l2), int(h2)]])

my_ticket = [int(i) for i in input_[1].split("\n")[1].split(",")]

nearby_tickets = []
for line in input_[2].split("\n")[1:]:
    nearby_tickets.append([int(i) for i in line.split(",")])

sort_rules = np.sort(np.array([r[1:] for r in rules]).reshape(-1, 2), axis=0)
valid_ranges = []
for s, e in sort_rules:
    if valid_ranges and s < valid_ranges[-1][1]:
        valid_ranges[-1][1] = max(e, valid_ranges[-1][1])
    else:
        valid_ranges.append([s, e])

valid_ranges = [range(s, e + 1) for s, e in valid_ranges]

invalid_nums = []
valid_tickets = [my_ticket]
for ticket in nearby_tickets:
    invalid_ticket = False
    for n in ticket:
        invalid_num = True
        for range_ in valid_ranges:
            if n in range_:
                invalid_num = False
                break
        if invalid_num:
            invalid_ticket = True
            invalid_nums.append(n)
    if not invalid_ticket:
        valid_tickets.append(ticket)


rules = [[t, range(r1[0], r1[1] + 1), range(r2[0], r2[1] + 1)] for t, r1, r2 in rules]
valid_tickets = np.array(valid_tickets).T.tolist()

departure_nums = []
assigned_cols = []
while len(assigned_cols) != len(valid_tickets):
    for j, r in enumerate(rules):
        valid_cols = []
        for i, col in enumerate(valid_tickets):
            if i in assigned_cols:
                continue
            valid_col = True
            for n in col:
                if n not in r[1] and n not in r[2]:
                    valid_col = False
                    break
            if valid_col:
                valid_cols.append(i)
        if len(valid_cols) == 1:
            if r[0].split()[0] == "departure":
                departure_nums.append(my_ticket[valid_cols[0]])
            assigned_cols.append(valid_cols[0])
            del rules[j]


print(f"1) Ticket scanning error rate {sum(invalid_nums)}")
print(f"2) Multiply number {np.prod(departure_nums)}")
