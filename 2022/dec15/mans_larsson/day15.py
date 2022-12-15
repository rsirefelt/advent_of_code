import re

with open('inputs/day15') as f:
    lines = f.read().splitlines()


def check_blocked(pos, beacon_positions, sensor_positions):
    if pos in beacon_positions:
        return False, 1
    if pos in sensor_positions:
        return True, 1

    for sensor_pos, smallest_dist in zip(sensor_positions, distances):
        this_dist = abs(pos[0] - sensor_pos[0]) + abs(pos[1] - sensor_pos[1])
        if this_dist <= smallest_dist:
            return True, smallest_dist - this_dist + 1
    return False, 1


def look_for_free(beacon_positions, sensor_positions):
    for ypos in range(4000000):
        xpos = 0
        while xpos < 4000000:
            pos = (xpos, ypos)
            is_blocked, max_safe_step = check_blocked(pos, beacon_positions, sensor_positions)
            if not is_blocked:
                return xpos*4000000+ypos
            xpos += max_safe_step
    return -1


if __name__ == '__main__':
    beacon_positions = []
    sensor_positions = []
    distances = []
    for line in lines:
        match = re.match(r'Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)', line)
        sensor_positions.append((int(match.groups()[0]), int(match.groups()[1])))
        beacon_positions.append((int(match.groups()[2]), int(match.groups()[3])))
        distances.append(abs(sensor_positions[-1][0] - beacon_positions[-1][0]) +
                         abs(sensor_positions[-1][1] - beacon_positions[-1][1]))

    xmin = min(min([sp[0] for sp in sensor_positions]), min([bp[0] for bp in beacon_positions])) - max(distances)
    xmax = max(max([sp[0] for sp in sensor_positions]), max([bp[0] for bp in beacon_positions])) + max(distances)

    not_blocked_count = 0
    ypos = 2000000
    xpos = xmin
    while xpos <= xmax:
        pos = (xpos, ypos)
        is_blocked, max_safe_step = check_blocked(pos, beacon_positions, sensor_positions)
        if not is_blocked:
            not_blocked_count += 1
        xpos += max_safe_step

    print(xmax - xmin - not_blocked_count)
    print(look_for_free(beacon_positions, sensor_positions))
