import math
import functools
import operator
import itertools


def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


class SnailNumber:
    """Represent a snail number by the regular numbers and their nesting level."""
    def __init__(self, expression):
        numbers = []
        levels = []
        level = 0
        for c in expression:
            if c == "[":
                level += 1
            elif c.isnumeric():
                numbers.append(int(c))
                levels.append(level)
            elif c == "]":
                level -= 1
            else:
                continue
        self.numbers = numbers
        self.levels = levels

    @classmethod
    def from_data(cls, numbers, levels):
        self = cls.__new__(cls)
        self.numbers = numbers
        self.levels = levels
        return self

    def __eq__(self, other):
        return self.numbers == other.numbers and self.levels == other.levels

    def __add__(self, other):
        numbers = self.numbers + other.numbers
        levels = [l + 1 for l in self.levels + other.levels]
        snail_number = SnailNumber.from_data(numbers, levels)
        snail_number.reduce()
        return snail_number

    def __str__(self):
        return f'Numbers: {self.numbers}\nLevels: {self.levels}'

    def explode(self, i):
        numbers = self.numbers
        levels = self.levels
        if i > 0:
            numbers[i - 1] += numbers[i]
        if i < len(numbers) - 2:
            numbers[i + 2] += numbers[i + 1]
        numbers[i] = 0
        levels[i] -= 1
        numbers.pop(i + 1)
        levels.pop(i + 1)

    def split(self, i):
        numbers = self.numbers
        levels = self.levels
        num, level = numbers[i], levels[i]
        self.numbers = (
            numbers[:i]
            + [math.floor(0.5*num), math.ceil(0.5*num)]
            + numbers[i + 1:]
        )
        self.levels = (
            levels[:i]
            + [level + 1]*2
            + levels[i + 1:]
        )

    def reduce(self):
        """Assume that at nesting level 5 there are only ever regular pairs. """
        while True:
            for i in range(len(self.levels)):
                if self.levels[i] == 5 == self.levels[i + 1]:
                    self.explode(i)
                    break
            else:
                for i in range(len(self.levels)):
                    if self.numbers[i] >= 10:
                        self.split(i)
                        break
                else:
                    return

    def magnitude(self):
        levels = self.levels
        numbers = self.numbers
        for level_curr in range(max(levels), 0, -1):
            numbers_new = []
            levels_new = []
            paired = False
            for inds in itertools.pairwise(range(len(numbers))):
                i, j = inds
                if levels[i] == levels[j] == level_curr:
                    if paired:
                        paired = False
                    else:
                        res = 3*numbers[i] + 2*numbers[j]
                        numbers_new.append(res)
                        levels_new.append(levels[i] - 1)
                        paired = True
                else:
                    if not paired:
                        numbers_new.append(numbers[i])
                        levels_new.append(levels[i])
                    else:
                        paired = False
                    if j == len(numbers) - 1:
                        numbers_new.append(numbers[j])
                        levels_new.append(levels[j])

            numbers = numbers_new
            levels = levels_new
        return numbers[0]


if __name__ == "__main__":
    lines = parse_input('./input_day18.txt')
    snail_numbers = [SnailNumber(expr) for expr in lines]

    # Part I
    res = functools.reduce(operator.add, snail_numbers)
    print(res.magnitude())

    # Part II
    mag_max = 0
    for a, b in itertools.permutations(snail_numbers, 2):
        mag = (a + b).magnitude()
        if mag > mag_max:
            mag_max = mag
    print(mag_max)
