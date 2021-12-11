import numpy as np
from utils import read_lines

# Some global variables
opening_to_closing_mapping = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
opening_brackets = {'(','[','{', '<'}
closing_brackets = {')',']','}','>'}
bracket_to_score_part_1 = {')' : 3,']' : 57,'}' : 1197 ,'>' : 25137}
bracket_to_score_part_2 = {')' : 1, ']' : 2, '}' : 3 ,'>' : 4}


def getIndexOfFirstErrorOrCompletionString(line):
    started_brackets = []
    for idx, char in enumerate(line):
        if char in opening_brackets:
            started_brackets.append(char)
        if char in closing_brackets:
            if opening_to_closing_mapping[started_brackets[-1]] == char:
                started_brackets.pop()
            else:
                return 'incorrect', idx

    completion_string = ''.join([opening_to_closing_mapping[char] for char in started_brackets])[::-1]
    return 'incomplete', completion_string # no errors encountered


lines = read_lines("/home/carl/Code/AdventOfCode/Day10/input.txt")

# Compute score for all incorrect lines
total_score = 0
for line in lines:
    status, idx = getIndexOfFirstErrorOrCompletionString(line)
    if status == "incorrect":
        total_score = total_score + bracket_to_score_part_1[line[idx]]

print("Part 1:", total_score)

# Compute score for all incomplete lines
scores = []
for line in lines:
    status, completion_string = getIndexOfFirstErrorOrCompletionString(line)
    if status == "incomplete":
        total_score = 0
        for char in completion_string:
            total_score = 5*total_score + bracket_to_score_part_2[char]
        scores.append(total_score)

final_score = int(np.median(np.array(scores)))

print("Part 2:", final_score)
