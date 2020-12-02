# Hey!!!
# Welcome to the day2 solution of a very handsome coding god

import re


num_valid_1 = 0
num_valid_2 = 0
with open("input.txt", "r") as f:
    for line in f:
        # Python split parsing
        lim, char, passw = line.rstrip().replace(":", "").split(" ")
        d1, d2 = map(int, lim.split("-"))

        # Python regexp parsing
        p = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")
        d1, d2, char, passw = p.match(line).groups()
        d1, d2 = int(d1), int(d2)

        # Part 1 password policy check
        num_char = passw.count(char)
        if d1 <= num_char <= d2:
            num_valid_1 += 1

        # Part 2 password policy check
        valid = False
        if len(passw) > d1 - 1:
            if passw[d1 - 1] == char:
                valid = True
            if len(passw) > d2 - 1 and passw[d2 - 1] == char:
                valid = not valid
        num_valid_2 += int(valid)


print(f"1) Number of valid passwords: {num_valid_1}")
print(f"2) Number of valid passwords: {num_valid_2}")
