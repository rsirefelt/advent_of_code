
def get_char_val(char):
  if char.islower():
    return int(ord(char)) - 97 + 1
  else:
    return int(ord(char)) - 65 + 27

def get_intersecting_char_p1(line):
    num_items = len(line)
    num_items_comp = int(num_items / 2)
    comp1 = line[0:num_items_comp]
    comp2 = line[num_items_comp:]
    char = list(set(comp1).intersection(set(comp2)))[0]
    return char

def get_intersecting_char_p2(group):
    char = set.intersection(*[set(g) for g in group])
    char = list(char)[0]
    return char

total_sum_p1 = 0
total_sum_p2 = 0
with open("input.txt", "r") as f:
  lines = f.readlines()
  group = []
  for idx, line in enumerate(lines):
    line = line.strip()
    char_p1 = get_intersecting_char_p1(line)
    total_sum_p1 += get_char_val(char_p1)
    group.append(line)
    if len(group) == 3:
      char_p2 = get_intersecting_char_p2(group)
      total_sum_p2 += get_char_val(char_p2)
      group = []
print(total_sum_p1)
print(total_sum_p2)