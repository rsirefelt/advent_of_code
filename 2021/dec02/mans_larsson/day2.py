
horizontal = 0
depth = 0
depth_with_aim = 0
aim = 0

with open('inputs/day2') as f:
    for line in f:
        direction, units = line.rstrip().split()
        if direction == 'forward':
            horizontal += int(units)
            depth_with_aim += int(units) * aim
        elif direction == 'down':
            depth += int(units)
            aim += int(units)
        elif direction == 'up':
            depth -= int(units)
            aim -= int(units)

print(horizontal*depth)
print(horizontal*depth_with_aim)
