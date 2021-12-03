import numpy as np


def count_zeros(strs, str_len):
    zero_counts = np.zeros((meas_len, 1))
    for pos in range(str_len):
        for meas in strs:
            if meas[pos] == '0':
                zero_counts[pos] += 1
    return zero_counts


measurements = []
with open('inputs/day3') as f:
    for line in f:
        meas = line.rstrip()
        meas_len = len(meas)
        measurements.append(meas)

zero_counts = count_zeros(measurements, meas_len)

gamma = 0
epsilon = 0
for pos in range(meas_len):
    if zero_counts[pos] > len(measurements) / 2:
        epsilon += 2 ** (meas_len - pos - 1)
    else:
        gamma += 2 ** (meas_len - pos - 1)

print(epsilon*gamma)

oxygen_measurements = measurements
co2_measurments = measurements
for pos in range(meas_len):
    new_ox = []
    new_co2 = []

    zero_counts = count_zeros(oxygen_measurements, meas_len)
    oxygen_token = '0' if zero_counts[pos] > len(oxygen_measurements) / 2 else '1'
    for meas in oxygen_measurements:
        if meas[pos] == oxygen_token:
            new_ox.append(meas)

    zero_counts = count_zeros(co2_measurments, meas_len)
    co2_token_token = '1' if zero_counts[pos] > len(co2_measurments) / 2 else '0'
    for meas in co2_measurments:
        if meas[pos] == co2_token_token:
            new_co2.append(meas)

    if len(new_ox) == 1:
        oxygen = int(new_ox[0], 2)
    if len(new_co2) == 1:
        co2 = int(new_co2[0], 2)

    oxygen_measurements = new_ox
    co2_measurments = new_co2

print(oxygen*co2)
