from collections import deque
from copy import deepcopy

player1in = deque()
player2in = deque()
mode = 0
with open('inputs/day22') as f:
    for line in f:
        if mode == 0:
            if line.startswith('Player 2:'):
                mode = 1
                continue
            elif line == '\n' or line.startswith('Player'):
                continue
            else:
                player1in.append(int(line.rstrip()))
        else:
            if line == '\n' or line.startswith('Player'):
                continue
            else:
                player2in.append(int(line.rstrip()))


player1 = deepcopy(player1in)
player2 = deepcopy(player2in)

while not (len(player1) == 0 or len(player2) == 0):
    val1 = player1.popleft()
    val2 = player2.popleft()

    if val1 > val2:
        player1.append(val1)
        player1.append(val2)
    else:
        player2.append(val2)
        player2.append(val1)

winner = player2 if len(player1) == 0 else player1

mul = len(winner)
score = 0
while not len(winner) == 0:
    score += mul*winner.popleft()
    mul -= 1

print(f'a) {score}')

player1 = deepcopy(player1in)
player2 = deepcopy(player2in)


def play_game(p1, p2):

    prev_p1_cards = set()
    while not (len(p1) == 0 or len(p2) == 0):
        val1 = p1.popleft()
        val2 = p2.popleft()

        if val1 <= len(p1) and val2 <= len(p2):
            pp1 = deepcopy(p1)
            pp2 = deepcopy(p2)
            newp1 = deque()
            newp2 = deque()
            for _ in range(val1):
                newp1.append(pp1.popleft())
            for _ in range(val2):
                newp2.append(pp2.popleft())
            player1_wins, _ = play_game(newp1, newp2)
        else:
            player1_wins = val1 > val2

        if player1_wins:
            p1.append(val1)
            p1.append(val2)
        else:
            p2.append(val2)
            p2.append(val1)

        if tuple(p1) in prev_p1_cards:
            return True, p1
        prev_p1_cards.add(tuple(p1))

    if len(p1) == 0:
        return False, p2
    else:
        return True, p1


player1_wins, winner = play_game(player1, player2)

mul = len(winner)
score = 0
while not len(winner) == 0:
    score += mul*winner.popleft()
    mul -= 1

print(f'b) {score}')
