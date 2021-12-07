import numpy as np

# Read the puzzle input
crab_positions = np.loadtxt("/home/carl/Code/AdventOfCode/Day7/input.txt", delimiter=",", dtype=int)

# Part 1
position = np.median(crab_positions)
total_fuel_spent = np.sum(np.abs(position-crab_positions))
print("Part 1", total_fuel_spent)

# Part 2
start_pos = np.min(crab_positions)
end_pos = np.max(crab_positions)
total_fuel_costs = []
for pos in range(start_pos, end_pos+1):
    dists = np.abs(pos - crab_positions)
    fuel_costs = dists*(dists+1)/2
    total_cost = np.sum(fuel_costs)
    total_fuel_costs.append(total_cost)

print("Part 2:", np.min(np.array(total_fuel_costs)))