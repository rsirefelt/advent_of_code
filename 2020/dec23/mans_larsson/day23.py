import numpy as np

puzzle_input = '916438275'

cups = list()
for num in puzzle_input:
    cups.append(int(num))
input_cups = cups.copy()
starting_num = int(puzzle_input[0])


def play(current_num, cup_order, n_rounds):
    """cup_order: array where index is cup number - 1 and value is number of next cup"""

    max_val = len(cup_order)
    for i in range(n_rounds):

        # pick three cups
        picked_cups = []
        next_cup = current_num
        for _ in range(3):
            next_cup = cup_order[next_cup - 1]
            picked_cups.append(next_cup)

        # since we removed three cups current num, now points to the one next to the third picked cup
        cup_after_picked_cups = cup_order[next_cup - 1]
        cup_order[current_num - 1] = cup_after_picked_cups

        destination = current_num - 1 if current_num > 1 else max_val
        while destination in picked_cups:
            destination = destination - 1 if destination > 1 else max_val

        # place cups after destination
        prev_cup = cup_order[destination - 1]  # save to add next to third inserted cup
        next_cup = destination
        for i in range(3):
            cup_order[next_cup - 1] = picked_cups[i]
            next_cup = picked_cups[i]
        cup_order[next_cup - 1] = prev_cup

        current_num = cup_order[current_num - 1]

        if i % 100000 == 0:
            print(i)


def get_cup_order(c):
    ord = np.zeros(len(c), dtype=np.int)
    for i in range(len(c) - 1):
        this_cup = c[i]
        next_cup = c[i + 1]
        ord[this_cup - 1] = next_cup
    ord[c[-1] - 1] = c[0]  # first cup is right of last cup
    return ord


cup_order = get_cup_order(cups)

play(starting_num, cup_order, 100)

num = 1
as_string = ''
for _ in range(len(cup_order)-1):
    num = cup_order[num-1]
    as_string += str(num)

print(f'a) {as_string}')

cups = input_cups.copy()
for i in range(len(puzzle_input)+1, 1000000 + 1):
    cups.append(i)

cup_order = get_cup_order(cups)
play(starting_num, cup_order, 10000000)

num = 1
prod = 1
for _ in range(2):
    num = cup_order[num-1]
    prod *= num

print(f'b) {prod}')
