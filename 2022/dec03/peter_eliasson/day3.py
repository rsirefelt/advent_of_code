import unittest

from pathlib import Path


def find_common(l1: str, l2 :str, l3 : str = "" ) -> set:
    s = set(l1).intersection(l2)
    if l3:
        s = s.intersection(l3)
    return s


def priority(item: str) -> int:
    if item >= "a":
        return ord(item) - ord('a') + 1
    else:
        return (ord(item) - ord('A')) + 27


def part1(input: str) -> int:
    prio_sum = 0
    rucksacks = input.splitlines()
    for r in rucksacks:
        mid_idx = len(r)//2
        [c1, c2] = [r[:mid_idx], r[mid_idx:]]
        in_common = find_common(c1, c2)
        for item in in_common:
            prio_sum += priority(item)
    return prio_sum


def part2(input: str) -> int:
    prio_sum = 0
    rucksacks = iter(input.splitlines())
    while True:
        try:
            elf1, elf2, elf3 = next(rucksacks), next(rucksacks), next(rucksacks)
        except StopIteration:
            break
        in_common = find_common(elf1, elf2, elf3).pop()
        prio_sum += priority(in_common)
    return prio_sum


class TestDay3(unittest.TestCase):

    EXAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".lstrip()

    def test_example_part1(self):
        actual = part1(self.EXAMPLE_INPUT)
        self.assertEqual(actual, 157)

    def test_example_part2(self):
        actual = part2(self.EXAMPLE_INPUT)
        self.assertEqual(actual, 70)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=0)
    input = Path("input").read_text()
    print("part1=", part1(input))
    print("part2=", part2(input))
