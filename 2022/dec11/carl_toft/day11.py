import numpy as np

class Monkey:
    monkeys = []
    total_denominator = 1

    def __init__(self):
        self.items = []
        self.operation = None
        self.test_denominator = None
        self.true_monkey = None
        self.false_monkey = None
        self.num_inspections = 0

    def throw_items(self, divide_worry = 1):
        for old in self.items:
            self.num_inspections = self.num_inspections + 1

            new_worry = eval(self.operation)
            if divide_worry != 1:
                new_worry = int(new_worry / divide_worry)
            new_worry = new_worry % Monkey.total_denominator

            if new_worry % self.test_denominator == 0:
                target_monkey = self.true_monkey
            else:
                target_monkey = self.false_monkey

            Monkey.monkeys[target_monkey].items.append(new_worry)

            #print(str(old) + " -> " + str(new_worry) + " to monkey " + str(target_monkey))

        self.items = []


def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseMonkeys(lines):
    monkeys = []

    monkey_num = 0
    curr_line = 0
    while curr_line < len(lines):
        curr_monkey = Monkey()
        tmp = lines[curr_line].split(' ')
        assert int(tmp[1][:-1]) == monkey_num, "Wrong monkey number!"
        curr_monkey.items = [int(item) for item in lines[curr_line + 1].split(": ")[-1].split(", ")]
        curr_monkey.operation = lines[curr_line+2].split(" = ")[-1]
        curr_monkey.test_denominator = int(lines[curr_line+3].split(" by ")[-1])
        curr_monkey.true_monkey = int(lines[curr_line+4].split(" monkey ")[-1])
        assert "true" in lines[curr_line+4], "Incorrect format!"
        curr_monkey.false_monkey = int(lines[curr_line + 5].split(" monkey ")[-1])
        assert "false" in lines[curr_line + 5], "Incorrect format!"
        monkeys.append(curr_monkey)
        monkey_num = monkey_num + 1

        curr_line = curr_line + 7

    return monkeys

# Part 1
Monkey.monkeys = parseMonkeys(parseInput("input.txt"))
for monkey in Monkey.monkeys:
    Monkey.total_denominator = Monkey.total_denominator * monkey.test_denominator

for round in range(20):
    for idx in range(len(Monkey.monkeys)):
        Monkey.monkeys[idx].throw_items(divide_worry=3.0)

inspections = np.sort(np.array([monkey.num_inspections for monkey in Monkey.monkeys]))
print("Part 1: " + str(inspections[-1]*inspections[-2]))

# Part 2
Monkey.monkeys = parseMonkeys(parseInput("input.txt"))
for monkey in Monkey.monkeys:
    Monkey.total_denominator = Monkey.total_denominator * monkey.test_denominator

for round in range(10000):
    for idx in range(len(Monkey.monkeys)):
        Monkey.monkeys[idx].throw_items(divide_worry=1)

inspections = np.sort(np.array([monkey.num_inspections for monkey in Monkey.monkeys]))
print("Part 2: " + str(inspections[-1]*inspections[-2]))
