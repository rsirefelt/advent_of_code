import numpy as np

# Part 1
with open("input.txt", "r") as f:
    earliest_time = int(f.readline())
    active_busses = [int(id_) for id_ in f.readline().replace("x,", "").split(",")]

minimum_wait_id = 0
minimum_wait = max(active_busses)
for buss_id in active_busses:
    min2wait = buss_id - (earliest_time % buss_id)
    if min2wait < minimum_wait:
        minimum_wait = min2wait
        minimum_wait_id = buss_id

print(f"1) Earliest buss id x minutes to wait: {minimum_wait * minimum_wait_id}")


# Part 2
active_busses = list()
with open("input.txt", "r") as f:
    throw_away = f.readline()
    t_count = 0
    for c in f.readline().split(","):
        if c != "x":
            if t_count % int(c) == 0:
                active_busses.append([int(c), int(c)])
            else:
                active_busses.append([int(c), t_count % int(c)])
        t_count += 1


def check_valid_t(t, busses):
    valid = True
    for buss in busses:
        if buss[0] - t % buss[0] != buss[1]:
            valid = False
            break
    return valid


active_busses = np.array(active_busses, dtype=np.int64)
t_step = 1
t = 0
t_step_check = 2
last_valid_t_step = 0
not_valid_t = True

while not_valid_t:
    not_valid_t = not check_valid_t(t, active_busses)

    if not_valid_t:
        # Check if step size can be updated
        valid_t_update = check_valid_t(t, active_busses[:t_step_check, :])
        if valid_t_update:
            if last_valid_t_step != 0:
                t_step_check += 1
                t_step = t - last_valid_t_step
                last_valid_t_step = 0
            else:
                last_valid_t_step = t

        t += t_step

print(f"2) Valid time is: {t}")
