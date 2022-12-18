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


formation_depht = 40000

current_high_point = formation_depht
rock_formation = np.zeros((formation_depht, 7), dtype=bool)
fall_i = 0
all_high_points = np.zeros((20000,), dtype=int)
for rock_i in range(20000):
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
    all_high_points[rock_i] = formation_depht - current_high_point

print(all_high_points[2022])

# look for periods of equal delta heights
lowest_starting_index = 100000
lowest_period = 100000
lowest_height_diff = 100000
for offset in range(1, 2000):
    for period in range(5, 3000, 5):
        diff = all_high_points[-offset] - all_high_points[-period-offset]
        start_index = -period-offset
        eq_height_diff = True
        n_tests_true = 0
        for j in range(100000):
            if period*(j+1)+offset >= len(all_high_points):
                break
            if all_high_points[-offset-j*period] - all_high_points[-offset-(j+1)*period] != diff:
                eq_height_diff = False
                break
            else:
                start_index = -offset-(j+1)*period
                n_tests_true += 1
        if eq_height_diff and n_tests_true > 5:
            print(f'{period}: {diff} - {n_tests_true} {offset}')
            if (period, start_index) < (lowest_period, lowest_starting_index):
                lowest_starting_index = start_index
                lowest_period = period
                lowest_height_diff = diff
            break

lowest_starting_index = len(all_high_points) + lowest_starting_index  # loop uses negative indexing
