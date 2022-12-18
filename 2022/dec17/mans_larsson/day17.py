import numpy as np


def if_pos_is_ok(y, x, rock, rock_formation):
    for ydiff in range(rock.shape[0]):
        for xdiff in range(rock.shape[1]):
            if x+xdiff < 0 or x+xdiff > 6 or y+ydiff >= rock_formation.shape[0] or \
               (rock[ydiff, xdiff] and rock_formation[y+ydiff, x+xdiff]):
                return False
    return True


with open('inputs/day17') as f:
    directions = f.read().splitlines()[0]

rock_types = [np.array([[1, 1, 1, 1]], dtype=bool),
              np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=bool),
              np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]], dtype=bool),
              np.array([[1], [1], [1], [1]], dtype=bool),
              np.array([[1, 1], [1, 1]], dtype=bool)]

diff = 2677
period = 1715
lowest_starting_index_for_period = 143

formation_depht = 10000
for n_rocks in (2022, 1000000000000):
    extra_height = 0
    current_high_point = formation_depht
    rock_formation = np.zeros((formation_depht, 7), dtype=bool)
    fall_i = 0
    rock_i = 0
    while rock_i < n_rocks:
        # check if we can use periodicity
        if rock_i >= lowest_starting_index_for_period:
            n_periods = (n_rocks - rock_i) // period
            rock_i += period * n_periods
            extra_height += diff * n_periods

        rock = rock_types[rock_i % len(rock_types)]
        rock_y = current_high_point - (3 + rock.shape[0])
        rock_x = 2

        while True:
            if directions[fall_i % len(directions)] == '<':
                if if_pos_is_ok(rock_y, rock_x - 1, rock, rock_formation):
                    rock_x -= 1

            if directions[fall_i % len(directions)] == '>':
                if if_pos_is_ok(rock_y, rock_x + 1, rock, rock_formation):
                    rock_x += 1

            fall_i += 1
            if if_pos_is_ok(rock_y + 1, rock_x, rock, rock_formation):
                rock_y += 1
            else:
                break

        rock_formation[rock_y:rock_y+rock.shape[0], rock_x:rock_x+rock.shape[1]] += rock
        current_high_point = min(np.where(rock_formation.sum(axis=1))[0])
        rock_i += 1

    print(formation_depht - current_high_point + extra_height)
