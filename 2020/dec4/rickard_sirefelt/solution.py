import re

req_pass_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def pass_check1(pass_entry):
    return req_pass_set <= pass_entry.keys()


def pass_check2(pass_entry):
    valid = False
    if req_pass_set <= pass_entry.keys():
        byr = (
            re.match(r"^\d{4}$", pass_entry["byr"])
            and 1920 <= int(pass_entry["byr"]) <= 2002
        )
        iyr = (
            re.match(r"^\d{4}$", pass_entry["iyr"])
            and 2010 <= int(pass_entry["iyr"]) <= 2020
        )
        eyr = (
            re.match(r"^\d{4}$", pass_entry["eyr"])
            and 2020 <= int(pass_entry["eyr"]) <= 2030
        )
        hgt = False
        if re.match(r"^\d{3}cm$", pass_entry["hgt"]):
            hgt = 150 <= int(pass_entry["hgt"][:-2]) <= 193
        elif re.match(r"^\d{2}in$", pass_entry["hgt"]):
            hgt = 59 <= int(pass_entry["hgt"][:-2]) <= 76
        hcl = re.match(r"^#[a-f0-9]{6}$", pass_entry["hcl"])
        ecl = pass_entry["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        pid = re.match(r"^\d{9}$", pass_entry["pid"])

        valid = byr and iyr and eyr and hgt and hcl and ecl and pid

    return valid


def nr_valid_passports(pass_check):
    nr_valid_passports = 0
    pass_entry = dict()
    with open("input.txt", "r") as f:
        for line in f:
            if line == "\n":
                if pass_check(pass_entry):
                    nr_valid_passports += 1
                pass_entry.clear()
            else:
                for field in line.rstrip().split():
                    field = field.split(":")
                    pass_entry[field[0]] = field[1]
    return nr_valid_passports


print(f"1) Number of valid passports: {nr_valid_passports(pass_check1)}")
print(f"2) Number of valid passports: {nr_valid_passports(pass_check2)}")
