import copy
import operator
import re
from collections import deque

import numpy as np

OP_TABLE = {"*": operator.mul, "+": operator.add}


class Monkey:
    def __init__(self, items, op, arg, div, throw_true, throw_false):
        self.items = deque(items)
        self.op = op
        self.arg = arg
        self.div = div
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.num_inspected = 0

    def operate(self, item):
        self.num_inspected += 1
        if self.arg == "old":
            return self.op(item, item)
        else:
            return self.op(item, int(self.arg))


def play_game(monkeys, num_rounds=1, reduction=None, mod=None):
    for _ in range(num_rounds):
        for monke in monkeys:
            try:
                while True:
                    item = monke.items.popleft()
                    item = monke.operate(item)
                    if reduction:
                        item = item // reduction
                    if mod:
                        item = item % mod
                    if item % monke.div == 0:
                        monkeys[monke.throw_true].items.append(item)
                    else:
                        monkeys[monke.throw_false].items.append(item)
            except IndexError:
                pass


def parse_monkey(text):
    lines = text.splitlines()
    items = re.findall(r"\d+", lines[1])
    items = [int(i) for i in items]
    match = re.search(r"([\*\+])\s((\d+|old))", lines[2])
    op_name, arg = match.group(1), match.group(2)
    op = OP_TABLE[op_name]
    div = int(lines[3].split()[-1])
    throw_true = int(lines[4].split()[-1])
    throw_false = int(lines[5].split()[-1])
    monke = Monkey(items, op, arg, div, throw_true, throw_false)
    return monke


if __name__ == "__main__":
    with open("./input.txt") as f:
        monkey_texts = f.read().split("\n\n")

    monkeys = []
    for text in monkey_texts:
        monkeys.append(parse_monkey(text))

    # part I
    monkeys1 = copy.deepcopy(monkeys)
    play_game(monkeys1, num_rounds=20, reduction=3)
    top_inspections = sorted([m.num_inspected for m in monkeys1], reverse=True)[:2]
    print(top_inspections[0] * top_inspections[1])

    # part II
    monkeys2 = copy.deepcopy(monkeys)
    mod = np.product([m.div for m in monkeys])
    play_game(monkeys2, num_rounds=10000, mod=mod)
    top_inspections = sorted([m.num_inspected for m in monkeys2], reverse=True)[:2]
    print(top_inspections[0] * top_inspections[1])
