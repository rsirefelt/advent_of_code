import os
import numpy as np

def check_and_add(x, cycle):
    if (cycle - 20) % 40 == 0:
        print(f"x2: {x}, cycle: {cycle}, signal: {x * cycle}")
        return x *cycle
    
    return 0

def prob1(instructions):
    cycle = 0
    x = 1
    sum_signals = 0
    for instruction in instructions:
        # print(instruction.rstrip())
        if instruction.rstrip() == "noop":
            cycle += 1
            sum_signals += check_and_add(x, cycle)

        else:
            cycle += 1
            sum_signals += check_and_add(x, cycle)
            cycle += 1
            sum_signals += check_and_add(x, cycle)

            x += int(instruction.rstrip()[5:])
    print(f"Signal sum: {sum_signals}")



def prob2(instructions):
    position = 0
    x = 1
    sum_signals = 0
    for instruction in instructions:

        if instruction.rstrip() == "noop":
            cycle += 1
            sum_signals += check_and_add(x, cycle)

        else:
            cycle += 1
            sum_signals += check_and_add(x, cycle)
            cycle += 1
            sum_signals += check_and_add(x, cycle)

            x += int(instruction.rstrip()[5:])
    print(f"Signal sum: {sum_signals}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    # filename = dir + "/data.csv"
    with open(filename, "r") as f:
        instructions = f.readlines()

    prob1(instructions)
    # prob2(map)


if __name__ == "__main__":
    main()
