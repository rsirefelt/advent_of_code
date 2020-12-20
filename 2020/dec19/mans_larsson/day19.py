from os import truncate
from typing import Set


def check_message_b(message, rule_31, rule_42):
    """c is index 8, rule 42 | 42 8, at least one repeat of rule 42
       d is index 11, rule 42 31 | 42 11 31, a series of 42s followed by the same number of 31s, at least one of each

       allowed message is cd, rule 31 and 42 have no c:s or d:s

       in summary, message needs to start with two or more repeats of 42, then end with at least one repeat of 31
       there has to be atleast one more 42 than 31 """

    rule_len = len(list(rule_31)[0])
    if message[-rule_len:] not in rule_31:
        return False

    only_31s_from_now = False
    rule42_count = 0
    rule31_count = 1
    for i in range(0, len(message) - rule_len, rule_len):
        if not only_31s_from_now:
            if message[i:i+rule_len] in rule_42:
                rule42_count += 1
            else:
                only_31s_from_now = True
        if only_31s_from_now:
            if message[i:i+rule_len] in rule_31:
                rule31_count += 1
            else:
                return False

    return rule42_count > rule31_count


rules = {}
messages = []

allrules = False
with open('inputs/day19') as f:
    for line in f:
        if allrules:
            messages.append(line.rstrip())
        else:
            if line == '\n':
                allrules = True
                continue
            linel = line.rstrip().split(':')
            rules[int(linel[0])] = linel[1].replace('"', ' ').strip()


def decode_from_list_of_indices(indices):
    allowed_messages = set()
    for ind in indices.strip().split(' '):
        next_parts = decode_rules(int(ind))
        if len(allowed_messages) == 0:
            allowed_messages = next_parts
        else:
            new_messages = set()
            for part1 in allowed_messages:
                for part2 in next_parts:
                    new_messages.add(part1+part2)
            allowed_messages = new_messages
    return allowed_messages


def decode_rules(this_index):
    """recursively decode rules, changes values in rules to avoid decoding same rule twice"""
    this_rule = rules[this_index]
    if isinstance(this_rule, Set):
        return this_rule
    if this_rule == 'a' or this_rule == 'b' or this_rule == 'c' or this_rule == 'd':
        rules[this_index] = set(this_rule)
        return set(this_rule)

    if '|' in this_rule:
        ors = this_rule.split('|')
        allowed_messages = set()
        allowed_messages.update(decode_from_list_of_indices(ors[0]))
        allowed_messages.update(decode_from_list_of_indices(ors[1]))

    else:
        allowed_messages = decode_from_list_of_indices(this_rule)
    rules[this_index] = allowed_messages
    return allowed_messages


allowed_messages = decode_rules(0)
count = 0
for message in messages:
    if message in allowed_messages:
        count += 1

print(f"a) {count}")

rule_42 = decode_rules(42)  # no c or d
rule_31 = decode_rules(31)  # no c or d
count = 0
for message in messages:
    if check_message_b(message, rule_31, rule_42):
        count += 1

print(f"b) {count}")
