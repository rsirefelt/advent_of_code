with open('inputs/day21') as f:
    monkey_lines = f.read().splitlines()

monkeys = dict()
for monkey_line in monkey_lines:
    monkey, number = monkey_line.split(': ')
    monkeys[monkey] = number


def calc_monkey_number(monkey_name, humn_value):
    monkeys['humn'] = humn_value
    monkey_number = monkeys[monkey_name]
    try:
        num = int(monkey_number)
        return num
    except ValueError:
        first_monkey, operator, second_monkey = monkey_number.split()
        if operator == '+':
            return calc_monkey_number(first_monkey, humn_value) + calc_monkey_number(second_monkey, humn_value)
        if operator == '-':
            return calc_monkey_number(first_monkey, humn_value) - calc_monkey_number(second_monkey, humn_value)
        if operator == '*':
            return calc_monkey_number(first_monkey, humn_value) * calc_monkey_number(second_monkey, humn_value)
        if operator == '/':
            return calc_monkey_number(first_monkey, humn_value) / calc_monkey_number(second_monkey, humn_value)
        return None


root_val = calc_monkey_number('root', humn_value=monkeys['humn'])
print(int(root_val))


# the difference decreases linearly with humn (plotted som example diffs)
first_monkey, _, second_monkey = monkeys['root'].split()
second_monkey_val = calc_monkey_number(second_monkey, 0)  # does not depent on humn


def diff(humn):
    return -1*(calc_monkey_number(first_monkey, humn) - second_monkey_val)


def interval_halving(func, low, high):
    while high - low > 1:
        mid = int(low + (high - low) / 2)
        if func(mid) == 0:
            return mid
        if func(mid) > 0:
            high, low = mid, low
        else:
            high, low = high, mid
    return None


print(interval_halving(diff, int(-1e15), int(1e15)))
