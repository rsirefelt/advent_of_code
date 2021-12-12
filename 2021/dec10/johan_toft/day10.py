
import numpy as np
with open("input.txt") as f:
    data = f.read().splitlines()

# There are three separate types of brackets we need to track.

# [,{, and <
# These are the opening brackets.

# ] and } and >
# These are the closing brackets.

matching_closing = {
    "[": "]",
    "{": "}",
    "<": ">",
    "(": ")"
}

matching_opening = {
    "]": "[",
    "}": "{",
    ">": "<",
    ")": "("
}

violation_vals = {
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137,
}


class Violation():
    def __init__(self, pos, illegal_char):
        self.pos = pos
        self.value = violation_vals[illegal_char]

    def __str__(self):
        return repr(self.value)


sum = 0

syntax_violations = []


def validate_line(line) -> Violation:
    # Stack containing all seen opening brackets.
    stack = []
    for pos, char in enumerate(line):
        if char in "[{<(":
            stack.append(char)
        elif char in "]}>)":
            if stack[-1] == matching_opening[char]:
                stack.pop()
            else:
                print("Expected: " + matching_closing[stack[-1]], "Got: " + char + " at position: " + str(pos))
                return Violation(pos, char)
    return None


def get_parse_stack(line):
    stack = []
    for pos, char in enumerate(line):
        if char in "[{<(":
            stack.append(char)
        elif char in "]}>)":
            stack.pop()
    return stack


for line in data:
    violation = validate_line(line)
    if violation:
        syntax_violations.append(violation)

# Part 1 : Count violations
for violation in syntax_violations:
    sum += violation.value

print(sum)

block_scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

valid_lines = [line for line in data if validate_line(line) is None]


def get_score(line):
    parse_stack = get_parse_stack(line)
    score = 0
    while len(parse_stack) > 0:
        block_opening = parse_stack.pop()
        score *= 5
        score += block_scoring[matching_closing[block_opening]]
    return score


line_scores = [get_score(line) for line in valid_lines]

# Get the middle
line_scores.sort()

median = line_scores[len(line_scores) // 2]
print(median)