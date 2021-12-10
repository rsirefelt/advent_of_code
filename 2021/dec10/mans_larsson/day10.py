import numpy as np
from collections import deque

code_lines = []
with open('inputs/day10') as f:
    for line in f:
        code_lines.append(line.rstrip())

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']
corresponing_chars = {o:c for o,c in zip(opening_chars, closing_chars)}
char_scores = {'':0, ')': 3, ']': 57, '}': 1197, '>': 25137}
completion_char_scores = {')': 1, ']': 2, '}': 3, '>': 4}

score = 0
completion_scores = []
for code_line in code_lines:
    error_char = ''
    open_chars = deque()
    for char in code_line:
        if char in opening_chars:
            open_chars.append(char)
        if char in closing_chars:
            char_to_close = open_chars.pop()    
            if corresponing_chars[char_to_close] != char:
                error_char = char
                break
    # a
    score += char_scores[error_char]

    # b
    if error_char == '': # no error, only incomplete
        completion_score = 0
        for char in reversed(open_chars):
            completion_score *= 5
            completion_score += completion_char_scores[corresponing_chars[char]]
        completion_scores.append(completion_score)

print(score)
print(int(np.median(completion_scores)))
