import numpy as np

data = np.loadtxt("dec8/rickard_sirefelt/input.txt", dtype=int)


def val_of_child(i):
    num_childs = data[i]
    num_meta_data = data[i + 1]
    next_data_i = i + 2
    val_of_childs = []
    for _ in range(num_childs):
        val, next_data_i = val_of_child(next_data_i)
        val_of_childs.append(val)

    val = 0
    meta_data_entries = data[next_data_i:next_data_i + num_meta_data]
    for meta_data_entry in meta_data_entries:
        if num_childs == 0:
            val += meta_data_entry
        elif meta_data_entry < num_childs + 1:
            val += val_of_childs[meta_data_entry - 1]

    return val, next_data_i + num_meta_data


print(val_of_child(0)[0])
