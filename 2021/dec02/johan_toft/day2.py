from aoc_helper import download_advent_of_code_input

import re


def main():
    download_advent_of_code_input(2021, 2)

    with open('input.txt', 'r') as f:
        input_data = f.read().splitlines()

    horizontal = 0
    depth = 0

    aim = 0
    """
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
    """

    for line in input_data:
        # Get direction and number of steps
        match = re.match(r'(up|down|forward) (\d+)', line)
        direction = match.group(1)
        steps = int(match.group(2))

        if direction == 'up':
            aim -= steps
        elif direction == 'down':
            aim += steps
        elif direction == 'forward':
            horizontal += steps
            depth += aim * steps

    print(f"Part 1 {aim * horizontal}")
    print(f"Part 2 {horizontal * depth}")


if __name__ == '__main__':
    main()
