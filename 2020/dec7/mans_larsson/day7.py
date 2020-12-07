import re
bags = {}  # keys: key_bag, values: bags that key_bag can be in
bags_with_counts = {}

exp_nobag = re.compile(r"([a-z ]+) bags contain no")
outer_bag_exp = re.compile(r"([a-z ]+) bags contain")
inner_bags_exp = re.compile(r"(\d+) ([a-z ]+) bags?")

with open('inputs/day7') as f:
    for line in f:
        nobag_match = exp_nobag.match(line.rstrip())
        if nobag_match is not None:
            continue

        outer_bag = outer_bag_exp.match(line.rstrip()).groups()[0]
        bags_with_counts[outer_bag] = list()
        for inner_bag_info in inner_bags_exp.findall(line.rstrip()):
            inner_bag = inner_bag_info[1]
            if inner_bag in bags:
                bags[inner_bag].append(outer_bag)
            else:
                bags[inner_bag] = [outer_bag]
            bags_with_counts[outer_bag].append((inner_bag_info[1], int(inner_bag_info[0])))


def recursive_bag_count(keys, bags, evaluated_bags):
    count = 0
    for key in keys:
        if key in evaluated_bags:
            continue
        count += 1
        if key in bags:
            c, evaluated_bags = recursive_bag_count(bags[key], bags, evaluated_bags)
            count += c
        evaluated_bags.add(key)
    return count, evaluated_bags


n_bags, _ = recursive_bag_count(('shiny gold',), bags, evaluated_bags=set())
print(f'a) {n_bags-1}')


def recursive_inner_bag_count(key, bags_count):
    count = 1
    if key in bags_count:
        for bags in bags_count[key]:
            count += bags[1] * recursive_inner_bag_count(bags[0], bags_count)
    return count


print(f"b) {recursive_inner_bag_count('shiny gold', bags_with_counts) - 1}")
