import numpy as np

data = np.loadtxt("dec8/rickard_sirefelt/input.txt", dtype=int)


def sum_my_child(i):
    sum_tot = 0
    num_childs = data[i]
    num_meta_data = data[i + 1]
    next_data_i = i + 2
    for _ in range(num_childs):
        sum_child, next_data_i = sum_my_child(next_data_i)
        sum_tot += sum_child

    sum_tot += sum(data[next_data_i:next_data_i + num_meta_data])

    return sum_tot, next_data_i + num_meta_data


print(sum_my_child(0)[0])
