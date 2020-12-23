""" Advent of Code Day 22 """
from collections import deque
from itertools import islice


def load_input(input_file):
    with open(input_file) as fp:
        decks_raw = fp.read().split("\n\n")
    deck1 = deque([int(c) for c in decks_raw[0].split("\n")[1:]])
    deck2 = deque([int(c) for c in decks_raw[1].split("\n")[1:-1]])
    return deck1, deck2


def calc_score(deck):
    num_cards = len(deck)
    return sum([c * (num_cards - i) for i, c in enumerate(deck)])


def play_regular_combat(deck1, deck2):
    i = 0
    while True:
        i += 1
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
        if len(deck2) == 0:
            winner = 1
            return winner
        elif len(deck1) == 0:
            winner = 2
            return winner


def play_recurisve_combat(deck1, deck2):
    seen_deck1 = []
    seen_deck2 = []
    i = 0
    while True:
        i += 1
        # check for infinite recursion
        match1 = next((i for i, d in enumerate(seen_deck1) if d == deck1), -1)
        match2 = next((i for i, d in enumerate(seen_deck2) if d == deck2), -2)
        if match1 == match2:
            winner = 1
            return winner
        else:
            seen_deck1.append(deck1.copy())
            seen_deck2.append(deck2.copy())

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if len(deck1) >= card1 and len(deck2) >= card2:
            deck1_sub = deque(islice(deck1, 0, card1))
            deck2_sub = deque(islice(deck2, 0, card2))
            round_winner = play_recurisve_combat(deck1_sub, deck2_sub)
        else:
            round_winner = (card2 > card1) + 1

        if round_winner == 1:
            deck1.extend([card1, card2])
        elif round_winner == 2:
            deck2.extend([card2, card1])

        if len(deck2) == 0:
            winner = 1
            return winner
        elif len(deck1) == 0:
            winner = 2
            return winner


if __name__ == "__main__":
    deck1_orig, deck2_orig = load_input("./input_day22.txt")

    # Part I
    deck1 = deck1_orig.copy()
    deck2 = deck2_orig.copy()
    winner = play_regular_combat(deck1, deck2)
    winning_deck = deck1
    if winner == 2:
        winning_deck = deck2
    print(calc_score(winning_deck))

    # Part II
    deck1 = deck1_orig.copy()
    deck2 = deck2_orig.copy()
    winner = play_recurisve_combat(deck1, deck2)
    winning_deck = deck1
    if winner == 2:
        winning_deck = deck2
    print(calc_score(winning_deck))
