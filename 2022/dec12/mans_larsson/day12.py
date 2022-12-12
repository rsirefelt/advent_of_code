import numpy as np

LARGE_NUMBER = 10000000


def get_neighbors(current_node, map_shape):
    neighbors = []
    if current_node[0] > 0:
        neighbors.append((current_node[0]-1, current_node[1]))
    if current_node[0] < map_shape[0] - 1:
        neighbors.append((current_node[0]+1, current_node[1]))
    if current_node[1] > 0:
        neighbors.append((current_node[0], current_node[1]-1))
    if current_node[1] < map_shape[1] - 1:
        neighbors.append((current_node[0], current_node[1]+1))
    return neighbors


def run_djikstra(start_pos, end_pos, height_map):
    distance_map = LARGE_NUMBER*np.ones_like(height_map)
    visited_map = np.zeros_like(height_map, dtype=bool)

    current_node = start_pos
    distance_map[current_node] = 0
    while not visited_map[end_pos]:
        for neighbor in get_neighbors(current_node, height_map.shape):
            if height_map[neighbor] - height_map[current_node] <= 1:
                if distance_map[neighbor] > distance_map[current_node] + 1:
                    distance_map[neighbor] = distance_map[current_node] + 1

        visited_map[current_node] = True
        if not np.any(np.logical_and(distance_map < LARGE_NUMBER, np.logical_not(visited_map))):
            return None
        current_node = np.unravel_index((distance_map + LARGE_NUMBER*visited_map).argmin(), visited_map.shape)

    return distance_map[end_pos]


with open('inputs/day12') as f:
    map_data = f.read().splitlines()

map_rows = []
for map_line in map_data:
    map_rows.append(np.array([ord(c) - ord('a') for c in map_line]))

height_map = np.stack(map_rows)
start_pos = tuple(np.argwhere(height_map == -14)[0])
height_map[start_pos] = 0
end_pos = tuple(np.argwhere(height_map == -28)[0])
height_map[end_pos] = 25

print(run_djikstra(start_pos, end_pos, height_map))

startpositions = np.argwhere(height_map == 0)
best_so_far = LARGE_NUMBER
for i, start_pos in enumerate(startpositions):
    this_dist = run_djikstra(tuple(start_pos), end_pos, height_map)

    if this_dist is not None and this_dist < best_so_far:
        best_so_far = this_dist
print(best_so_far)
