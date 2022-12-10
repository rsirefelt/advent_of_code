import numpy as np


def maybe_add(cycle_count, register):
    if (cycle_count - 20) % 40 == 0:
        return register * cycle_count
    return 0


def maybe_draw(cycle_count, register, screen):
    if abs(((cycle_count - 1) % 40) - register) <= 1:
        screen[cycle_count-1] = True
    return screen


with open('inputs/day10') as f:
    instructions = f.read().splitlines()

cycle = 1
register = 1
signal_strength_sum = 0
screen = np.zeros((40*6,), dtype=bool)

screen = maybe_draw(cycle, register, screen)
for instruction in instructions:
    if instruction == 'noop':
        cycle += 1
    else:
        cycle += 1
        signal_strength_sum += maybe_add(cycle, register)
        screen = maybe_draw(cycle, register, screen)
        cycle += 1
        register += int(instruction.split()[-1])
    signal_strength_sum += maybe_add(cycle, register)
    screen = maybe_draw(cycle, register, screen)

print(signal_strength_sum)
for row in range(6):
    print(''.join('#' if s else '.' for s in screen[40*row: 40*(row+1)]))
