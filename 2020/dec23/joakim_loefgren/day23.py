from functools import reduce
from itertools import repeat, starmap


def play_game(cups_init, n_moves):
    cmin = min(cups_init)
    cmax = max(cups_init)
    ncups = len(cups_init)
    cups = {cups_init[k]: cups_init[k + 1] for k in range(ncups - 1)}
    cups[cups_init[-1]] = cups_init[0]
    curr = cups_init[0]
    for i in range(n_moves):
        pick1 = cups[curr]
        pick2 = cups[pick1]
        pick3 = cups[pick2]
        dest = curr - 1
        while True:
            if dest < cmin:
                dest = cmax
            if dest != pick1 and dest != pick2 and dest != pick3:
                break
            else:
                dest -= 1

        after_pick3 = cups[pick3] 
        after_dest = cups[dest]
        cups[curr] = after_pick3
        cups[dest] = pick1
        cups[pick3] = after_dest
        curr = after_pick3
    return cups


if __name__ == "__main__":
    cups_init = [3, 2, 7, 4, 6, 5, 1, 8, 9]

    # Part I
    cups = play_game(cups_init, n_moves=100)
    cups_str = ''
    cup = cups[1]
    for _ in range(len(cups) - 1):
        cups_str += str(cup)
        cup = cups[cup]
    print(cups_str)

    # Part II
    cmax = max(cups_init)
    cups_init += list(range(cmax+1, int(1e6)+1))
    cups = play_game(cups_init, n_moves=int(1e7))
    print(cups[1]*cups[cups[1]])
