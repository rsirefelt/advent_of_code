import numpy as np
from dateutil.parser import parse

schedule = []
with open("dec4/rickard_sirefelt/input.txt", "r") as f:
    for i, line in enumerate(f):
        change = {}
        change["datetime"] = parse(line[1:17])
        change["event"] = line.split(']')[1].lstrip()
        schedule.append(change)

schedule.sort(key=lambda change: change["datetime"])

guard_sleep_time = {}
guard_on_shift = 0
start_sleep, end_sleep = 0, 0
for change in schedule:
    if change["event"][0] == "G":
        guard_on_shift = int(
            change["event"].split("#")[1].split("b")[0].rstrip())
    elif change["event"][0] == "f":
        sleep_array = np.zeros(60)
        start_sleep = change["datetime"].minute
    else:
        end_sleep = change["datetime"].minute
        sleep_array[start_sleep:end_sleep] += 1
        if guard_on_shift not in guard_sleep_time:
            guard_sleep_time[guard_on_shift] = sleep_array
        else:
            guard_sleep_time[guard_on_shift] = np.vstack(
                [guard_sleep_time[guard_on_shift], sleep_array])
max_sleepiest_min = 0
max_sleep_in_max_sleepiest_min = 0
sleepiest_guard = 0
for guard, guard_sleep in guard_sleep_time.items():
    tot_sleep_each_min = sum(guard_sleep)
    sleepiest_min = np.argmax(tot_sleep_each_min)
    sleep_in_sleepiest_min = tot_sleep_each_min[sleepiest_min]
    if sleep_in_sleepiest_min > max_sleep_in_max_sleepiest_min:
        max_sleep_in_max_sleepiest_min = sleep_in_sleepiest_min
        max_sleepiest_min = sleepiest_min
        sleepiest_guard = guard
print(sleepiest_guard * max_sleepiest_min)