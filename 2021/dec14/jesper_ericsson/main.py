from collections import deque
import re
import time


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        start_polymer = f.readline().rstrip()
        f.readline()
        input_lines = f.readlines()

        replacements = []

        for line in input_lines:
            search, new = line.rstrip().split(" -> ")
            replacements.append((search, new))
        f.close()

    return start_polymer, replacements


def prob1(polymer_str, replacements):

    for step in range(10):
        list_of_replacements = []
        for search, new_char in replacements:
            for match in re.finditer("(?=" + search + ")", polymer_str):
                list_of_replacements.append((match.start() + 1, new_char))

        list_of_replacements.sort()

        polymer_deque = deque(polymer_str)
        old_index = 0
        extra_rotate = list_of_replacements[-1][0] - len(polymer_str)

        for index, new_char in list_of_replacements:
            polymer_deque.rotate(old_index - index)
            polymer_deque.appendleft(new_char)
            polymer_deque.rotate(-1)
            old_index = index

        polymer_deque.rotate(extra_rotate)
        polymer_str = "".join(polymer_deque)

    num_chars = []
    for char in set(polymer_str):
        num_chars.append(polymer_str.count(char))

    print(max(num_chars) - min(num_chars))


def prob2(polymer_str, replacements):
    conversions = {}
    for old_str, new_char in replacements:
        conversions[old_str] = (old_str[0] + new_char, new_char + old_str[1])

    old_polymer_pairs = {}

    for char_ind in range(len(polymer_str) - 1):
        old_polymer_pairs[polymer_str[char_ind : char_ind + 2]] = 1

    for step in range(40):
        new_polymer_pairs = {}

        for pair, count in old_polymer_pairs.items():
            new_pairs = conversions[pair]
            new_polymer_pairs[new_pairs[0]] = (
                new_polymer_pairs.get(new_pairs[0], 0) + count
            )
            new_polymer_pairs[new_pairs[1]] = (
                new_polymer_pairs.get(new_pairs[1], 0) + count
            )

        old_polymer_pairs = new_polymer_pairs

    letter_dict = {polymer_str[0]: 1, polymer_str[-1]: 1}

    for pair, count in old_polymer_pairs.items():
        letter_dict[pair[0]] = letter_dict.get(pair[0], 0) + count
        letter_dict[pair[1]] = letter_dict.get(pair[1], 0) + count

    letter_counts = letter_dict.values()
    print(int((max(letter_counts) - min(letter_counts)) / 2))


def main():
    start_polymer, replacements = readData()

    start = time.time()
    prob1(start_polymer, replacements)
    end = time.time()
    print("Time first part naive: ", end - start)

    start = time.time()
    prob2(start_polymer, replacements)
    end = time.time()
    print("Time second part better: ", end - start)


if __name__ == "__main__":
    main()
