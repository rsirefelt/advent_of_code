import re


def parse_input(input_file):
    with open(input_file, 'r') as fp:
        split = fp.read().split('\n\n')
        text_rules = split[0].replace('"', '')
        text_messages = split[1]

    rules = {}
    for rule_raw in text_rules.split('\n'):
        split = rule_raw.split(':')
        rules[int(split[0])] = split[1].strip()

    messages = text_messages.split('\n')[:-1]
    return rules, messages


def create_regex(rules, ind):
    regex = r''
    rule = rules[ind]
    has_or = '|' in rule
    dr = r'' 
    if has_or:
        or_split = rule.split('|')
        for n in or_split[0].strip().split(' '):
            ddr = create_regex(rules, int(n))
            dr += ddr
        dr += '|'
        for n in or_split[1].strip().split(' '):
            ddr = create_regex(rules, int(n))
            dr += ddr
        regex += '(' + dr + ')'
    else:
        if rule.isalpha():
            dr += rule
        else:
            nsplit = rule.split(' ')
            for n in nsplit:
                dr += create_regex(rules, int(n))
        regex += dr
    return regex


def attempt_match(message, reg31, reg42):
    """ Bruteforce search bounded by the message length. """
    len_m = len(message)
    len_8 = 8
    len_11 = 16
    ni = len_m // len_8
    nj = len_m // len_11
    for i in range(1, ni + 1):
        for j in range(1, nj + 1):
            if i*len_8 + j*len_11 > len_m:
                continue
            reg = i*reg42 + j*reg42 + j*reg31
            match = re.search(reg, message)
            if match:
                if match.group(0) == message:
                    return True
    return False


if __name__ == "__main__":

    rules, messages = parse_input('./input_day19.txt')

    # Part I
    regex = create_regex(rules, 0)
    count = 0
    for mess in messages:
        if match := re.search(regex, mess):
            if match.group(0) == mess:
                count += 1
    print(count)

    # Part II
    # rule 0: 8 11, rule 8: 42 | 42 8, rule 11: 42 31 | 42 11 31
    # => rules are sequences of the form (42 x i) (42 x j) (31 x j)
    reg31 = create_regex(rules, 31) 
    reg42 = create_regex(rules, 42)
    count = 0
    for mess in messages:
        match = attempt_match(mess, reg31, reg42)
        if match:
            count += 1
    print(count)
