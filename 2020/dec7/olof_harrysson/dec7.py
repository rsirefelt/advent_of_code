from collections import defaultdict


def bag_continers(bags_dict, bag_name):
  bag_names = set((bag_name, ))
  for parent_bag in bags_dict[bag_name]:
    bag_names |= bag_continers(bags_dict, parent_bag)
  return bag_names


def count_bags(bags_dict, bag_name):
  n_bags = 1
  for child_bag, number_bags in bags_dict[bag_name]:
    bag_capacity = count_bags(bags_dict, child_bag)
    n_bags += number_bags * bag_capacity

  return n_bags


with open("input.txt") as f:
  lines = f.read().splitlines()

# Child -> Parents
parent_bags = defaultdict(list)

# Parent -> Children
children_bags = defaultdict(list)

for line in lines:
  src_bag, dest_bags = line.split(' contain ')
  src_bag = src_bag.replace(' bags', '')

  if dest_bags == 'no other bags.':
    child_bags = {}
  else:
    child_bags = {
      ' '.join(bag.split()[1:-1]): bag.split()[0]
      for bag in dest_bags.split(',')
    }

  for bag_name, bag_number in child_bags.items():
    parent_bags[bag_name].append(src_bag)
    children_bags[src_bag].append((bag_name, int(bag_number)))

# Part1
root_bag = 'shiny gold'
parent_bags = bag_continers(parent_bags, root_bag)
parent_bags -= set((root_bag, ))
print(parent_bags)
print(len(parent_bags))

# Part2
n_bags = count_bags(children_bags, root_bag)
print(n_bags - 1)  # For the shiny gold
