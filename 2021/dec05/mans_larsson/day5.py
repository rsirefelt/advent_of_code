import numpy as np

lines = np.zeros((1000, 1000), dtype=np.int32)
lines_b = np.zeros((1000, 1000), dtype=np.int32)
with open('inputs/day5') as f:
    for line in f:
        if len(line) > 1:
            coord = line.rstrip().split('->')
            coord_left = [int(c) for c in coord[0].split(',')]
            coord_right = [int(c) for c in coord[1].split(',')]

            y_step, y_extra = (1, 0) if coord_left[1] <= coord_right[1] else (-1, -2)
            x_step, x_extra = (1, 0) if coord_left[0] <= coord_right[0] else (-1, -2)
            if coord_left[1] == coord_right[1]:
                x_inds = np.array(range(coord_left[0], coord_right[0]+x_extra+1, x_step))
                lines[coord_left[1]*np.ones_like(x_inds), x_inds] += 1
                lines_b[coord_left[1]*np.ones_like(x_inds), x_inds] += 1
            elif coord_left[0] == coord_right[0]:
                y_inds = np.array(range(coord_left[1], coord_right[1]+y_extra+1, y_step))
                lines[y_inds, coord_left[0]*np.ones_like(y_inds)] += 1
                lines_b[y_inds, coord_left[0]*np.ones_like(y_inds)] += 1
            else:
                lines_b[np.array(range(coord_left[1], coord_right[1]+y_extra+1, y_step)),
                        np.array(range(coord_left[0], coord_right[0]+x_extra+1, x_step))] += 1


print(np.sum(lines > 1))
print(np.sum(lines_b > 1))
