
from math import floor

import numpy as np


class Monkey:
    def __init__(self, lines, do_divide) -> None:
        self.item_list = [int(it) for it in lines[1].replace(',', '').split()[2:]]
        self.operation = lines[2][19:]
        self.test_div = int(lines[3].split()[-1])
        self.true_monkey = int(lines[4].split()[-1])
        self.false_monkey = int(lines[5].split()[-1])
        self.do_divide = do_divide
        self.num_inspects = 0

    def inspect_and_throw(self, total_denominator):
        thrown_items = []
        for old in self.item_list:
            new = eval(self.operation)
            if self.do_divide:
                new = floor(new/3)
            if total_denominator is not None:
                new = new % total_denominator  # worry management
            if new % self.test_div == 0:
                thrown_items.append((new, self.true_monkey))
            else:
                thrown_items.append((new, self.false_monkey))
            self.num_inspects += 1
        self.item_list = []
        return thrown_items

    def __repr__(self):
        return f'{self.num_inspects} -- {str(self.item_list)}'


with open('inputs/day11') as f:
    monkey_data = f.read().splitlines()


for do_divide, rounds in zip((True, False), (20, 10000)):
    monkeys = [Monkey(monkey_data[i:i+7], do_divide) for i in range(0, len(monkey_data), 7)]
    total_denominator = np.prod([m.test_div for m in monkeys]) if not do_divide else None

    for i in range(rounds):
        for monkey in monkeys:
            thrown_items = monkey.inspect_and_throw(total_denominator)
            for (worry_level, receive_monkey) in thrown_items:
                monkeys[receive_monkey].item_list.append(worry_level)

    monkeys.sort(key=lambda monkey: monkey.num_inspects)
    print(monkeys[-1].num_inspects*monkeys[-2].num_inspects)
