import numpy as np
import time
from collections import deque

def read_decks(filename):
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        deck1 = []
        deck2 = []
        player1 = True
        for string in data_lines:
            if string.rstrip() =='Player 1:':
                player1 = True
            elif string.rstrip() == 'Player 2:':
                player1 = False
            elif string.rstrip() == '':
                continue
            else:
                if player1:
                    deck1.append(int(string.rstrip()))
                else:
                    deck2.append(int(string.rstrip()))

    return deque(deck1), deque(deck2)


def move_cards(winner, loser):
    loser.rotate(-1)
    card_to_move = loser.pop()
    # print(card_to_move)
    winner.rotate(-1)
    winner.append(card_to_move)

def compare_decks(deck1, deck2):
    if deck1[0] > deck2[0]:
        move_cards(deck1, deck2)
    else:
        move_cards(deck2, deck1)

def create_copy_of_decks(deck1, deck2):
    # print(deck1)
    deck1_copy = deck1.copy()
    deck2_copy = deck2.copy()
    # print(deck1_copy)
    num_cards_1 = deck1_copy.popleft()
    num_cards_2 = deck2_copy.popleft()

    out_copy_deck1 = deque([])
    for i in range(num_cards_1):
        out_copy_deck1.append(deck1_copy.popleft())

    out_copy_deck2 = deque([])
    for i in range(num_cards_2):
        out_copy_deck2.append(deck2_copy.popleft())

    return out_copy_deck1, out_copy_deck2
   
def calculate_winner_score(deck1, deck2):
    if len(deck1) >  len(deck2):
        winner = deck1
    else:
        winner = deck2

    num_cards = len(winner)
    sum_cards = 0
    for ind in range(num_cards):
        sum_cards += winner[ind] * (num_cards - ind)

    return sum_cards

def part1 (deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        compare_decks(deck1, deck2)

    print('Winner score part 1: %i' %calculate_winner_score(deck1, deck2))

def recursive_combat(deck1, deck2, all_games):
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1 in all_games:
            deck2.clear()
            return
        elif len(deck1) > deck1[0] and len(deck2) > deck2[0]:
            all_games.append(deck1.copy())
            deck1_copy,deck2_copy = create_copy_of_decks(deck1, deck2)
  
            recursive_combat(deck1_copy,deck2_copy, all_games.copy())
            
            if len(deck1_copy) >  len(deck2_copy):
                move_cards(deck1, deck2)
            else:
                move_cards(deck2, deck1)

        else:
            all_games.append(deck1.copy())
            compare_decks(deck1, deck2)

def main():
    deck1, deck2 = read_decks('testdata.csv')
    deck1, deck2 = read_decks('data.csv')

    start = time.time()
    part1 (deck1.copy(), deck2.copy())
    end = time.time()
    print('Part 1 time: %f' %(end - start))
    
    start = time.time()
    all_games = []
    recursive_combat(deck1, deck2, all_games)
    print('Winner score part 2: %i' %calculate_winner_score(deck1, deck2))
    end = time.time()
    print('Part 1 time: %f' %(end - start))

if __name__ == "__main__": main()