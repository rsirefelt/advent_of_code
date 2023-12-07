from collections import Counter


def classify_hand(cards):
    if not any([c == 1 for c in cards]):
        sorted_occ = sorted(Counter(cards).values())

        if sorted_occ[-1] == 5:
            return 6
        elif sorted_occ[-1] == 4:
            return 5
        elif sorted_occ[-1] == 3:
            if sorted_occ[-2] == 2:
                return 4
            else:
                return 3
        elif sorted_occ[-1] == 2:
            if sorted_occ[-2] == 2:
                return 2
            else:
                return 1
        return 0
    else:  # try all combinations
        cards = list(cards)
        for joker_index in range(5):
            if cards[joker_index] == 1:
                break
        all_possible_classes = []
        for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]:
            cards[joker_index] = i
            all_possible_classes.append(classify_hand(tuple(cards)))

        return max(all_possible_classes)


class Hand():
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = bid

    def get_sort_key(self):
        return (classify_hand(self.cards), ) + self.cards


def run(joker_value):
    card_convert = {'T': 10, 'J': joker_value, 'Q': 12, 'K': 13, 'A': 14}
    for i in range(10):
        card_convert[str(i)] = i

    hands = []

    with open('inputs/day7') as f:
        for line in f:
            hand, bid = line.rstrip().split()
            hands.append(Hand(tuple(card_convert[ch] for ch in hand), int(bid)))

    sorted_hands = sorted(hands, key=Hand.get_sort_key)

    winnings = sum(rank * hand.bid for rank, hand in enumerate(sorted_hands, start=1))
    print(winnings)


if __name__ == '__main__':
    run(joker_value=11)
    run(joker_value=1)
