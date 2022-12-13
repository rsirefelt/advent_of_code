from typing import List
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for i in range(max(len(left), len(right))):
        if i >= len(left):
            return False, True
        if i >= len(right):
            return False, False
        if isinstance(left[i], List) or isinstance(right[i], List):
            is_same, return_val = compare(left[i], right[i])
            if not is_same:
                return False, return_val
        elif left[i] < right[i]:
            return False, True
        elif right[i] < left[i]:
            return False, False
    return True, None


with open('inputs/day13') as f:
    data = f.read().splitlines()

pair_sum = 0
for pair_i, i in enumerate(range(0, len(data), 3), 1):
    left = eval(data[i])
    right = eval(data[i+1])
    _, rightorder = compare(left, right)
    if rightorder:
        pair_sum += pair_i

print(pair_sum)

all_lines_to_sort = [[[2]], [[6]]]
for line in data:
    if line != '':
        all_lines_to_sort.append(eval(line))


def cmp(left, right):
    _, rightorder = compare(left, right)
    return -1 if rightorder else 1


all_lines_to_sort.sort(key=cmp_to_key(cmp))
print((all_lines_to_sort.index([[2]]) + 1) * (all_lines_to_sort.index([[6]]) + 1))
