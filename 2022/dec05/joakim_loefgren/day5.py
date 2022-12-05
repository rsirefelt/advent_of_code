from collections import deque
import copy
import re

with open('./input.txt', 'r') as f:
    text_crates, text_moves = f.read().split('\n\n')

# build stacks of crates
lines_crates = text_crates.splitlines()
keys = [int(n) for n in lines_crates[-1].split()]
stacks = {k: deque() for k in keys}

# find indices of stacks in the crate string
matches = re.finditer('[A-Z]', lines_crates[-2])
inds = [m.start(0) for m in matches]

# fill the stacks
for layer in reversed(lines_crates[:-1]):
    for n, ind in enumerate(inds):
        c = layer[ind] 
        if c.isalpha():
            stacks[n + 1].appendleft(c)

# Part I
stacks1 = copy.deepcopy(stacks)
lines_moves = text_moves.splitlines()
for line in lines_moves:
    num, i_from, i_to = [int(d) for d in re.findall('\d+', line)]
    for _ in range(num):
        c = stacks1[i_from].popleft()
        stacks1[i_to].appendleft(c)
    

on_top = ''.join([s[0] for s in stacks1.values()])
print(on_top)

# Part II
stacks2 = copy.deepcopy(stacks)
lines_moves = text_moves.splitlines()
for line in lines_moves:
    num, i_from, i_to = [int(d) for d in re.findall('\d+', line)]
    to_move = []
    for _ in range(num):
        to_move.append(stacks2[i_from].popleft())
    for c in reversed(to_move):
        stacks2[i_to].appendleft(c)
    
on_top = ''.join([s[0] for s in stacks2.values()])
print(on_top)
