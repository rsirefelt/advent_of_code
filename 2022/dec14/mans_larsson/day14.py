import numpy as np


def print_cave(cave, depth, width):
    chars = {0: '.', 1: '#', 2: 'o'}
    for i in range(depth):
        print(''.join(chars[cave[i, j]] for j in range(500-width//2, 500 + width//2, 1)))


def drop_sand(cave, sand_index, lowest_allowed):
    more_sand = True

    while more_sand:
        current_index = sand_index

        while current_index[0] <= lowest_allowed:
            is_stuck = True
            for diffs in ((1, 0), (1, -1), (1, 1)):
                maybe_next = (current_index[0] + diffs[0], current_index[1] + diffs[1])
                if cave[maybe_next] == 0:
                    current_index = maybe_next
                    is_stuck = False
                    break

            if is_stuck:
                if current_index == sand_index:
                    more_sand = False
                cave[current_index] = 2
                break
        else:
            more_sand = False


with open('inputs/day14') as f:
    path_strs = f.read().splitlines()


for add_floor in (False, True):
    cave = np.zeros((200, 1000))
    sand_index = (0, 500)

    for path_str in path_strs:
        points = path_str.split(' -> ')
        for i in range(len(points) - 1):
            start_x, start_y = (int(p) for p in points[i].split(','))
            stop_x, stop_y = (int(p) for p in points[i+1].split(','))

            if start_x == stop_x:
                a, b = (start_y, stop_y) if start_y < stop_y else (stop_y, start_y)
                cave[a:b+1, start_x] = 1
            elif start_y == stop_y:
                a, b = (start_x, stop_x) if start_x < stop_x else (stop_x, start_x)
                cave[start_y, a:b+1] = 1

    lowest_allowed = np.where(cave.sum(axis=1))[0].max()
    if add_floor:
        cave[lowest_allowed+2, :] = 1
        lowest_allowed += 2

    drop_sand(cave, sand_index, lowest_allowed)
    print((cave == 2).sum())
