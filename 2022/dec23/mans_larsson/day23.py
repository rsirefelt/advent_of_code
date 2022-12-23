
import numpy as np


def view(elves):
    print('----------------------------------')
    elf_positions = np.argwhere(elves)
    for y in range(elf_positions[:, 0].min(), elf_positions[:, 0].max()+1):
        chars = []
        for x in range(elf_positions[:, 1].min(), elf_positions[:, 1].max()+1):
            if elves[y, x]:
                chars.append('#')
            else:
                chars.append('.')
        print(''.join(ch for ch in chars))


def get_doubles_mask(positions):
    doubles_mask = np.zeros((positions.shape[0],), dtype=bool)

    pos_count = dict()
    for this_pos in positions:
        pos_count[tuple(this_pos)] = pos_count.get(tuple(this_pos), 0) + 1

    for i, this_pos in enumerate(positions):
        if pos_count[tuple(this_pos)] > 1:
            doubles_mask[i] = True

    return doubles_mask


with open('inputs/day23') as f:
    data = f.read().splitlines()

elves = np.stack([np.array([ch == '#' for ch in line]) for line in data])
elves = np.pad(elves, 500)
elf_positions = np.argwhere(elves)

directions = ('N', 'S', 'W', 'E')

for round in range(1000000000):
    new_elf_positions = np.zeros_like(elf_positions)
    nmoves = 0
    for elf_index, elf_pos in enumerate(elf_positions):
        if elves[elf_pos[0]-1:elf_pos[0]+2, elf_pos[1]-1:elf_pos[1]+2].sum() == 1:
            new_elf_positions[elf_index] = elf_pos
            continue

        nmoves += 1
        for j in range(4):
            dir = directions[(round+j) % 4]
            if dir == 'N' and not np.any(elves[elf_pos[0]-1, elf_pos[1]-1:elf_pos[1]+2]):
                new_elf_positions[elf_index] = (elf_pos[0] - 1, elf_pos[1])
                break
            elif dir == 'S' and not np.any(elves[elf_pos[0]+1, elf_pos[1]-1:elf_pos[1]+2]):
                new_elf_positions[elf_index] = (elf_pos[0] + 1, elf_pos[1])
                break
            elif dir == 'E' and not np.any(elves[elf_pos[0]-1:elf_pos[0]+2, elf_pos[1]+1]):
                new_elf_positions[elf_index] = (elf_pos[0], elf_pos[1] + 1)
                break
            elif dir == 'W' and not np.any(elves[elf_pos[0]-1:elf_pos[0]+2, elf_pos[1]-1]):
                new_elf_positions[elf_index] = (elf_pos[0], elf_pos[1] - 1)
                break
            else:
                new_elf_positions[elf_index] = elf_pos

    if nmoves == 0:
        print(round + 1)
        break

    doubles_mask = get_doubles_mask(new_elf_positions)
    new_elf_positions[doubles_mask] = elf_positions[doubles_mask]
    elf_positions = new_elf_positions

    elves = np.zeros_like(elves)
    for pos in elf_positions:
        elves[tuple(pos)] = True

    if round == 9:
        print((elf_positions[:, 0].max()-elf_positions[:, 0].min() + 1)
              * (elf_positions[:, 1].max()-elf_positions[:, 1].min() + 1) - elves.sum())
