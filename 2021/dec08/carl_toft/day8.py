from utils import read_lines

def getNumber(all_letters, corresponding_numbers, number):
    for idx, letter in enumerate(all_letters):
        if set(number) == set(letter):
            return corresponding_numbers[idx]
    return False

def solveLine(line):
    all_letters = line.split('|')[0].strip().split(' ')
    corresponding_numbers = [-1 for letter in all_letters]
    input_numbers = line.split('|')[1].strip().split(' ')

    # First, identify the letters with a unique number of segments
    mapping = {} # will map numbers to the corresponding strings
    for idx, letter in enumerate(all_letters):
        if len(letter) == 2:
            corresponding_numbers[idx] = 1
            mapping[1] = letter
        elif len(letter) == 3:
            corresponding_numbers[idx] = 7
            mapping[7] = letter
        elif len(letter) == 4:
            corresponding_numbers[idx] = 4
            mapping[4] = letter
        elif len(letter) == 7:
            corresponding_numbers[idx] = 8
            mapping[8] = letter
        #elif len(letter) == 6:
        #    corresponding_numbers[idx] = 6
        #    mapping[6] = letter

    # We can now identify letter 9. It is the only 6 segment letter with 4 as a subset
    for idx, letter in enumerate(all_letters):
        if len(letter) == 6 and set(mapping[4]) < set(letter):
            corresponding_numbers[idx] = 9
            mapping[9] = letter

    # We can now identify letter 3. It is the only 5 segment letter with 1 as a subset
    for idx, letter in enumerate(all_letters):
        if len(letter) == 5 and set(mapping[1]) < set(letter):
            corresponding_numbers[idx] = 3
            mapping[3] = letter

    # Five is the only remaining 5 segment letter which is a subset of 9
    for idx, letter in enumerate(all_letters):
        if len(letter) == 5 and corresponding_numbers[idx] == -1 and set(letter) < set(mapping[9]):
            corresponding_numbers[idx] = 5
            mapping[5] = letter

    # Two is the only remaining 5 segment letter
    for idx, letter in enumerate(all_letters):
        if len(letter) == 5 and corresponding_numbers[idx] == -1:
            corresponding_numbers[idx] = 2
            mapping[2] = letter

    # Zero is the only remaining 6 segment letter with 1 as a subset
    for idx, letter in enumerate(all_letters):
        if len(letter) == 6 and corresponding_numbers[idx] == -1 and set(mapping[1]) < set(letter):
            corresponding_numbers[idx] = 0
            mapping[0] = letter

    # Six is the only remaining 6 segment letter
    for idx, letter in enumerate(all_letters):
        if len(letter) == 6 and corresponding_numbers[idx] == -1:
            corresponding_numbers[idx] = 6
            mapping[6] = letter

    return all_letters, corresponding_numbers, mapping

lines = read_lines("/home/carl/Code/AdventOfCode/Day8/input.txt")
easy_numbers = 0
for line in lines:
    all_letters, corresponding_numbers, _ = solveLine(line)
    input_numbers = line.split('|')[1].strip().split(' ')
    for number in input_numbers:
        val = getNumber(all_letters, corresponding_numbers, number)
        if val == 1 or val == 7 or val == 4 or val == 8:
            easy_numbers = easy_numbers + 1
print('Part 1:', easy_numbers)

sum = 0
for line in lines:
    all_letters, corresponding_numbers, _ = solveLine(line)
    input_numbers = line.split('|')[1].strip().split(' ')
    num = ''
    for number in input_numbers:
        num = num + str(getNumber(all_letters, corresponding_numbers, number))
    num = int(num)
    sum = sum + num
print('Part 2:', sum)