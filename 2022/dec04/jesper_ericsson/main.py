import os
import re

regex_lines = re.compile(r"([0-9]*)-([0-9]*),([0-9]*)-([0-9]*)")


def read_data(filename):
    elf_pairs = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_values = regex_lines.findall(line)
            elf_pairs.append([int(i) for i in line_values[0]])

    return elf_pairs


def prob1(elf_pairs):
    num_full_overlap = 0
    for elf_pair in elf_pairs:

        if (elf_pair[0] >= elf_pair[2] and elf_pair[1] <= elf_pair[3]) or (
            elf_pair[2] >= elf_pair[0] and elf_pair[3] <= elf_pair[1]
        ):
            num_full_overlap += 1

    print(f"Number total overlap: {num_full_overlap}")


def prob2(elf_pairs):
    num_overlap = 0
    for elf_pair in elf_pairs:

        if (
            (elf_pair[0] >= elf_pair[2] and elf_pair[0] <= elf_pair[3])
            or (elf_pair[1] >= elf_pair[2] and elf_pair[1] <= elf_pair[3])
            or (elf_pair[2] >= elf_pair[0] and elf_pair[2] <= elf_pair[1])
            or (elf_pair[3] >= elf_pair[0] and elf_pair[3] <= elf_pair[1])
        ):
            num_overlap += 1

    print(f"Number any overlap: {num_overlap}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"
    elf_pairs = read_data(filename)

    prob1(elf_pairs)
    prob2(elf_pairs)


if __name__ == "__main__":
    main()
