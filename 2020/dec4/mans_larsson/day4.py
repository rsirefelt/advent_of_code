import re

passports = []
passport = dict()

with open('inputs/day4') as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            passports.append(passport)
            passport = dict()
        else:
            key_vals = line.split(' ')
            for key_val in key_vals:
                key_val = key_val.split(':')
                passport[key_val[0]] = key_val[1]
if len(passport) != 0:
    passports.append(passport)

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def evaluate_passport(passport):
    for field in required_fields:
        if field not in passport:
            return False
    return True


count = 0
for passport in passports:
    if evaluate_passport(passport):
        count += 1

print(f'a) valid passports {count}')


def eval_byr(str):
    if len(str) != 4:
        return False
    year = int(str)
    return year >= 1920 and year <= 2002


def eval_iyr(str):
    if len(str) != 4:
        return False
    year = int(str)
    return year >= 2010 and year <= 2020


def eval_eyr(str):
    if len(str) != 4:
        return False
    year = int(str)
    return year >= 2020 and year <= 2030


def eval_hgt(str):
    if str[-2:] == 'cm':
        if len(str) != 5:
            return False
        hgt = int(str[:3])
        return hgt >= 150 and hgt <= 193
    elif str[-2:] == 'in':
        if len(str) != 4:
            return False
        hgt = int(str[:2])
        return hgt >= 59 and hgt <= 76
    else:
        return False


hcl_exp = re.compile('#[\da-z]{6}')


def eval_hcl(str):
    if re.fullmatch(hcl_exp, str) is not None:
        return True
    else:
        return False


def eval_ecl(str):
    return str in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


pid_exp = re.compile('[\d]{9}')


def eval_pid(str):
    if re.fullmatch(pid_exp, str) is not None:
        return True
    else:
        return False


eval_fcts = {'byr': eval_byr, 'iyr': eval_iyr, 'eyr': eval_eyr,
             'hgt': eval_hgt, 'hcl': eval_hcl, 'ecl': eval_ecl, 'pid': eval_pid}


def evaluate_passport_b(passport):
    for field, fun in eval_fcts.items():
        if field not in passport or not fun(passport[field]):
            return False
    return True


count = 0
for passport in passports:
    if evaluate_passport_b(passport):
        count += 1

print(f'b) valid passports {count}')
