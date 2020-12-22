import numpy as np
import copy


def score(result_dict):
    sum_ = 0
    for player, deck in result_dict.items():
        # Loosing player
        if len(deck) == 0:
            continue

        for i, elem in enumerate(deck[::-1]):
            sum_ += (i + 1) * elem
    return sum_


def combat(game_dict):
    results = copy.deepcopy(game_dict)
    while not any([len(list_) == 0 for list_ in results.values()]):

        cards = []
        for player in results.keys():
            card = results[player].pop(0)
            cards.append(card)

        # +1 as players are not 0-indexed
        winning_player = np.argmax(cards) + 1

        # Fix order of added cards
        cards.sort(reverse=True)
        results[winning_player].extend(cards)

    return results


def recursive_combat(game_dict):
    history = {1: set(), 2: set()}
    results = copy.deepcopy(game_dict)

    while not any([len(list_) == 0 for list_ in results.values()]):

        # Slow check, but needed unhashable type.
        if tuple(results[1]) in history[1] and tuple(results[2]) in history[2]:
            return results, 1
        else:
            history[1].add(tuple(results[1]))
            history[2].add(tuple(results[2]))

        cards = []
        for player in results.keys():
            card = results[player].pop(0)
            cards.append(card)

        if len(results[1]) >= cards[0] and len(results[2]) >= cards[1]:
            # print("Spawning recursive game:")
            new_game = {}
            for i, (key, val) in enumerate(results.items()):
                new_game[key] = val[: cards[i]]

            _, winning_player = recursive_combat(new_game)
            # print(f"BACK FROM RECURSIVE GAME {winning_player}")

            if winning_player == 2:
                cards = cards[::-1]

        else:
            # +1 as players are not 0-indexed
            winning_player = np.argmax(cards) + 1

            # Fix order of added cards
            cards.sort(reverse=True)
        results[winning_player].extend(cards)

    return results, 1 if len(results[1]) > len(results[2]) else 2


if __name__ == "__main__":
    with open("input") as f:
        lines = [line for line in f.readlines()]

    lines.append("")

    players = {}
    current_player = 0
    current_deck = []
    for line in lines:
        line = line.rstrip()
        if "Player" in line:
            current_player += 1
            continue
        if line == "":
            players[current_player] = current_deck
            current_deck = []
            continue
        current_deck.append(int(line))

    game1 = combat(players)
    print(f"Result task 1: {score(game1)}")
    print(players)
    game2, _ = recursive_combat(players)
    print(game2)
    print(f"Result task 2: {score(game2)}")
