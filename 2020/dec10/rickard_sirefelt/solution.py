import numpy as np

input_ = np.sort(np.loadtxt("input.txt", dtype=np.int32))

# Part 1
diffs_dist = [0, 0, 1]
diffs_dist[input_[0] - 1] += 1
for i in range(1, len(input_)):
    diffs_dist[input_[i] - input_[i - 1] - 1] += 1

# Part 2:
n_consec_1_diff = []
consec_1_diff_count = 1 if input_[0] == 1 else 0
for i in range(1, len(input_)):
    if input_[i] - input_[i - 1] == 1:
        consec_1_diff_count += 1
    else:
        n_consec_1_diff.append(consec_1_diff_count)
        consec_1_diff_count = 0

n_consec_1_diff.append(consec_1_diff_count)  # Last three diff
consec_1_diff_comb_map = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
consec_1_comb = list(map(lambda x: consec_1_diff_comb_map[x], n_consec_1_diff))
tot_adapter_comb = np.prod(consec_1_comb)

print(f"1) 1 jolt diffs times 3 jolt diffs: {diffs_dist[0] * diffs_dist[2]}")
print(f"2) Number of adapter combinations: {tot_adapter_comb}")

"""
consec_1_diff_comb_map:
# Two consecutive ones
4 5 6
4 6

# Three consecutive ones
4 5 6 7
4 5 7
4 6 7
4 7

# Four consecutive ones
4 5 6 7 8
4 5 6 8
4 5 7 8
4 5 8
4 6 7 8
4 6 8
4 7 8
"""
