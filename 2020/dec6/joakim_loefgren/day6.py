""" Advent of Code Day 6. """


def load_input(input_file='./input_day6.txt'):
    with open(input_file, 'r') as fp:
        answer_groups = [text.strip().split('\n') for text in fp.read().split('\n\n')]

    return answer_groups


if __name__ == "__main__":
    answer_groups = load_input()

    # Part I: any yes
    count = sum([len(set(''.join(group))) for group in answer_groups])
    print(count)

    # Part II: all yes
    count = 0
    for group in answer_groups:
        common = set.intersection(*[set(ans) for ans in group])
        count += len(common)

    print(count)
