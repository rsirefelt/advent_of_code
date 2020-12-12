import math

commands = list()
with open('inputs/day12') as f:
    for line in f:
        line = line.rstrip()
        commands.append((line[0], int(line[1:])))


pos = complex(0, 0)
dir = complex(1, 0)

deg_to_rad = math.pi / 180
for command in commands:
    if command[0] == 'L':
        angle = deg_to_rad * command[1]
        dir *= complex(round(math.cos(angle)), round(math.sin(angle)))
    elif command[0] == 'R':
        angle = -1 * deg_to_rad * command[1]
        dir *= complex(round(math.cos(angle)), round(math.sin(angle)))
    elif command[0] == 'N':
        pos += complex(0, command[1])
    elif command[0] == 'S':
        pos -= complex(0, command[1])
    elif command[0] == 'E':
        pos += complex(command[1], 0)
    elif command[0] == 'W':
        pos -= complex(command[1], 0)
    elif command[0] == 'F':
        pos += command[1] * dir

print(f'a) {abs(pos.real) + abs(pos.imag)}')

pos = complex(0, 0)
wp = complex(10, 1)

for command in commands:
    if command[0] == 'L':
        angle = deg_to_rad * command[1]
        wp *= complex(round(math.cos(angle)), round(math.sin(angle)))
    elif command[0] == 'R':
        angle = -1 * deg_to_rad * command[1]
        wp *= complex(round(math.cos(angle)), round(math.sin(angle)))
    elif command[0] == 'N':
        wp += complex(0, command[1])
    elif command[0] == 'S':
        wp -= complex(0, command[1])
    elif command[0] == 'E':
        wp += complex(command[1], 0)
    elif command[0] == 'W':
        wp -= complex(command[1], 0)
    elif command[0] == 'F':
        pos += command[1] * wp

print(f'b) {abs(pos.real) + abs(pos.imag)}')
