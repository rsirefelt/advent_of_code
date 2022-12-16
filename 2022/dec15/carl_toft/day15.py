import numpy as np

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseData(lines):
    sensors = []
    beacons = []
    for line in lines:
        parts = line.split(": ")
        parts1 = parts[0].split("=")
        sensor = [int(parts1[1].split(", ")[0]), int(parts1[2])]

        parts2 = parts[1].split("=")
        beacon = (int(parts2[1].split(", ")[0]), int(parts2[2]))

        sensors.append(sensor)
        beacons.append(beacon)

    return sensors, beacons

sensors, beacons = parseData(parseInput("input.txt"))
sensors = np.array(sensors)
beacons = np.array(beacons)
distances = np.sum(np.abs(sensors - beacons), axis=1)

y = 2000000
tmp = distances - np.abs(sensors[:,1] - y)
intersecting_beacons = np.where(tmp > 0)[0]
start_points = sensors[intersecting_beacons,0] - tmp[intersecting_beacons]
end_points = sensors[intersecting_beacons,0] + tmp[intersecting_beacons]

row = np.zeros(10000000, dtype=bool)
offset = 1000000

for idx in range(start_points.size):
    row[start_points[idx] + offset:end_points[idx] + offset + 1] = True

num_positions = np.sum(row)

beacons_found = set()
for idx in range(len(beacons)):
    if beacons[idx][1] == y:
        beacons_found.add((beacons[idx, 0], beacons[idx,1]))

num_positions = num_positions - len(beacons_found)

print("Part 1: " + str(num_positions))

# Part 2
for idx in range(len(sensors)):
    print(str(idx+1) + "/" + str(len(sensors)))
    for x in range(sensors[idx, 0] - distances[idx] - 1, sensors[idx, 0] + distances[idx]+2):
        delta = distances[idx] + 1 - abs(sensors[idx,0] - x)
        for y in [sensors[idx,1] + delta, sensors[idx,1] - delta]:
            if x < 0 or x > 4000000:
                continue
            if y < 0 or y > 4000000:
                continue

            pos = np.array([[x, y]])

            if not np.any(np.sum(np.abs(pos - sensors), axis=1) <= distances):
                print("Found it! " + str(x) + " " + str(y))
                break
