
from copy import deepcopy
alldirs = ('e', 'w', 'se', 'sw', 'ne', 'nw')


def step(coord, dir):
    if dir == 'e':
        coord[0] += 1
    elif dir == 'w':
        coord[0] -= 1
    elif dir == 'se':
        if coord[1] % 2 == 1:
            coord[0] += 1
        coord[1] += 1
    elif dir == 'sw':
        if coord[1] % 2 == 0:
            coord[0] -= 1
        coord[1] += 1
    elif dir == 'ne':
        if coord[1] % 2 == 1:
            coord[0] += 1
        coord[1] -= 1
    elif dir == 'nw':
        if coord[1] % 2 == 0:
            coord[0] -= 1
        coord[1] -= 1


def check_pos(tiles, pos):
    count = 0
    for d in alldirs:
        npos = list(pos)
        step(npos, d)
        count += tiles.get(tuple(npos), 0)
    this = tiles.get(pos, 0)

    if this == 1 and (count == 0 or count > 2):
        return 0
    if this == 0 and count == 2:
        return 1
    return None


steps = []
with open('inputs/day24') as f:
    for line in f:
        steps.append(line.rstrip())

tiles = {}

for tilepos in steps:
    coord = [0, 0]
    i = 0
    while i < len(tilepos):
        if tilepos[i] == 'e' or tilepos[i] == 'w':
            step(coord, tilepos[i])
            i += 1
        else:
            step(coord, tilepos[i:i+2])
            i += 2

    tile_color = tiles.get(tuple(coord), 0)
    tiles[tuple(coord)] = 1 - tile_color

print(f'a) {sum(tiles.values())}')

for i in range(1, 101):
    new_tiles = deepcopy(tiles)
    checked_positions = set()
    for pos, tile_color in tiles.items():
        if pos not in checked_positions:
            isblack = check_pos(tiles, pos)
            if isblack is not None:
                new_tiles[pos] = isblack
            # checked_positions.add(pos)
            for d in alldirs:
                posn = list(pos)
                step(posn, d)
                isblack = check_pos(tiles, tuple(posn))
                if isblack is not None:
                    new_tiles[tuple(posn)] = isblack
                # checked_positions.add(tuple(posn))

    tiles = new_tiles
    print(f'{i} - {sum(tiles.values())}')
