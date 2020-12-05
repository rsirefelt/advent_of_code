import itertools


def main():
    fields = [
        r"ecl:\S+\s",
        r"pid:\S+\s",
        r"eyr:\S+\s",
        r"hcl:\S+\s",
        r"byr:\S+\s",
        r"iyr:\S+\s",
        r"(?:cid:\S+\s)?",
        r"hgt:\S+\s",
    ]
    s = ""
    for fs in itertools.permutations(fields):
        s += r"(?:%s(?:\n|$))|" % r"".join(fs)
    s = s[:-1]
    with open("regex.txt", "w") as f:
        f.write(s)

if __name__ == "__main__":
    main()
