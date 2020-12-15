""" Advent of Code Day 15 """

def play(starting, max_turn):
    when = {n: i + 1 for i, n in enumerate(starting[:-1])}
    spoken = starting[-1]
    for turn in range(len(starting) + 1, max_turn+1):
        turn_last = when.get(spoken, None)
        when[spoken] = turn - 1
        if turn_last is None:
            spoken = 0
        else:
            spoken = turn - turn_last - 1
    return spoken

if __name__ == "__main__":
    starting = [9, 6, 0, 10, 18, 2, 1]

    # Part I
    spoken = play(starting, max_turn=2020)
    print(spoken)

    # Part II
    spoken = play(starting, max_turn=30000000)
    print(spoken)
