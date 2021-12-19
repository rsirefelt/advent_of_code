import numpy as np
from utils import read_lines

class SnailfishNumber():
    def __init__(self):
        self.first = None
        self.second = None
        self.parent = None
        self.value = None

    @classmethod
    def construct_number(cls, number):
        if type(number) == str:
            number = eval(number)

        snailfish_num = SnailfishNumber()
        if type(number) != list:
            snailfish_num.value = number
            return snailfish_num

        snailfish_num.first = cls.construct_number(number[0])
        snailfish_num.second = cls.construct_number(number[1])
        snailfish_num.first.parent = snailfish_num
        snailfish_num.second.parent = snailfish_num

        return snailfish_num

    def send_left(self, value):
        current = self
        while current.parent is not None and current.parent.first == current:
            current = current.parent
            child = current.first

        if current.parent is None and current.first == child:
            return None

        # Traverse down to the right
        current = current.parent.first
        while current.second is not None:
            current = current.second

        # We have found the rightmost node!
        current.value = value + current.value

        return None

    def send_right(self, value):
        current = self
        while current.parent is not None and current.parent.second == current:
            current = current.parent
            child = current.second

        if current.parent is None and current.second == child:
            return None

        # Traverse down to the left
        current = current.parent.second
        while current.first is not None:
            current = current.first

        # We have found the rightmost node!
        current.value = value + current.value

        return None

    def explode(self):
        self.send_left(self.first.value)
        self.send_right(self.second.value)

        self.first = None
        self.second = None
        self.value = 0
        return None

    def reduce(self, explode_or_split, depth=1):
        """Traverse the tree and reduce the number accordingly."""
        # Check for exploding number
        if explode_or_split == "explode":
            if depth >= 5:
                if self.value is None: # only pairs will explode
                    if self.first.value is not None and self.second.value is not None:
                        self.explode()
                        return True

        # Check for splitting number
        if explode_or_split == "split":
            if self.value is not None:
                if self.value >= 10:
                    self.first = SnailfishNumber()
                    self.first.value = int(self.value / 2)
                    self.first.parent = self
                    self.second = SnailfishNumber()
                    self.second.value = int(self.value / 2 + 0.5)
                    self.second.parent = self
                    self.value = None
                    return True

        # Continue search down the tree, considering the left branch first
        reduced = False
        if self.first is not None:
            reduced = self.first.reduce(explode_or_split, depth+1)
        if not reduced and self.second is not None:
            reduced = self.second.reduce(explode_or_split, depth+1)

        return reduced

    def full_reduce(self):
        reduced = True
        while reduced:
            #print(self.asString())
            reduced_explode = True
            while reduced_explode:
                reduced_explode = self.reduce("explode")
            reduced = self.reduce("split")

    def asString(self):
        if self.value is not None:
            return str(self.value)

        representation = "[" + self.first.asString() + ", " + self.second.asString() + "]"
        return representation

    @classmethod
    def add(cls, number1, number2):
        sum = SnailfishNumber()

        sum.first = number1
        sum.second = number2
        sum.first.parent = sum
        sum.second.parent = sum

        sum.full_reduce()

        return sum

    def computeSum(self):
        if self.value is not None:
            return self.value
        else:
            return 3*self.first.computeSum() + 2*self.second.computeSum()


numbers = read_lines("/home/carl/Code/AdventOfCode/Day18/input.txt")

sum = SnailfishNumber.construct_number(numbers[0])
for k in range(1, len(numbers)):
    sum = SnailfishNumber.add(sum, SnailfishNumber.construct_number(numbers[k]))
print("Part 1:", sum.computeSum())

sums = []
for k in range(len(numbers)):
    for kk in range(len(numbers)):
        if k != kk:
            sum = SnailfishNumber.add(SnailfishNumber.construct_number(numbers[k]), SnailfishNumber.construct_number(numbers[kk])).computeSum()
            sums.append(sum)
            sum = SnailfishNumber.add(SnailfishNumber.construct_number(numbers[kk]), SnailfishNumber.construct_number(numbers[k])).computeSum()
            sums.append(sum)
print("Part 2:", np.max(np.array(sums)))