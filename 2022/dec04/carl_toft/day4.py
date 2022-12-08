def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    lines = lines[:-1]
    ranges = [line.split(',') for line in lines]
    elf1_range = [item[0].split('-') for item in ranges]
    elf1_range = [(int(item[0]), int(item[1])) for item in elf1_range]

    elf2_range = [item[1].split('-') for item in ranges]
    elf2_range = [(int(item[0]), int(item[1])) for item in elf2_range]

    return elf1_range, elf2_range

def isOneRangeInTheOther(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

def doRangesOverlap(range1, range2):
    if range1[0] < range2[0] and range1[1] < range2[0]:
        return False
    if range2[0] < range1[0] and range2[1] < range1[0]:
        return False
    return True


elf1_range, elf2_range = parseInput("input.txt")

assert len(elf1_range) == len(elf2_range), "Not the same length!"

num_bad_ranges = 0
num_overlapping_ranges = 0
for k in range(len(elf1_range)):
    if isOneRangeInTheOther(elf1_range[k], elf2_range[k]):
        num_bad_ranges = num_bad_ranges + 1
    if doRangesOverlap(elf1_range[k], elf2_range[k]):
        num_overlapping_ranges = num_overlapping_ranges + 1
        #print("Hello")
        #print(elf1_range[k])
        #print(elf2_range[k])

print("Part 1: " + str(num_bad_ranges))
print("Part 2: " + str(num_overlapping_ranges))

xxx = 3
