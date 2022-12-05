from typing import List


def priority(packing_item: str) -> int:
    ref_char, to_add = ('A', 27) if packing_item.isupper()else ('a', 1)
    return ord(packing_item) - ord(ref_char) + to_add


def priority_for_letter_in_both(packing_list: str) -> int:
    first_half, second_half = packing_list[:len(packing_list) // 2], packing_list[len(packing_list) // 2:]
    for letter in first_half:
        if letter in second_half:
            return priority(letter)
    return -1


def priority_for_badge(group_lists: List[str]) -> int:
    assert len(group_lists) == 3
    letter = set(group_lists[0]).intersection(group_lists[1]).intersection(group_lists[2])
    return priority(list(letter)[0])


packing_lists = []
with open('inputs/day3') as f:
    packing_lists = f.read().splitlines()

print(sum(priority_for_letter_in_both(packing_list) for packing_list in packing_lists))
print(sum(priority_for_badge(packing_lists[i:i+3]) for i in range(0, len(packing_lists), 3)))
