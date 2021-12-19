from utils import read_lines

def parseInput(filename):
    lines = read_lines(filename)
    template = lines[0]
    rules = {}
    for k in range(2, len(lines)):
        source, dest = lines[k].split(' -> ')
        rules[source] = dest
    return template, rules

def growPolymer(template, rules):
    new_polymer = ""
    for k in range(len(template)-1):
        new_polymer = new_polymer + template[k] + rules[template[k:k+2]]
    new_polymer = new_polymer + template[-1]
    return new_polymer

def growPolymerSeveralTimes(template, rules, steps):
    for k in range(steps):
        template = growPolymer(template, rules)
    return template

template, rules = parseInput("/home/carl/Code/AdventOfCode/Day14/input.txt")
# Grow the polymer 10 times
for k in range(10):
    template = growPolymer(template, rules)
    #print(template)

# Find the difference in frequence of the most common and the least common element in the polymer
frequencies = [template.count(element) for element in set(template)]
print("Part 1:", max(frequencies) - min(frequencies))

# Part 2. First, find all elements
template, rules = parseInput("/home/carl/Code/AdventOfCode/Day14/input.txt")

elements = set()
for rule in rules.keys():
    for elem in rule:
        elements.add(elem)

# Initialize lookup table
table = []
for step in range(41):
    table.append({pair : {elem : 0 for elem in elements} for pair in rules.keys()})

# Fill out the first part of the lookup table
for k in range(10):
    for pair in rules.keys():
        polymer = growPolymerSeveralTimes(pair, rules, k)
        table[k][pair] = {elem : polymer.count(elem) for elem in elements}

# Fill out the rest of the table using a recurrence relation
for k in range(10, 41):
    for pair in rules.keys():
        grown_pair = growPolymer(pair, rules)
        first_part = table[k-1][grown_pair[:2]]
        second_part = table[k-1][grown_pair[1:]]
        total_elements = {elem : first_part[elem] + second_part[elem] for elem in elements}
        total_elements[grown_pair[1]] -= 1
        table[k][pair] = total_elements

# Ok! Now find how many elements our initial template becomes
total_num_elements = {elem : 0 for elem in elements}
for k in range(len(template)-1):
    this_pair = table[40][template[k:k+2]]
    for el in this_pair:
        total_num_elements[el] += this_pair[el]
    total_num_elements[template[k+1]] -= 1
total_num_elements[template[-1]] += 1

frequencies = [total_num_elements[el] for el in total_num_elements]
print("Part 2:", max(frequencies) - min(frequencies))