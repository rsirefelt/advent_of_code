import re

def read_passports(filename):
    passports = []
    passports.append({})
    passport_ind = 0
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        # print(data_lines)
        for string in data_lines:
            # print(string.rstrip())

            if string.rstrip() == '':
                passports.append({})
                passport_ind += 1
            else:
               fields = string.rstrip().split(' ')
               for field in fields:
                   (key,value) = field.split(':')
                   passports[passport_ind][key] = value
    return passports

def check_passports_fields(passport):
    regex_hair = re.compile('#[0-9a-f]{6}')
    regex_id = re.compile('[0-9]{9}')
    eye_colors = ('amb','blu','brn', 'gry', 'grn', 'hzl', 'oth')
    valid = True
    for key, value in passport.items():

        if key == 'byr':
            year = int(value)
            valid = valid and (1920  <= year <= 2002)

        elif key == 'iyr':
            year = int(value)
            valid = valid and  (2010  <= year <= 2020)
        
        elif key == 'eyr':
            year = int(value)
            valid =  valid and (2020  <= year <= 2030)
        
        elif key == 'hgt':
            height = int(value[:-2])
            unit = value[-2:]
            if unit == 'cm':
                valid = valid and (150  <= height <= 193)
            elif unit == 'in':
                valid = valid and  (59  <= height <= 76)
            else:
                valid =  valid and False
        
        elif key == 'hcl':
            valid =  valid and bool(regex_hair.match(value))
        
        elif key == 'ecl':
            valid =  valid and value in eye_colors
        
        elif key == 'pid':
            valid =  valid and bool(regex_id.match(value)) and len(value) == 9
    return valid

def check_if_valid(passports, needed_fields):
    valid_passports = 0
    for passport in passports:
        if all(needed_field in passport for needed_field in needed_fields):
            valid_passports += 1
    return valid_passports

def check_if_valid_2(passports, needed_fields):
    valid_passports = 0
    for passport in passports:
        if all(needed_field in passport for needed_field in needed_fields):
        
            if check_passports_fields(passport):
                valid_passports += 1
    return valid_passports

def main():
    needed_fields = ('byr','iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid')
    # passports = read_passports('testdata.csv')
    passports = read_passports('data.csv')
    valid_passports = check_if_valid(passports, needed_fields )
    print('Part1 valid passwords: %i' %valid_passports)

    valid_passports = check_if_valid_2(passports, needed_fields )
    print('Part2 valid passwords: %i' %valid_passports)

if __name__ == "__main__": main()