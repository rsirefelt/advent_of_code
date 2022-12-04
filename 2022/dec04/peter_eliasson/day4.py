import unittest

from pathlib import Path


def parse_range(s: str) -> set[int]:
    begin, end = s.split("-")
    begin = int(begin)
    end = int(end)
    return set(range(begin, end + 1))


def part1(input: str) -> int:
    num_subsets = 0
    for line in input.splitlines():
        range1, range2 = line.split(",")
        range1, range2 = parse_range(range1), parse_range(range2)
        if range1.issubset(range2) or range2.issubset(range1):
            num_subsets += 1
    return num_subsets



def part2(input: str) -> int:
    num_overlap = 0
    for line in input.splitlines():
        range1, range2 = line.split(",")
        range1, range2 = parse_range(range1), parse_range(range2)
        if range1.intersection(range2):
            num_overlap += 1
    return num_overlap


class TestDay4(unittest.TestCase):

    EXAMPLE_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".lstrip()

    def test_example_part1(self):
        actual = part1(self.EXAMPLE_INPUT)
        self.assertEqual(actual, 2)

    def test_example_part2(self):
        actual = part2(self.EXAMPLE_INPUT)
        self.assertEqual(actual, 4)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=0)
    input = Path("input").read_text()
    print("part1=", part1(input))
    print("part2=", part2(input))
