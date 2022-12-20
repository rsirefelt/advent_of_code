with open('inputs/day20') as f:
    input_numbers = [int(line) for line in f.read().splitlines()]


def mix(numbers, n_rounds, decryption_key=1):
    numbers_with_order = [(decryption_key * n, i) for i, n in enumerate(numbers)]

    for i in range(n_rounds):
        for j in range(len(numbers_with_order)):
            index = None
            for ind, (_, order) in enumerate(numbers_with_order):
                if order == j:
                    index = ind
                    break

            number = numbers_with_order.pop(index)
            new_index = (index + number[0]) % len(numbers_with_order)
            numbers_with_order.insert(new_index, (number[0], order))

    for ind, (num, _) in enumerate(numbers_with_order):
        if num == 0:
            print(sum([numbers_with_order[(ind + diff) % len(numbers_with_order)][0] for diff in (1000, 2000, 3000)]))
            return


mix(input_numbers, 1)
mix(input_numbers, 10, 811589153)
