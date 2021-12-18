with open('real_input.txt', 'r') as f:
    input = f.read().splitlines()
    data = (list(map(lambda x: [int(y) for y in list(x)], input)))

    # Create a repeated 5x5 grid of the input data
    grid = [[0]*len(data[0]*5) for i in range(len(data)*5)]
    for i in range(5):
        for j in range(5):
            for k in range(len(data)):
                for l in range(len(data[0])):
                    newdata = data[k][l] + i + j
                    newdata = newdata if newdata < 10 else newdata - 9
                    grid[i*len(data)+k][j*len(data[0])+l] = newdata


# Part 1

# Find the shortest path from the start to the end
def find_path(data):
    start = (0, 0)
    end = (len(data) - 1, len(data[0]) - 1)

    explored = {}

    # Create a priority queue
    # The priority queue is a list of tuples (distance, (x,y))
    # The distance is the distance from the start to the current position


    from queue import PriorityQueue

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        # Get the next position
        distance, pos = pq.get()

        # Check if we have reached the end
        if pos == end:
            return distance
            break

        # Check if we have already explored this position
        if pos in explored:
            continue

        # Mark the position as explored
        explored[pos] = distance

        # Add the neighbours to the priority queue
        for neighbour in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
            if neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= len(data) or neighbour[1] >= len(data[0]):
                continue
            if data[neighbour[0]][neighbour[1]] == 0:
                continue
            # Distance to neighbour is the value in data + the distance to the current position
            pq.put((data[neighbour[0]][neighbour[1]] + distance, neighbour))

print(find_path(grid))