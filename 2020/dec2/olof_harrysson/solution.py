def is_valid1(password, passpolicy):
  passlimits, letter = passpolicy.split()
  lower, upper = passlimits.split('-')
  n_letters = password.count(letter)
  valid = n_letters in range(int(lower), int(upper) + 1)

  print(password, passpolicy, n_letters, valid)
  return valid


def is_valid2(password, passpolicy):
  passlimits, letter = passpolicy.split()
  lower, upper = passlimits.split('-')
  v1 = password[int(lower) - 1] == letter
  v2 = password[int(upper) - 1] == letter

  valid = (v1 or v2) and not (v1 and v2)
  print(password, passpolicy, valid)
  return valid


with open("input.txt") as f:
  lines = f.read().splitlines()

n_valid = 0
for line in lines:
  passpolicy, password = line.split(': ')

  if is_valid2(password, passpolicy):
    n_valid += 1

print(n_valid)
print(len(lines))
