import numpy as np
with open("dec7/rickard_sirefelt/input.txt", "r") as f:
    lines = f.readlines()

# dependency_matrix: y letter ready to go after all x letters
num_letters = 26
num_workers = 5
dependency_matrix = np.zeros((num_letters, num_letters), dtype=int)
for line in lines:
    dependency_matrix[ord(line[5]) - 65, ord(line[36]) - 65] += 1

schedule = ""
time = 0
worker_time_task = np.zeros((num_workers, 2), dtype=int)
while np.sum(dependency_matrix.diagonal()) != 2 * num_letters:
    sum_mat = sum(dependency_matrix)
    ready_to_go_inds = np.where(sum_mat == 0)[0]

    ready_workers = np.where(worker_time_task[:, 0] == 0)[0].tolist()
    for ready_to_go_ind in ready_to_go_inds:
        if len(ready_workers) > 0:
            worker_time_task[ready_workers[-1]] += [
                ready_to_go_ind + 61, ready_to_go_ind
            ]
            del ready_workers[-1]
            dependency_matrix[ready_to_go_ind, ready_to_go_ind] += 1

    finished_inds = []
    for worker in worker_time_task:
        if worker[0] != 0:
            worker[0] -= 1
            if worker[0] == 0:
                finished_inds.append(worker[1])
                worker[1] = 0

    dependency_matrix[finished_inds, :] = 0
    dependency_matrix[finished_inds, finished_inds] += 2
    time += 1

print(time)
