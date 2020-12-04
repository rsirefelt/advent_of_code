def validate1(p):
    return set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')).issubset(p.keys())

def validate2(p):
    if not 1920 <= int(p['byr']) <= 2002: return False
    if not 2010 <= int(p['iyr']) <= 2020: return False
    if not 2020 <= int(p['eyr']) <= 2030: return False
    if p['hgt'].endswith('in'):
        if not 59 <= int(p['hgt'][:-2]) <= 76: return False
    elif p['hgt'].endswith('cm'):
        if not 150 <= int(p['hgt'][:-2]) <= 193: return False
    else:
        return False
    if not p['hcl'].startswith('#') or not all(c in "0123456789abcdef" for c in p['hcl'][1:]): return False
    if not p['ecl'] in set(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')): return False
    if not len(p['pid']) == 9 or not p['pid'].isdigit(): return False
    return True

with open('input', 'r') as f:
    passports = [dict(attr.split(':', 1) for attr in passport) for passport in [x.replace('\n', ' ').strip().split(' ') for x in f.read().split('\n\n')]]
    valid1 = [x for x in passports if validate1(x)]
    print('Part 1: ' + str(len(valid1)))
    print('Part 2: ' + str(list(map(validate2, valid1)).count(True)))
