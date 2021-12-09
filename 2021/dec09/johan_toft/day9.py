import numpy as np

with open("input.txt") as f:
    arr = []
    for line in f.read().splitlines():
        arr.append([int(c) for c in line])

nparr = np.array(arr)


def explore_basin(x, y, arr):
    lim_y = len(arr)
    lim_x = len(arr[0])

    def valid_point(x, y):
        return (0 <= x < lim_x) and (0 <= y < lim_y)

    basin_size = 1
    arr[y][x] = 9
    queue = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    queue = [(p[0], p[1]) for p in queue if valid_point(p[0], p[1])]

    while len(queue) > 0:
        x, y = queue.pop()
        if arr[y][x] < 9:
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            neighbors = [(p[0], p[1]) for p in neighbors if valid_point(p[0], p[1])]
            neighbors = [(p[0], p[1]) for p in neighbors if arr[y][x] < 9]
            queue.extend(neighbors)
            arr[y][x] = 9
            basin_size += 1
    return basin_size


def check_is_low(x, y, arr):
    lim_y = len(arr)
    lim_x = len(arr[0])

    candidate_points = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for xc, yc in candidate_points:
        if (0 <= xc < lim_x) and (0 <= yc < lim_y):
            if arr[yc][xc] <= arr[y][x]:
                return False
    return True


sum = 0

basin_sizes = []

for y in range(0, len(arr)):
    for x in range(0, len(arr[0])):
        if (check_is_low(x, y, arr)):
            print(x, y, arr[y][x])
            sum += arr[y][x] + 1
            # Explore basin
            basin_sizes.append(explore_basin(x, y, arr))

print(sum)

largest = (sorted(basin_sizes, reverse=True)[0:3])
test = 1
for num in largest:
    test *= num
print(test)
