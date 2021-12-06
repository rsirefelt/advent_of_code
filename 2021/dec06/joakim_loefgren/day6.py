def parse_input(file_path='./input_day6.txt'):
    with open(file_path, 'r') as f:
        text = f.read()

    return [int(n) for n in text.split(',')]


def propagate(occupations, num_days):
    for _ in range(num_days):
        num_new = occupations[0]
        for n in range(8):
            occupations[n] = occupations[n + 1]
        occupations[6] += num_new
        occupations[8] = num_new
    return sum(occupations.values())


def get_occupations(states):
    occupations = {n: 0 for n in range(9)}
    for s in states:
        occupations[s] += 1
    return occupations


if __name__ == '__main__':
    states = parse_input('./input_day6.txt')

    # Part I
    occupations = get_occupations(states)
    print(propagate(occupations, num_days=80))

    # Part II
    occupations = get_occupations(states)
    print(propagate(occupations, num_days=256))
