import re

regex_top = re.compile(r'([a-z ]*) bags? contain')
regex_contain = re.compile(r'[0-9] ([a-z]* [a-z]*) bags?')

def read_rules(filename):
    rules = {}

    with open(filename, 'r') as f:
        data_lines = f.readlines()

        for string in data_lines:
            top_bag = regex_top.findall(string)[0]
            contained_bags = regex_contain.findall(string)

            rules[top_bag] = contained_bags

    return rules

def contains_bag(rules, bags):
    number_of_bags = 0
    if 'shiny gold' in bags:
        number_of_bags = 1
    else:
        for bag in bags:
            number_of_bags += contains_bag(rules, rules[bag])
    if number_of_bags > 0:
        return 1
    else:
        return 0

def count_top_bags(rules):
    number_of_top_bags = 0
    for bag in rules:
        if bag != 'shiny gold':
            number_of_top_bags += contains_bag(rules, rules[bag])

    return number_of_top_bags

def main():
    rules = read_rules('testdata.csv')
    rules = read_rules('data.csv')
    # print(rules)
    bags_contain_shiny = count_top_bags(rules)
    print('Part1, Total number of bags holding shiny: %i' %bags_contain_shiny)


if __name__ == "__main__": main()