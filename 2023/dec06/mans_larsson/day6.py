from math import sqrt, ceil, floor


def win_count(time, distance):
    # analytical solution to second order eq
    sqrt_expr = sqrt(time**2/4 - distance)
    low = ceil(time/2 - sqrt_expr)
    high = floor(time/2 + sqrt_expr)
    return high - low + 1


with open('inputs/day6') as f:
    lines = f.readlines()
    times = [int(t) for t in lines[0].rstrip().split()[1:]]
    distances = [int(t) for t in lines[1].rstrip().split()[1:]]

# A
multiply = 1
for time, distance in zip(times, distances):
    multiply *= win_count(time, distance)

print(multiply)

# B
time = int(''.join(lines[0].rstrip().split()[1:]))
distance = int(''.join(lines[1].rstrip().split()[1:]))

print(win_count(time, distance))
