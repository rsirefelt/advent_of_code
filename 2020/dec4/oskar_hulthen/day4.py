import regex as re


def task(task=1):
    valid_count = 0
    current_passport = {}
    with open("input") as f:
        lines = list(f.readlines())

        # Add last newline (to not have to individually check last passport)
        lines.append("\n")
        for line in lines:
            line = line.rstrip()
            if line == "":
                if valid(current_passport, task):
                    valid_count += 1

                current_passport = {}
                continue

            entries = line.split(" ")

            for entry in entries:
                key, value = entry.split(":")
                current_passport[key] = value

    print(valid_count)


def valid(passport, task=1):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validation_funcs = {
        "byr": val_byr,
        "iyr": val_iyr,
        "eyr": val_eyr,
        "hgt": val_hgt,
        "hcl": val_hcl,
        "ecl": val_ecl,
        "pid": val_pid,
    }
    if task == 1:
        if all(key in passport for key in required_fields):
            return True
        return False
    elif task == 2:

        valid = True
        for key, value in passport.items():
            if not all(key in passport for key in required_fields):
                valid = False

            func = validation_funcs.get(key, empty_op)
            valid = valid and func(value)
        return valid


def empty_op(_):
    return True


def val_byr(byr):
    byr = int(byr)
    return byr >= 1920 and byr <= 2002


def val_iyr(iyr):
    iyr = int(iyr)
    return iyr >= 2010 and iyr <= 2020


def val_eyr(eyr):
    eyr = int(eyr)
    return eyr >= 2020 and eyr <= 2030


def val_hgt(hgt):
    pattern = re.findall("^([0-9]*)(cm|in)$", hgt)
    if len(pattern) == 1:
        val, metric = pattern[0]
        val = int(val)
        if metric == "in":
            return val >= 59 and val <= 76
        elif metric == "cm":
            return val >= 150 and val <= 193
    return False


def val_hcl(hcl):
    pattern = re.findall("^#([a-z0-9]{6})$", hcl)
    return len(pattern) == 1


def val_ecl(ecl):
    valids = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valids


def val_pid(pid):
    pattern = re.findall("^([0-9]{9})$", pid)
    return len(pattern) == 1


if __name__ == "__main__":
    task()
    task(2)
