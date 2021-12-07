import numpy as np

initial_state = np.loadtxt('/home/carl/Code/AdventOfCode/Day6/input.txt', delimiter=',', dtype=int)

def simulateOneFish(initial_state, num_days):
    fishes = [initial_state]
    for day in range(num_days):
        num_new_fishes = 0
        for idx in range(len(fishes)):
            fishes[idx] = fishes[idx] - 1
            if fishes[idx] == -1:
                fishes[idx] = 6
                num_new_fishes += 1
        for k in range(num_new_fishes):
            fishes.append(8)
        #print("After ", day, " days: ", fishes)
    return fishes

num_fish_after_num_days = np.zeros((9, 300))
for state in range(9):
    for days in range(20):
        num_fish_after_num_days[state, days] = len(simulateOneFish(state, days))
for days in range(20, 257):
    num_fish_after_num_days[0, days] = num_fish_after_num_days[6, days-1] + num_fish_after_num_days[8, days-1]
    for state in range(1,9):
        num_fish_after_num_days[state, days] = num_fish_after_num_days[0, days-state]

total_num_fish = 0
for state in initial_state:
    total_num_fish += num_fish_after_num_days[state, 256]
print(total_num_fish)