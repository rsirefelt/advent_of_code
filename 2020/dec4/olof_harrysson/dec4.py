with open("input.txt") as f:
  passports = f.read().split('\n\n')
  passports = [line.replace('\n', ' ') for line in passports]


def check_height(x):
  if 'cm' in x:
    h = x.replace('cm', '')
    if h.isdigit() and 150 <= int(h) <= 193:
      return True
  elif 'in' in x:
    h = x.replace('in', '')
    if h.isdigit() and 59 <= int(h) <= 76:
      return True

  return False


def check_hair_color(x):
  valid = True
  chars = 'abcdef' + '0123456789'
  if x[0] != '#' or len(x[1:]) != 6:
    valid = False

  for c in x[1:]:
    if c not in chars:
      valid = False
  return valid


val_rules = {
  "byr": lambda x: x.isdigit() and len(x) == 4 and 1920 <= int(x) <= 2002,
  "iyr": lambda x: x.isdigit() and len(x) == 4 and 2010 <= int(x) <= 2020,
  "eyr": lambda x: x.isdigit() and len(x) == 4 and 2020 <= int(x) <= 2030,
  "hgt": check_height,
  "hcl": check_hair_color,
  "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
  "pid": lambda x: x.isdigit() and len(x) == 9,
  "cid": lambda x: True,
}

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

n_valids = 0
for passport in passports:
  fields = req_fields + optional_fields
  for field in passport.split():
    field_id, field_val = field.split(':')

    if not val_rules[field_id](field_val):
      print(field_id)
      break

    fields.remove(field_id)

  for opt_field in optional_fields:
    if opt_field in fields:
      fields.remove(opt_field)

  if not fields:
    n_valids += 1

print(len(passports))
print(n_valids)
