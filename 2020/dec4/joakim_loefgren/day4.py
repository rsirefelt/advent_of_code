"""Advent of Code Day 4 2020 """
import re


def validate_basic(input_file='input_day4.txt'):
    with open(input_file, 'r') as fp:
        input_text = fp.read()

    input_split = input_text.split('\n\n')
    regex = r"([a-z]{3}):(#?\w+)"
    num_valid = 0

    for pp_text in input_split:
        matches = re.findall(regex, pp_text)
        keys = {groups[0] for groups in matches}
        if len(keys - {'cid'}) == 7:
            num_valid += 1

    return num_valid


def validate_advanced(input_file='input_day4.txt'):

    with open(input_file, 'r') as fp:
        input_text = fp.read()

    input_split = input_text.split('\n\n')

    regexes = [
        r"(byr):(19[2-8][0-9]|199[0-9]|200[0-2])(\s|\n|$)",
        r"(iyr):(201[0-9]|2020)(\s|\n|$)",
        r"(eyr):(202[0-9]|2030)(\s|\n|$)",
        r"(hgt):((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)(\s|\n|$)",
        r"(hcl):#[0-9a-f]{6}(\s|\n|$)",
        r"(ecl):(amb|blu|brn|gry|grn|hzl|oth)(\s|\n|$)",
        r"(pid):\d{9}(\s|\n|$)",
    ]

    num_valid = 0
    for pp_text in input_split:
        if all([re.search(regex, pp_text) for regex in regexes]):
            num_valid += 1
    
    return num_valid


if __name__ == "__main__":

    print('Part I')
    print(validate_basic())

    print('Part II')
    print(validate_advanced())
