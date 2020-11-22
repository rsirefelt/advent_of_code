import numpy as np
with open("dec7/rickard_sirefelt/input.txt", "r") as f:
    lines = f.readlines()

# dependency_matrix: y letter ready to go after all x letters
dependency_matrix = np.zeros((26, 26), dtype=int)
for line in lines:
    dependency_matrix[ord(line[5]) - 65, ord(line[36]) - 65] += 1

schedule = ""
while len(schedule) < 26:
    sum_mat = sum(dependency_matrix)
    ready_to_go_ind = np.where(sum_mat == 0)[0]

    schedule += chr(ready_to_go_ind[0] + 65)
    dependency_matrix[ready_to_go_ind[0], :] = 0
    dependency_matrix[ready_to_go_ind[0], ready_to_go_ind[0]] += 1

print(schedule)
