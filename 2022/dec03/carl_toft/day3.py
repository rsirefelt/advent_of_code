def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def findCommonItem(contents):
    size = len(contents)
    assert size % 2 == 0, "Not even size!"
    compartment1 = contents[:int(size / 2)]
    compartment2 = contents[int(size / 2):]
    common_items = list(set(compartment1).intersection(set(compartment2)))
    assert len(common_items) == 1, "More than one common item!"
    return common_items[0]

def computeItemPriority(item):
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 64 + 26
    else:
        assert False, "Should either be lower or upper case!"

def findSharedItemBetweenElfs(rucksacks):
    shared_items = list(set(rucksacks[0]).intersection(rucksacks[1]).intersection(rucksacks[2]))
    assert len(shared_items) == 1, "Only one item should be shared"
    return shared_items[0]

data = parseInput("input.txt")

# Part 1
total_priority_1 = 0
for rucksack in data:
    common_item = findCommonItem(rucksack)
    priority = computeItemPriority(common_item)
    total_priority_1 = total_priority_1 + priority

# Part 2
idx = 0
total_priority_2 = 0
while idx < len(data):
    shared_item = findSharedItemBetweenElfs(data[idx:idx+3])
    priority = computeItemPriority(shared_item)
    total_priority_2 = total_priority_2 + priority
    idx = idx + 3

print("Part 1: " + str(total_priority_1))
print("Part 2: " + str(total_priority_2))
