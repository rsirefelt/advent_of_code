import numpy as np

measurements = []
with open('inputs/day6') as f:
    fish_days = np.array([int(daystr) for daystr in f.readlines()[0].split(',')])

day_nr, day_count = np.unique(fish_days, return_counts=True)
fish_day_tracker = {day: count for day, count in zip(day_nr, day_count)}


for day in range(256):
    new_tracker = {}
    for index in range(1, 9):
        new_tracker[index-1] = fish_day_tracker.get(index, 0)
    new_tracker[8] = fish_day_tracker.get(0, 0)
    new_tracker[6] += fish_day_tracker.get(0, 0)
    fish_day_tracker = new_tracker

    if day in {79, 255}:
        print(sum(fish_day_tracker.values()))
