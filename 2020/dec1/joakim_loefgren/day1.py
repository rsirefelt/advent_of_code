from itertools import product


def find_pair_sum(arr, target):
    """Finds two numbers in a unique integer array that add up to a target sum.

    Complexity O(n)
    """
    memberships = {num: True for num in arr}
    for num1 in arr:
        num2 = target - num1
        is_member = memberships.get(num2, False)
        if num2 != num1 and is_member:
            return num1, num2
    return None


def find_triplet_sum(arr, target):
    """Finds three numbers in a unique integer array that add up to a target sum.

    Complexity O(n^2)
    """
    memberships = {num: True for num in arr}
    for num1, num2 in product(arr, arr):
        num3 = target - num1 - num2
        is_member = memberships.get(num3, False)
        if num3 != num1 and num3 != num2 and is_member:
            return num1, num2, num3
    return None


if __name__ == "__main__":
    import numpy as np

    # Day 1 Advent of code 2020
    arr = np.loadtxt("input.txt", dtype=np.int64)
    assert len(arr) == len(set(arr))  # A unique arr lets us use some shortcuts.

    # Part I
    num1, num2 = find_pair_sum(arr, 2020)
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} * {num2} = {num1*num2}")

    # Part II
    num1, num2, num3 = find_triplet_sum(arr, 2020)
    print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
    print(f"{num1} * {num2} * {num3} = {num1*num2*num3}")
