""" Advent of Code Day 14 """
import re
from itertools import product

import numpy as np


def parse_input(input_file):
    with open(input_file, "r") as fp:
        regex_mask = r"mask\s=\s((X|1|0)+)"
        regex_mem = r"mem\[(\d+)\]\s=\s(\d+)"
        instructions = []
        for line in fp:
            if match := re.search(regex_mem, line):
                instructions.append((int(match.group(1)), int(match.group(2))))
            elif match := re.search(regex_mask, line):
                instructions.append(match.group(1))
    return instructions


if __name__ == "__main__":
    instructions = parse_input("./input_day14.txt")

    # Part I
    # The operation of the bitmask number a is equivalent to
    # to a bitwise AND that zeros the target bits, followed by a
    # bitwise OR that sets those bits to their new values.
    mem = {}
    for inst in instructions:
        if isinstance(inst, str):
            mask_and = int(
                inst.translate(str.maketrans({"X": "1", "1": "0", "0": "0"})), 2
            )
            mask_or = int(inst.replace("X", "0"), 2)
        else:
            addr, val = inst
            val &= mask_and
            val |= mask_or
            mem[addr] = val

    print(sum(mem.values()))

    # Part II
    # The operation of the bitmask number a is equivalent to
    # to a bitwise OR with X's replaced by 0's, followed by
    # copying over all X's from the original mask.
    mem = {}
    nmask = 36
    for inst in instructions:
        if isinstance(inst, str):
            mask = inst
            mask_or = int(mask.replace("X", "0"), 2)
        else:
            addr, val = inst
            addr |= mask_or
            addr_pad = format(addr, "036b")
            addr_float = np.array(
                ["X" if mask[i] == "X" else addr_pad[i] for i in range(nmask)]
            )
            i_X = [i for i in range(nmask) if addr_float[i] == "X"]
            num_X = len(i_X)
            for bits in product(*[[0, 1]] * num_X):
                addr_float[i_X] = bits
                new_addr = int("".join(addr_float), 2)
                mem[new_addr] = val

    print(sum(mem.values()))
