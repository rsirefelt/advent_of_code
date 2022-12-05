
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Move:
    num: int
    start: int
    stop: int


with open('inputs/day5') as f:
    data = f.read().splitlines()

stacks = [[] for i in range(9)]
for line_i in range(7, -1, -1):
    for stack_i in range(9):
        letter = data[line_i][1 + stack_i*4]
        if letter != ' ':
            stacks[stack_i].append(letter)

moves = []
for line in data[10:]:
    move_data = line.split()
    moves.append(Move(int(move_data[1]), int(move_data[3])-1, int(move_data[5])-1))

stacks_a = deepcopy(stacks)
stacks_b = deepcopy(stacks)


def apply_move_a(move: Move):
    for _ in range(move.num):
        crate = stacks_a[move.start].pop()
        stacks_a[move.stop].append(crate)


def apply_move_b(move: Move):
    crates = stacks_b[move.start][-move.num:]
    stacks_b[move.stop].extend(crates)
    stacks_b[move.start] = stacks_b[move.start][:-move.num]


for move in moves:
    apply_move_a(move)
    apply_move_b(move)

print(''.join(s[-1] for s in stacks_a))
print(''.join(s[-1] for s in stacks_b))
