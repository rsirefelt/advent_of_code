import numpy as np

input_ = np.sort(np.loadtxt("input.txt", dtype=np.int32))

# Part 1
diffs_dist = [0, 0, 1]
diffs_dist[input_[0] - 1] += 1
for i in range(1, len(input_)):
    diffs_dist[input_[i] - input_[i - 1] - 1] += 1

# Part 2:
comb_map = {0: 1}


def consec_1_diff_comb_map(n_consec_1_diff):
    if n_consec_1_diff not in comb_map and n_consec_1_diff > -1:
        # Add number of combination to previous 3 adapters together which are the possible new
        # path to the new node
        comb_map[n_consec_1_diff] = 0
        for i in range(1, 4):
            comb_map[n_consec_1_diff] += consec_1_diff_comb_map(n_consec_1_diff - i)

    return comb_map[n_consec_1_diff] if n_consec_1_diff > -1 else 0


n_consec_1_diff = []
consec_1_diff_count = 1 if input_[0] == 1 else 0
for i in range(1, len(input_)):
    if input_[i] - input_[i - 1] == 1:
        consec_1_diff_count += 1
    else:
        n_consec_1_diff.append(consec_1_diff_count)
        consec_1_diff_count = 0

n_consec_1_diff.append(consec_1_diff_count)  # Last three diff
consec_1_comb = list(map(lambda x: consec_1_diff_comb_map(x), n_consec_1_diff))
tot_adapter_comb = np.prod(consec_1_comb)

print(f"1) 1 jolt diffs times 3 jolt diffs: {diffs_dist[0] * diffs_dist[2]}")
print(f"2) Number of adapter combinations: {tot_adapter_comb}")
