""" Advent of Code Day[9] """

import numpy as np


def find_pair_sum(arr, target):
    memberships = {num: True for num in arr}
    for num1 in arr:
        num2 = target - num1
        is_member = memberships.get(num2, False)
        if num2 != num1 and is_member:
            return True
    return False


if __name__ == "__main__":
    arr = np.loadtxt('./input_day9.txt', dtype=np.int64)

    # Part I
    npre = 25
    for i in range(npre, len(arr)):
        if not find_pair_sum(arr[i - npre : i], arr[i]):
            i_inv = i
            inv = arr[i]
            break

    # Part II
    ncont = 2
    while True:
        for ioff in range(ncont):
            istart = np.arange(ioff, len(arr) + 1, ncont)
            sums = np.array(
                [np.sum(arr[i : i + ncont]) for i in istart]
            )
            isum = np.where(sums == inv)[0]
            if len(isum) > 0:
                ihit = istart[isum[0]]
                seq = arr[ihit:ihit+ncont]
                print(np.min(seq) + np.max(seq))
                break
        else:
            ncont += 1
            continue
        break
