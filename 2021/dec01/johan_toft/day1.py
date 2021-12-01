from aoc_helper import download_advent_of_code_input


def main():
    download_advent_of_code_input(2021, 1)

    # Part 1
    # Read the input into a list
    with open("input.txt") as f:
        input_list = [int(x) for x in f.read().splitlines()]

    # Find all increasing numbers
    increasing_numbers = []
    for x, xp1 in zip(input_list, input_list[1:]):
        if x < xp1:
            increasing_numbers.append(x)

    print(f"Part 1: {len(increasing_numbers)}")

    # Part 2
    # Slide over the input with 2 windows with a window size of 3
    # If the sum of the second window is larger than the sum of the previous window,
    # count it.
    increasing_sums = 0
    print(len(input_list))
    for i in range(len(input_list) - 3):
        window1 = input_list[i:i + 3]
        window2 = input_list[i + 1:i + 4]
        assert len(window1) == 3
        assert len(window2) == 3
        if sum(window2) > sum(window1):
            increasing_sums += 1

    print(f"Part 2: {increasing_sums}")


if __name__ == '__main__':
    main()
