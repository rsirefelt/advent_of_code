import numpy as np

with open("input.txt", "r") as f:
    rules = (
        f.read().replace(" bags", "").replace(" bag", "").replace(".", "").split("\n")
    )

bag_adj_mat = np.zeros((len(rules), len(rules)), np.int32)
bag_adj_dict = dict()

# Construct adjacency list
for rule in rules:
    bags = rule.split(" contain ")
    bag_adj_dict[bags[0]] = list()
    for b in bags[1].split(", "):
        if b != "no other":
            bag_adj_dict[bags[0]].append([int(b[:2]), b[2:].strip()])

# Construct adjacency matrix
key_list = list(bag_adj_dict)
for i, bag in enumerate(bag_adj_dict.items()):
    for cont_bag in bag[1]:
        bag_adj_mat[i][key_list.index(cont_bag[1])] = 1

# Part 1:
# Using the multiplication trick of adjacency matrices
# Seems both slow an cumbersome to implement
shiny_gold_idx = key_list.index("shiny gold")
adj_map_pow = bag_adj_mat
valid_idx = set(x for x in range(len(rules)))
curr_idx = set(np.where(adj_map_pow[:, shiny_gold_idx] > 0)[0])
curr_valid_idx = curr_idx & valid_idx
bag_color_count = len(curr_valid_idx)
valid_idx -= curr_valid_idx
while len(curr_valid_idx) > 0:
    adj_map_pow = np.matmul(adj_map_pow, bag_adj_mat)
    curr_idx = set(np.where(adj_map_pow[:, shiny_gold_idx] > 0)[0])
    curr_valid_idx = curr_idx & valid_idx
    bag_color_count += len(curr_valid_idx)
    valid_idx -= curr_valid_idx


# Part 2:
def calculate_bag_count(bag_name):
    bag_sum = 0
    for cont_bag in bag_adj_dict[bag_name]:
        bag_sum += cont_bag[0] + cont_bag[0] * calculate_bag_count(cont_bag[1])
    return bag_sum


bag_count = calculate_bag_count("shiny gold")

print(f"1) Number of bag colors: {bag_color_count}")
print(f"2) Number of bags inside: {bag_count}")
