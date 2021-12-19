import numpy as np
from utils import read_lines

def parseScannerInput(filename):
    lines = read_lines(filename)
    scanner_data = []
    for line in lines:
        if len(line) == 0:
            scanner_data.append(curr_scanner)
            continue
        if 'scanner' in line:
            curr_scanner = np.zeros((0,3), dtype=int)
            continue
        coords = np.array([[int(coord) for coord in line.split(',')]], dtype=int)
        curr_scanner = np.vstack((curr_scanner, coords))
    scanner_data.append(curr_scanner)
    return scanner_data

def generateAllPossibleRotations():
    rotations = []
    for x_dir in range(3):
        for x_sign in [-1, 1]:
            x_raw = np.zeros(3, dtype=int)
            x_raw[x_dir] = 1
            x_hat = x_raw * x_sign
            for y_dir in range(3):
                if y_dir == x_dir:
                    continue
                y_raw = np.zeros(3, dtype=int)
                y_raw[y_dir] = 1
                for y_sign in [-1, 1]:
                    y_hat = y_raw * y_sign
                    z_hat = np.cross(x_hat, y_hat)
                    R = np.zeros((3,3), dtype=int)
                    R[:,0] = x_hat
                    R[:,1] = y_hat
                    R[:,2] = z_hat
                    rotations.append(R) # TODO: WTF???
    return rotations

ALL_ROTATIONS = generateAllPossibleRotations()

def getRelativePoseFast(scanner1, scanner2):
    # Pick a beacon correspondence
    best_R = None
    best_t = None
    best_inliers = 0
    points1 = set()
    for point in scanner1:
        points1.add((point[0], point[1], point[2]))
    for k in range(scanner1.shape[0]):
        beacon1 = scanner1[k,:]
        for kk in range(scanner2.shape[0]):
            beacon2 = scanner2[kk, :]
            # For this correspondence, consider all possible rotations.
            for R in ALL_ROTATIONS:
                # Compute the transformation mapping from the coordinate system of beacon 2 into the system of beacon 1
                t = beacon1 - R @ beacon2
                transformed_points = R @ scanner2.transpose() + np.reshape(t, (3,1))
                transformed_points = transformed_points.transpose()
                points2 = set()
                for point in transformed_points:
                    points2.add((point[0], point[1], point[2]))

                # Compute the total number of scanners that agree with this transformation.
                num_inliers = len(points1.intersection(points2))
                if num_inliers > best_inliers:
                    if num_inliers >= 12:
                        return R, t, num_inliers
                    best_R = R
                    best_t = t
                    best_inliers = num_inliers

    return best_R, best_t, best_inliers

scanner_data = parseScannerInput("/home/carl/Code/AdventOfCode/Day19/input.txt")
#R, t, num_inliers = getRelativePose(scanner_data[0], scanner_data[1])

solved_scanners = set([0])
global_reconstruction = set()
for point in scanner_data[0]:
    global_reconstruction.add((point[0], point[1], point[2]))
# Add all scanners incrementally to the reconstruction

Rs = {0 : np.eye(3, dtype=int)}
ts = {0 : np.zeros(3, dtype=int)}
solved_any = True
while solved_any:
    solved_any = False
    for scanner in range(1, len(scanner_data)):
        if scanner in solved_scanners:
            continue
        # The current scanner has not been registered yet. Try to register it to the current reconstruction
        solved = False
        for reference_scanner in solved_scanners:
            R, t, num_inliers = getRelativePoseFast(scanner_data[reference_scanner], scanner_data[scanner])
            if num_inliers >= 12:
                solved = True
                solved_any = True
                print("Registered scanner", scanner, "to", reference_scanner, ". Number of inliers:", num_inliers, ". Number of scanners registered:", len(solved_scanners)+1, "/", len(scanner_data))
                for beacon in scanner_data[scanner]:
                    point = Rs[reference_scanner] @ (R @ beacon + t) + ts[reference_scanner]
                    global_reconstruction.add((point[0], point[1], point[2]))
                Rs[scanner] = Rs[reference_scanner] @ R
                ts[scanner] = Rs[reference_scanner] @ t + ts[reference_scanner]
                break
        if solved:
            solved_scanners.add(scanner)
            continue
print("Part 1:", len(global_reconstruction))

scanner_positions = set()
for k in range(len(scanner_data)):
    scanner_positions.add((ts[k][0], ts[k][1], ts[k][2]))
largest_manhattan_distance = 0
for point1 in scanner_positions:
    for point2 in scanner_positions:
        manhattan_distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2])
        if manhattan_distance > largest_manhattan_distance:
            largest_manhattan_distance = manhattan_distance

print("Part 2", largest_manhattan_distance)
