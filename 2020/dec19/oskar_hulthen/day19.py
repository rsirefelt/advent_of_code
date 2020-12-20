import re


def count_matches(pattern, messages):
    sum_ = 0
    for message in messages:
        message = message.rstrip()
        sum_ += len(re.findall(pattern, message))
    return sum_


def parse_rules(in_rules):
    rules = in_rules.copy()
    # Parse list to regex string:
    applied_rules = get_rule(0, rules, {})
    # Add start & end
    return "^" + applied_rules + "$"


def get_rule(rule_idx, rules, memory, i=0):
    entry = rules[rule_idx]
    solved = memory.get(rule_idx, 0)
    # if it is already parsed, return it.
    if solved:
        return entry

    if isinstance(entry, str):
        memory[rule_idx] = True
        return entry

    new_regex = []
    for rule in entry:
        if isinstance(rule, list):
            # Combination of rules.
            sub_strings = []
            for subrule in rule:
                sub_strings.append(get_rule(subrule, rules, memory, i + 1))

                # Handle recursion depth (limited to 20)
                if i + 1 == 20:
                    return ""

            # Merge the combination into one string.
            new_regex.append("".join(sub_strings))

        else:
            new_regex.append(get_rule(rule, rules, memory))
    # Several rules, means options separate with |.
    new_regex = f"({'|'.join(new_regex)})"
    rules[rule_idx] = new_regex
    memory[rule_idx] = True
    return new_regex


if __name__ == "__main__":
    rules = {}
    with open("input") as f:
        lines = list(f.readlines())
        num_lines = len(lines)
        # Load rules
        for i in range(0, num_lines):
            line = lines[i]
            # print(line)
            line = line.rstrip()
            if line == "":
                break
            line = line.split(": ")
            rule = int(line[0])

            conditions = []
            for cond in line[1].split(" | "):
                # Split condition on space
                conds = cond.split(" ")
                if len(conds) == 1:
                    single = conds[0].strip('"')
                    if single in "ab":
                        conditions = single
                    else:
                        conditions.append(int(single))
                else:
                    conditions.append([int(c) for c in conds])

            rules[rule] = conditions
        # Load message
        messages = lines[i:num_lines]

    task1_rules = parse_rules(rules)
    print(f"Result task 1: {count_matches(task1_rules, messages)}")

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    task2_rules = parse_rules(rules)
    print(f"Result task 2: {count_matches(task2_rules, messages)}")
