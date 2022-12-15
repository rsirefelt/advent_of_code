import re
import numpy as np


def manhattan(p1, p2):
    return np.abs(p1 - p2).sum(-1)


def scan_y(sensors, dists, y):
    intervals = []
    for i , sen in enumerate(sensors):
        diff = dists[i] - abs(sen[1] - y)
        if diff >= 0:
            intervals.append([sen[0] - diff, sen[0] + diff])
            
    # assemble disjoint intervals
    intervals.sort(key=lambda x: (x[0], x[1]))
    intervals_dis = [intervals[0]]
    for new in intervals[1:]:
        curr = intervals_dis[-1]
        if new[0] - 1 <= curr[1]:
            intervals_dis[-1] = [curr[0], max(curr[1], new[1])]
        else:
            intervals_dis.append(new)
    return intervals_dis
   

if __name__ == '__main__':
    sensors = []
    beacons = []
    with open('./input.txt') as f:
        for line in f:
            xs, ys, xb, yb = re.findall(r'-?\d+', line)
            sensors.append([xs, ys])
            beacons.append([xb, yb])

    sensors = np.array(sensors, dtype=np.int64)
    beacons = np.array(beacons, dtype=np.int64)
    dists = manhattan(sensors, beacons)

    # part I
    # determine the interval on the y=y_scan line excluded by each sensor
    y = 2000000
    intervals_dis = scan_y(sensors, dists, y)
        
    # we only get single interval back so no need to loop
    inter = intervals_dis[0]
    num_pos = inter[1] - inter[0] + 1  # number of excluded positions in line y_scan
    # subtract any sensors and/or beacons on line y_scan
    num_sens = len(np.unique(
        sensors[(sensors[:, 1] == y) &
                (sensors[:, 0] >= inter[0]) &
                (sensors[:, 0] <= inter[1])], axis=0
    ))
    num_beac = len(np.unique(
        beacons[(beacons[:, 1] == y)
                & (beacons[:, 0] >= inter[0])
                & (beacons[:, 0] <= inter[1])], axis=0
    ))
    num_pos -= num_sens + num_beac
    print(num_pos)

    # part II
    for y in range(0, 4000000):
        inters = scan_y(sensors, dists, y)
        if len(inters) == 2:
            x = inters[1][0] - 1
            break
        elif inters[0][0] > 0:
            x = inters[0][0]
            break

    print(x, y) 
    print(x*4000000 + y)
