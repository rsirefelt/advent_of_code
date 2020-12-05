import itertools


def main():
    fields = [
        # exactly one of: amb blu brn gry grn hzl oth.
        r"ecl:(?:amb|blu|brn|gry|grn|hzl|oth)\s",
        # a nine-digit number, including leading zeroes.
        r"pid:\d{9}\s",
        # four digits; at least 2020 and at most 2030.
        r"eyr:20(?:2\d|30)\s",
        # a # followed by exactly six characters 0-9 or a-f.
        r"hcl:#[0-9a-f]{6}\s",
        # four digits; at least 1920 and at most 2002.
        r"byr:(?:19[2-9]\d|200[0-2])\s",
        # four digits; at least 2010 and at most 2020.
        r"iyr:20(?:1\d|20)\s",
        # ignored, missing or not.
        r"(?:cid:\S+\s)?",
        # hgt (Height) - a number followed by either cm or in:
        # - If cm, the number must be at least 150 and at most 193.
        # - If in, the number must be at least 59 and at most 76.
        r"hgt:(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)\s",
    ]
    s = ""
    for fs in itertools.permutations(fields):
        s += r"(?:%s(?:\n|$))|" % r"".join(fs)
    s = s[:-1]
    with open("regex.txt", "w") as f:
        f.write(s)

if __name__ == "__main__":
    main()
