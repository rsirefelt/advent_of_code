from dataclasses import dataclass
from typing import Tuple

import numpy as np
from scipy.ndimage import binary_dilation, generate_binary_structure


@dataclass
class Blizzard:
    pos: Tuple[int, int]
    dir: Tuple[int, int]

    def move(self, map_size):
        self.pos = ((self.pos[0] + self.dir[0]) % map_size[0], (self.pos[1] + self.dir[1]) % map_size[1])


with open('inputs/day24') as f:
    map_lines = f.read().splitlines()


blizzards = []
for y, map_line in enumerate(map_lines[1:-1]):
    for x, ch in enumerate(map_line[1:-1]):
        if ch == '>':
            blizzards.append(Blizzard(pos=(y, x), dir=(0, 1)))
        elif ch == '<':
            blizzards.append(Blizzard(pos=(y, x), dir=(0, -1)))
        elif ch == '^':
            blizzards.append(Blizzard(pos=(y, x), dir=(-1, 0)))
        elif ch == 'v':
            blizzards.append(Blizzard(pos=(y, x), dir=(1, 0)))


neighbor_elem = generate_binary_structure(rank=2, connectivity=1)
populated_map = np.zeros((len(map_lines) - 2, len(map_line) - 2), dtype=bool)

start = (0, 0)
goal = (populated_map.shape[0]-1, populated_map.shape[1]-1)
success_count = 0

round = 0
while success_count < 3:
    reset = False
    if populated_map[goal]:
        start, goal = goal, start
        reset = True
        success_count += 1
        round += 1

        print(round)
        for blizzard in blizzards:
            blizzard.move(populated_map.shape)

    for blizzard in blizzards:
        blizzard.move(populated_map.shape)

    if reset:
        populated_map = np.zeros((len(map_lines) - 2, len(map_line) - 2), dtype=bool)
    else:
        populated_map = binary_dilation(populated_map, neighbor_elem)
        populated_map[start] = True

    blizzard_map = np.zeros_like(populated_map)
    blizzard_map[tuple([tuple(b.pos[0] for b in blizzards), tuple(b.pos[1] for b in blizzards)])] = True
    populated_map = np.logical_and(populated_map, np.logical_not(blizzard_map))
    round += 1
