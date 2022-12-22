from dataclasses import dataclass

import numpy as np


@dataclass
class Edge:
    index: int
    rot: float
    needs_mirror: bool
    destination_side: str


class CubeSide:
    def __init__(self, cube_map, cube_side, index) -> None:
        self.top_left = np.argwhere(cube_map == index)[0]
        self.cube_side = cube_side

    def set_neighbours(self, right, bottom, left, top):
        self.right = right
        self.bottom = bottom
        self.left = left
        self.top = top


def view(data, every_n=10):
    for i in range(0, data.shape[0], every_n):
        print(''.join(str(j) for n, j in enumerate(data[i]) if n % every_n == 0))


def rotate(dir, angle):
    return (round(dir[1] * np.sin(angle) + dir[0] * np.cos(angle)),
            round(dir[1] * np.cos(angle) - dir[0] * np.sin(angle)))


with open('inputs/day22') as f:
    data = f.read().splitlines()

lookup = {' ': 0, '.': 1, '#': 2}
rows = []
for line in data:
    if line == '':
        break

    rows.append(np.array([lookup[ch] for ch in line]))

width = max(len(r) for r in rows)
rows = [np.pad(row, pad_width=((0, width-len(row)))) for row in rows]

monkey_map = np.stack(rows)
directions = data[-1]

pos = (0, np.min(np.where(monkey_map[0, :] == 1)[0]))
direction = (0, 1)

dir_pos = 0
while dir_pos < len(directions):
    if directions[dir_pos].isnumeric():
        next_dir_pos = dir_pos + 1
        while next_dir_pos < len(directions) and directions[next_dir_pos].isnumeric():
            next_dir_pos += 1

        steps = int(directions[dir_pos:next_dir_pos])
        dir_pos = next_dir_pos

        for _ in range(steps):
            maybe_next = ((pos[0] + direction[0]) % monkey_map.shape[0], (pos[1] + direction[1]) % monkey_map.shape[1])
            while monkey_map[maybe_next] == 0:
                maybe_next = ((maybe_next[0] + direction[0]) % monkey_map.shape[0],
                              (maybe_next[1] + direction[1]) % monkey_map.shape[1])
            if monkey_map[maybe_next] == 2:  # wall
                break
            else:
                pos = maybe_next
    else:
        direction = rotate(direction, np.pi/2 if directions[dir_pos] == 'R' else -np.pi/2)
        dir_pos += 1

facing_scores = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}

print(1000*(pos[0]+1) + 4*(pos[1]+1) + facing_scores[direction])

cube_side_len = 50
cube_map = np.zeros_like(monkey_map)

cube_count = 1
for y in range(cube_map.shape[0]):
    for x in range(cube_map.shape[1]):
        if cube_map[y, x] == 0 and monkey_map[y, x] > 0:
            cube_map[y:y+cube_side_len, x:x+cube_side_len] = cube_count
            cube_count += 1


view(cube_map)
cube_sides = {i: CubeSide(cube_map, cube_side_len, i) for i in range(1, 7)}

# set neighbour info manually
cube_sides[1].set_neighbours(right=Edge(2, 0, False, 'left'),
                             bottom=Edge(3, 0, False, 'top'),
                             left=Edge(4, np.pi, True, 'left'),
                             top=Edge(6, np.pi/2, False, 'left'))
cube_sides[2].set_neighbours(right=Edge(5, np.pi, True, 'right'),
                             bottom=Edge(3, np.pi/2, False, 'right'),
                             left=Edge(1, 0, False, 'right'),
                             top=Edge(6, 0, False, 'bottom'))
cube_sides[3].set_neighbours(right=Edge(2, -np.pi/2, False, 'bottom'),
                             bottom=Edge(5, 0, False, 'top'),
                             left=Edge(4, -np.pi/2, False, 'top'),
                             top=Edge(1, 0, False, 'bottom'))
cube_sides[4].set_neighbours(right=Edge(5, 0, False, 'left'),
                             bottom=Edge(6, 0, False, 'top'),
                             left=Edge(1, np.pi, True, 'left'),
                             top=Edge(3, np.pi/2, False, 'left'))
cube_sides[5].set_neighbours(right=Edge(2, np.pi, True, 'right'),
                             bottom=Edge(6, np.pi/2, False, 'right'),
                             left=Edge(4, 0, False, 'right'),
                             top=Edge(3, 0, False, 'bottom'))
cube_sides[6].set_neighbours(right=Edge(5, -np.pi/2, False, 'bottom'),
                             bottom=Edge(2, 0, False, 'top'),
                             left=Edge(1, -np.pi/2, False, 'top'),
                             top=Edge(4, 0, False, 'bottom'))

pos = (0, np.min(np.where(monkey_map[0, :] == 1)[0]))
direction = (0, 1)

dir_pos = 0
while dir_pos < len(directions):
    if directions[dir_pos].isnumeric():
        next_dir_pos = dir_pos + 1
        while next_dir_pos < len(directions) and directions[next_dir_pos].isnumeric():
            next_dir_pos += 1

        steps = int(directions[dir_pos:next_dir_pos])
        dir_pos = next_dir_pos

        for _ in range(steps):
            maybe_next = ((pos[0] + direction[0]) % monkey_map.shape[0], (pos[1] + direction[1]) % monkey_map.shape[1])
            meybe_new_direction = direction
            if cube_map[maybe_next] != cube_map[pos]:  # across edge of cube
                cube_side = cube_sides[cube_map[pos]]
                if direction == (0, 1):
                    rel_orth_pos = pos[0] - cube_side.top_left[0]
                    edge_info = cube_side.right
                elif direction == (1, 0):
                    rel_orth_pos = pos[1] - cube_side.top_left[1]
                    edge_info = cube_side.bottom
                elif direction == (0, -1):
                    rel_orth_pos = pos[0] - cube_side.top_left[0]
                    edge_info = cube_side.left
                elif direction == (-1, 0):
                    rel_orth_pos = pos[1] - cube_side.top_left[1]
                    edge_info = cube_side.top

                if edge_info.needs_mirror:
                    rel_orth_pos = cube_side_len - 1 - rel_orth_pos

                meybe_new_direction = rotate(direction, edge_info.rot)

                dest_cube_top_left = cube_sides[edge_info.index].top_left

                if edge_info.destination_side == 'right':
                    maybe_next = (dest_cube_top_left[0] + rel_orth_pos, dest_cube_top_left[1] + cube_side_len - 1)
                    assert meybe_new_direction == (0, -1)
                elif edge_info.destination_side == 'bottom':
                    maybe_next = (dest_cube_top_left[0] + cube_side_len - 1, dest_cube_top_left[1] + rel_orth_pos)
                    assert meybe_new_direction == (-1, 0)
                elif edge_info.destination_side == 'left':
                    maybe_next = (dest_cube_top_left[0] + rel_orth_pos, dest_cube_top_left[1])
                    assert meybe_new_direction == (0, 1)
                elif edge_info.destination_side == 'top':
                    maybe_next = (dest_cube_top_left[0], dest_cube_top_left[1] + rel_orth_pos)
                    assert meybe_new_direction == (1, 0)

                assert cube_map[maybe_next] == edge_info.index
            if monkey_map[maybe_next] == 2:  # wall
                break
            else:
                direction = meybe_new_direction
                pos = maybe_next
    else:
        direction = rotate(direction, np.pi/2 if directions[dir_pos] == 'R' else -np.pi/2)
        dir_pos += 1

print(1000*(pos[0]+1) + 4*(pos[1]+1) + facing_scores[direction])
