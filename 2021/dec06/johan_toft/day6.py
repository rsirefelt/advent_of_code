from aoc_helper import download_advent_of_code_input

download_advent_of_code_input(2021, 6)

with open('input.txt', 'r') as f:
    ls = f.read().split(',')

fishes = {}
for i in range(0,10):
    fishes[i] = 0

original_fish = [int(x) for x in ls]

for fish in original_fish:
    fishes[fish] += 1

def simulate_fishies(fishes, numdays):
    fishes = fishes.copy()
    for i in range(0, numdays):
        next_fishes = {x : 0 for x in range(0,10)}
        for i in range(1,9):
            next_fishes[i] = fishes[i+1]
        next_fishes[8] += fishes[0]
        next_fishes[6] += fishes[0]
        next_fishes[0] = fishes[1]
        fishes = next_fishes
    return fishes, sum(fishes.values())

print(f"Part 1: {simulate_fishies(fishes, 80)[1]}")
print(f"Part 2: {simulate_fishies(fishes, 256)[1]}")