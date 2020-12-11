import numpy as np
from scipy.ndimage import correlate

seatmaps = []
with open('inputs/day11') as f:
    for line in f:
        row = line.rstrip()
        seatmap = np.array([c == 'L' for c in row])
        seatmaps.append(seatmap)

seatmap = np.array(seatmaps)
occupied_seats = np.zeros_like(seatmap, dtype=np.int)

neigbor_filter = np.ones((3, 3), dtype=np.int)
neigbor_filter[1, 1] = 0
while True:
    occupied_seats_before = occupied_seats.copy()
    occupied_neighbours = correlate(occupied_seats, neigbor_filter, mode='constant', cval=0)
    occupied_seats[occupied_neighbours >= 4] = 0
    occupied_seats[occupied_neighbours == 0] = 1
    occupied_seats = occupied_seats * seatmap
    if (occupied_seats == occupied_seats_before).all():
        break

print(f'a) {occupied_seats.sum()}')

seatmap = seatmap.astype(np.int)  # 0: no seat, 1: empty seat, 2: occupied seat
while True:
    seatmap_before = seatmap.copy()

    for x in range(seatmap.shape[0]):
        for y in range(seatmap.shape[1]):
            neighbor_count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue

                    x_seen = x + dx
                    y_seen = y + dy
                    while x_seen >= 0 and y_seen >= 0 and x_seen < seatmap.shape[0] and y_seen < seatmap.shape[1]:
                        if seatmap_before[x_seen, y_seen] == 2:
                            neighbor_count += 1
                            break
                        elif seatmap_before[x_seen, y_seen] == 1:
                            break

                        x_seen += dx
                        y_seen += dy

            if seatmap_before[x, y] == 2 and neighbor_count >= 5:
                seatmap[x, y] = 1
            if seatmap_before[x, y] == 1 and neighbor_count == 0:
                seatmap[x, y] = 2
    if(seatmap == seatmap_before).all():
        break

print(f'b) {(seatmap == 2).sum()}')
