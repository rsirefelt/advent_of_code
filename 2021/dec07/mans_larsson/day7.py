import numpy as np

with open('inputs/day7') as f:
    crab_positions = np.array([int(daystr) for daystr in f.readlines()[0].split(',')])

min_fuel_a = 1e10
best_pos_a = None
min_fuel_b = 1e10
best_pos_b = None
for this_pos in range(min(crab_positions), max(crab_positions)):
    abs_diffs = np.abs(crab_positions-this_pos)
    fuel_cost_a = np.sum(abs_diffs)
    fuel_cost_b = np.sum([np.sum(range(ad+1)) for ad in abs_diffs])

    if fuel_cost_a < min_fuel_a:
        min_fuel_a = fuel_cost_a
        best_pos_a = this_pos
    if fuel_cost_b < min_fuel_b:
        min_fuel_b = fuel_cost_b
        best_pos_b = this_pos

print(int(min_fuel_a))
print(int(min_fuel_b))
