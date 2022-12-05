
from typing import Set, Tuple


def extract_cleaning_assignments(cleaning_assignment: str) -> Tuple[Set[int], Set[int]]:
    cleaner1, cleaner2 = cleaning_assignment.split(',')

    start, stop = cleaner1.split('-')
    cleaner1_assignments = set(range(int(start), int(stop) + 1))
    start, stop = cleaner2.split('-')
    cleaner2_assignment = set(range(int(start), int(stop) + 1))

    return cleaner1_assignments, cleaner2_assignment


with open('inputs/day4') as f:
    cleaning_assignments = f.read().splitlines()

count = 0
countb = 0
for cleaning_assignment in cleaning_assignments:
    ca1, ca2 = extract_cleaning_assignments(cleaning_assignment)
    if ca1.issubset(ca2) or ca2.issubset(ca1):
        count += 1
    if not ca1.isdisjoint(ca2):
        countb += 1
print(count)
print(countb)
