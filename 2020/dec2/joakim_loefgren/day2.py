"""
Advent of code day 2
"""


def load_input(input_file="input_day2.txt"):
    entries = []
    with open(input_file) as fd:
        for line in fd:
            policy = line.split(":")[0].strip()
            password = line.split(":")[1].strip()
            entries.append((policy, password))

    return entries


def parse_policy(policy):
    letter = policy[-1]
    num1, num2 = policy[:-1].split("-")
    return letter, int(num1), int(num2)


def validate_sled(entries):
    num_valid = 0
    for policy, password in entries:
        letter, lmin, lmax = parse_policy(policy)
        if lmin <= password.count(letter) <= lmax:
            num_valid += 1

    return num_valid


def validate_official(entries):
    num_valid = 0
    for policy, password in entries:
        letter, pos1, pos2 = parse_policy(policy)
        if (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter):
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    entries = load_input()

    # Part I
    print(validate_sled(entries))

    # Part II
    print(validate_official(entries))
