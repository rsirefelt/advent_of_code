""" Advent of Code Day 7. """

import numpy as np
import re
import scipy.sparse.csgraph as csgraph


def parse_input(input_file='./input_day7.txt'):
    regex_bag = r'(.+)\sbags\scontain'
    regex_rule = r'\s([0-9])\s([a-z]+\s[a-z]+)'
    bag_rules = {}
    with open(input_file, 'r') as fp:
        for line in fp:
            bag = re.match(regex_bag, line).group(1)
            rules = re.findall(regex_rule, line)
            bag_rules[bag] = {bg: int(num) for num, bg in rules} 
            
    return bag_rules


def create_graph(bag_rules):
    num_bags = len(bag_rules)
    bags = list(bag_rules.keys())
    g_dense = np.zeros((num_bags, num_bags), dtype=np.int64)
    for i, rule in enumerate(bag_rules.values()):
        for bg, num in rule.items():
            g_dense[i, bags.index(bg)] = num

    return csgraph.csgraph_from_dense(g_dense).astype(np.int64)


def count_bags(graph, irow):
    row = graph.getrow(irow)
    inds = row.indices 
    data = row.data
    if len(inds) > 0:
        res = np.sum(data)
        for k in range(len(inds)):
            res += data[k]*count_bags(graph, inds[k])
        return res
    else:
        return 0


if __name__ == "__main__":

    bag_rules = parse_input()
    bags = list(bag_rules.keys())

    g = create_graph(bag_rules)

    # Part I
    btree = csgraph.breadth_first_tree(g.T, bags.index('shiny gold'))
    print(btree.nnz)

    # Part II
    print(count_bags(g, bags.index('shiny gold')))
