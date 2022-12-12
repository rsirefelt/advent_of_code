import numpy as np
from queue import PriorityQueue

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseHeightmap(lines):
    heightmap = np.ones((len(lines) + 2, len(lines[0]) + 2))*100
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "S":
                start = (row+1, col+1)
                heightmap[row+1, col+1] = 0
            elif lines[row][col] == "E":
                end = (row+1, col+1)
                heightmap[row+1, col+1] = ord('z') - 97
            else:
                heightmap[row+1, col+1] = ord(lines[row][col]) - 97
    return heightmap, start, end

def getNeighbours(pos, heightmap, visited):
    neighbours = []
    for delta_x in [-1, 1]:
        if (heightmap[pos[0], pos[1]+delta_x] <= heightmap[pos[0], pos[1]] + 1 and visited[pos[0], pos[1]+delta_x] == False):
            neighbours.append((pos[0], pos[1]+delta_x))
    for delta_y in [-1, 1]:
        if (heightmap[pos[0]+delta_y, pos[1]] <= heightmap[pos[0], pos[1]] + 1 and visited[pos[0]+delta_y, pos[1]] == False):
            neighbours.append((pos[0]+delta_y, pos[1]))
    return neighbours

def Djikstra(heightmap, start):
    next_nodes = PriorityQueue()

    distance_map = np.ones_like(heightmap)*(-1)
    distance_map[start[0], start[1]] = 0
    visited = np.zeros_like(heightmap, dtype=np.bool)
    visited[start[0], start[1]] = True

    neighbours = getNeighbours(start, heightmap, visited)
    for neighbour in neighbours:
        next_nodes.put((1, neighbour))

    while not next_nodes.empty():
        distance, next_node = next_nodes.get()
        #if visited[next_node[0], next_node[1]] == True:
        #    xxx = 3
        #if next_node[0] == 20 and next_node[1] == 2:
        #    xxx = 3
        distance_map[next_node[0], next_node[1]] = distance
        visited[next_node[0], next_node[1]] = True
        neighbours = getNeighbours(next_node, heightmap, visited)
        for neighbour in neighbours:
            visited[neighbour[0], neighbour[1]] = True
            next_nodes.put((distance + 1, neighbour))

    return distance_map

heightmap, start, end = parseHeightmap(parseInput("input.txt"))

# Part 1
distance_map = Djikstra(heightmap, start)
print("Part 1: " + str(distance_map[end[0], end[1]]))

# Part 2
possible_paths = []
for row in range(1, heightmap.shape[0]-1):
    for col in range(1, heightmap.shape[1]-1):
        if heightmap[row, col] == 0:
            distance = Djikstra(heightmap, (row, col))[end[0], end[1]]
            possible_paths.append(distance)
shortest_path = np.min(np.array(possible_paths))
print("Part 2: " + str(shortest_path))
