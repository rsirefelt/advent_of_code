import numpy as np
import time


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        wires = []
        segments = []
        for line in input_lines:
            line_wires, line_segments = line.rstrip().split(" | ")
            wires.append(line_wires.split())
            segments.append(line_segments.split())

    return wires, segments


def prob1(segments):
    segment_counter = 0
    for line_segments in segments:
        for segment in line_segments:

            if len(segment) == 2:
                # 1
                segment_counter += 1
            elif len(segment) == 4:
                # 4
                segment_counter += 1
            elif len(segment) == 3:
                # 7
                segment_counter += 1
            elif len(segment) == 7:
                # 8
                segment_counter += 1
    print("Problem 1, number of 1,4,7,8:", segment_counter)


def find_1478(pattern_list):
    decoded_patterns = {}
    pattern_to_remove = []
    for pattern in pattern_list:
        if len(pattern) == 2:
            decoded_patterns["".join(sorted(pattern))] = 1
            pattern_to_remove.append(pattern)
            one_pattern = set(pattern)
        elif len(pattern) == 4:
            decoded_patterns["".join(sorted(pattern))] = 4
            pattern_to_remove.append(pattern)
            four_pattern = set(pattern)
        elif len(pattern) == 3:
            decoded_patterns["".join(sorted(pattern))] = 7
            pattern_to_remove.append(pattern)
        elif len(pattern) == 7:
            decoded_patterns["".join(sorted(pattern))] = 8
            pattern_to_remove.append(pattern)

    for pattern in pattern_to_remove:
        pattern_list.remove(pattern)
    return decoded_patterns, one_pattern, four_pattern


def find_690(pattern_list, decoded_patterns, one_pattern, four_pattern):

    for pattern in pattern_list:

        if len(pattern) == 6:  # 069
            if len(set(pattern) - four_pattern) == 2:
                decoded_patterns["".join(sorted(pattern))] = 9
            elif len(one_pattern - set(pattern)) == 0:
                decoded_patterns["".join(sorted(pattern))] = 0
            else:
                decoded_patterns["".join(sorted(pattern))] = 6
                six_pattern = set(pattern)
    return six_pattern


def find_235(pattern_list, decoded_patterns, one_pattern, six_pattern):
    for pattern in pattern_list:
        if len(pattern) == 5:
            if len(one_pattern - set(pattern)) == 0:
                decoded_patterns["".join(sorted(pattern))] = 3
            elif len(set(pattern) - six_pattern) == 0:
                decoded_patterns["".join(sorted(pattern))] = 5
            else:
                decoded_patterns["".join(sorted(pattern))] = 2


def prob2(wires, segments):
    sum_values = 0
    for (line_wires, line_segments) in zip(wires, segments):

        decoded_patterns, one_pattern, four_pattern = find_1478(line_wires)
        six_pattern = find_690(line_wires, decoded_patterns, one_pattern, four_pattern)
        find_235(line_wires, decoded_patterns, one_pattern, six_pattern)

        value = 0
        for ind, segment in enumerate(line_segments):
            sort_digit_pattern = "".join(sorted(segment))
            value += decoded_patterns[sort_digit_pattern] * 10 ** (3 - ind)

        sum_values += value
    print("Problem 2 sum of all values:", sum_values)


def main():
    wires, segments = readData()

    prob1(segments)
    prob2(wires, segments)


if __name__ == "__main__":
    main()
