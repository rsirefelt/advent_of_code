import numpy as np

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dijkstra(cost_map):
    distance_map = 100000*np.ones_like(cost_map)
    visited = np.zeros_like(cost_map, bool)
    distance_map[0, 0] = 0

    current = (0, 0)
    visited[current] = True
    while np.any(~visited):
        # update distance to neighbors
        for delta in deltas:
            neighbor = (current[0] + delta[0], current[1] + delta[1])

            if neighbor[0] >= 0 and neighbor[0] < cost_map.shape[0] and \
               neighbor[1] >= 0 and neighbor[1] < cost_map.shape[1] and \
               not visited[neighbor]:

                this_distance = distance_map[current] + cost_map[neighbor]
                if this_distance < distance_map[neighbor]:
                    distance_map[neighbor] = this_distance

        # choose next node as closest unvisited
        current = np.unravel_index(np.argmin(100000*visited + distance_map), distance_map.shape)
        visited[current] = True
    return distance_map[-1, -1]


rows = []
with open('inputs/day15') as f:
    for line in f:
        rows.append(np.array([int(c) for c in line.rstrip()]))

cost_map = np.stack(rows)

print(dijkstra(cost_map))

cost_b = np.zeros((5*cost_map.shape[0], 5*cost_map.shape[1]), dtype=np.int32)
for i in range(5):
    for j in range(5):
        this_cost = np.mod(cost_map + i + j - 1, 9) + 1
        cost_b[i*cost_map.shape[0]:(i+1)*cost_map.shape[0], j*cost_map.shape[1]:(j+1)*cost_map.shape[1]] = this_cost

print(dijkstra(cost_b))
