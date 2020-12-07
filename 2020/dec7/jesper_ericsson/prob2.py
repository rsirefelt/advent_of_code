import re

regex_top = re.compile(r'([a-z ]*) bags? contain')
regex_contain = re.compile(r'([0-9]) ([a-z]* [a-z]*) bags?')

def read_rules(filename):
    rules = {}

    with open(filename, 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            top_bag = regex_top.findall(string)[0]
            contained_bags = regex_contain.findall(string)

            rules[top_bag] = contained_bags

    return rules

def count_contained_bags(rules, bags):
    number_of_bags = 0
    for count,bag in bags:
        number_of_bags += int(count)
        number_of_bags += int(count) * count_contained_bags(rules, rules[bag])
    return number_of_bags


def main():
    # rules = read_rules('testdata.csv')
    rules = read_rules('data.csv')
    # print(rules)
    total_number_of_bags = count_contained_bags(rules, rules['shiny gold'])
    print('Part2, Total number of contained bags: %i' %total_number_of_bags)


if __name__ == "__main__": main()