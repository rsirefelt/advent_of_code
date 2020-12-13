import time
import numpy as np

t = time.process_time()

start_time = 1000417
bus_ids = (23, None, None, None, None, None, None, None, None, None, None, None, None, 41, None, None, None, 37, None,
           None, None, None, None, 479, None, None, None, None, None, None, None, None, None, None, None, None, 13,
           None, None, None, 17, None, None, None, None, None, None, None, None, None, None, None, 29, None, 373, None,
           None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 19)

active_bus_ids = tuple(id for id in bus_ids if id is not None)
waiting_times = np.array([id - (start_time % id) for id in active_bus_ids])

index_for_bus = np.argmin(waiting_times)

print(f'a) {waiting_times[index_for_bus] * active_bus_ids[index_for_bus]}')
bus_ids_d = {i: id for i, id in enumerate(bus_ids) if id is not None}


def eval_timestamp(timestamp, id_dict):
    new_ind = None
    for order, id in id_dict.items():
        if (timestamp + order) % id != 0:
            return False, new_ind
        else:
            new_ind = order
    return True, new_ind


correct_ids = set()
step = 1
current_time = 100000000000000
while True:
    done, ind_to_add = eval_timestamp(current_time, bus_ids_d)
    if done:
        break

    if ind_to_add is not None:
        step *= bus_ids_d[ind_to_add]
        del bus_ids_d[ind_to_add]

    current_time += step

print(f'b) {current_time}')
print(f'total runtime {time.process_time() - t} seconds')
