import re

rules = {}
nearby_tickets = []
my_ticket = None

rule_pat = re.compile('([ \w]+): (\d+)-(\d+) or (\d+)-(\d+)')
input_mode = 0
with open('inputs/day16') as f:
    for line in f:
        if line.rstrip() == '':
            input_mode += 1
            continue
        elif input_mode == 0:
            content = rule_pat.match(line.rstrip()).groups()
            rules[content[0]] = [int(c) for c in content[1:]]
        elif input_mode == 1:
            if line.startswith('your'):
                continue
            my_ticket = [int(c) for c in line.rstrip().split(',')]
        elif input_mode == 2:
            if line.startswith('nearby'):
                continue
            nearby_tickets.append([int(c) for c in line.rstrip().split(',')])

scanning_error_rate = 0
valid_tickets = []
for ticket in nearby_tickets:
    valid_ticket = True
    for val in ticket:
        valid = False
        for rv in rules.values():
            if rv[1] >= val >= rv[0] or rv[3] >= val >= rv[2]:
                valid = True
                break
        if not valid:
            valid_ticket = False
            scanning_error_rate += val
    if valid_ticket:
        valid_tickets.append(ticket)

print(f'a) {scanning_error_rate}')

valid_rules_for_index = {i: [] for i in range(len(rules))}
for i in range(len(my_ticket)):
    for rule_name, rv in rules.items():
        rule_valid = True
        for ticket in valid_tickets:
            if not (rv[1] >= ticket[i] >= rv[0] or rv[3] >= ticket[i] >= rv[2]):
                rule_valid = False
                break  # next rule

        if rule_valid:
            valid_rules_for_index[i].append(rule_name)
            # break  # next index

rules_in_order = [None]*len(rules)
while True:  # assign rules with only one valid index first
    rule_to_remove = None
    for index, valid_rules in valid_rules_for_index.items():
        if len(valid_rules) == 1:
            rule_to_remove = valid_rules[0]
            rules_in_order[index] = rule_to_remove
            break

    for rules in valid_rules_for_index.values():
        if rule_to_remove in rules:
            rules.remove(rule_to_remove)

    if all([r is not None for r in rules_in_order]):
        break

ruleprod = 1
for i, rule in enumerate(rules_in_order):
    if rule.startswith('departure'):
        ruleprod *= my_ticket[i]

print(f'b) {ruleprod}')
