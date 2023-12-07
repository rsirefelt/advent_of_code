import numpy as np

num_cards = np.zeros((1000,), dtype=int)
score = 0
index = 0
with open('inputs/day4') as f:
    for line in f:
        index += 1
        num_cards[index] += 1

        data = line.rstrip().split('|')

        winning = set(int(ch) for ch in data[0].split()[2:])
        my = set(int(ch) for ch in data[1].split())
        matches = len(my.intersection(winning))

        if matches > 0:
            score += 2**(matches-1)

        num_cards[index+1:index+1+matches] += num_cards[index]

print(score)
print(sum(num_cards))
