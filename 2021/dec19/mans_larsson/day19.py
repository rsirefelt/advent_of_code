import numpy as np
from scipy.spatial.distance import cdist

directions = np.array([[1, 0, 0], [-1, 0, 0],
                       [0, 1, 0], [0, -1, 0],
                       [0, 0, 1], [0, 0, -1]])


def try_to_locate(scanned_points, current_beacons):
    # try to find location
    def inner():
        for x_axis in directions:
            for y_axis in directions:
                if np.all(np.abs(x_axis) == np.abs(y_axis)):  # same axis
                    continue
                z_axis = np.cross(x_axis, y_axis)
                transformation_matrix = np.stack([x_axis, y_axis, z_axis], axis=1)
                transformed_points = np.transpose(transformation_matrix @ np.transpose(scanned_points))

                for beacon in current_beacons:
                    for point in transformed_points:
                        position = beacon - point
                        # check how many points align if this would be the position of scanner
                        absolute_point_positions = transformed_points + position
                        dists = cdist(absolute_point_positions, current_beacons)
                        min_dists = np.min(dists, axis=1)

                        if sum(min_dists == 0) >= 12:
                            points_to_add = absolute_point_positions[min_dists > 0, :]  # add points not overlapping
                            return points_to_add, position
        return None, None

    points_to_add, scanner_pos = inner()

    # if succesful, add all beacons
    if points_to_add is not None:
        current_beacons = np.concatenate((current_beacons, points_to_add))

    return current_beacons, scanner_pos


scans = {}
scan_i = -1
with open('inputs/day19') as f:
    for line in f:
        if line.startswith('--'):
            if scan_i != -1:
                scans[scan_i] = np.stack(these_scans)
            scan_i += 1
            these_scans = []
        elif len(line) > 1:
            these_scans.append(np.array([int(n) for n in line.rstrip().split(',')]))
scans[scan_i] = np.stack(these_scans)

current_beacons = scans[0]
del scans[0]

scanner_positions = [np.array([0, 0, 0])]
while len(scans) > 0:
    for scan_i, scanned_points in scans.items():
        updated_beacons, scanner_pos = try_to_locate(scanned_points, current_beacons)
        if current_beacons.shape[0] != updated_beacons.shape[0]:
            print(f'adding scanner {scan_i}')
            scanner_positions.append(scanner_pos)
            del scans[scan_i]
            break
    current_beacons = updated_beacons

print(current_beacons.shape[0])

largest_dist = 0
for a in scanner_positions:
    for b in scanner_positions:
        dist = np.sum(np.abs(a - b))
        if dist > largest_dist:
            largest_dist = dist
print(largest_dist)
