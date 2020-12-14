import math
import regex as re
import numpy as np


def task1(actions):
    memory = {}
    for mask, mem_actions in actions.items():

        for mem_address, mem_value in mem_actions:
            mem_value = str(np.binary_repr(mem_value, 36))
            sol = ""
            for mem_val, mask_val in zip(mem_value, mask):
                sol += mem_val if mask_val == "X" else mask_val

            memory[mem_address] = int(sol, 2)

    sum_ = 0
    for val in memory.values():
        sum_ += val

    return sum_


def adder(list_, val):
    return [item + val for item in list_]


def task2(actions):
    memory = {}
    for mask, mem_actions in actions.items():

        for mem_address, mem_value in mem_actions:
            mem_address = str(np.binary_repr(mem_address, 36))
            sols = [""]
            for mem_adr_val, mask_val in zip(mem_address, mask):
                if mask_val == "X":
                    sols = [*adder(sols, "1"), *adder(sols, "0")]

                elif mask_val == "1":
                    sols = adder(sols, "1")
                elif mask_val == "0":
                    sols = adder(sols, mem_adr_val)

            for sol in sols:
                memory[int(sol, 2)] = mem_value

    sum_ = 0
    for val in memory.values():
        sum_ += val

    return sum_


if __name__ == "__main__":
    actions = {}
    current_actions = []
    current_mask = None

    with open("input") as f:
        lines = list(f.readlines())
        for line in lines:
            line = line.rsplit()

            if line[0] == "mask":
                if current_mask:
                    actions[current_mask] = current_actions
                current_mask = line[2]
                current_actions = []
            else:
                mem_location = re.findall("mem\[([0-9]*)\]", line[0])
                mem_location = int(mem_location[0])
                mem_value = int(line[2])
                current_actions.append((mem_location, mem_value))

    actions[current_mask] = current_actions

    res1 = task1(actions)
    print(res1)
    res2 = task2(actions)
    print(res2)
