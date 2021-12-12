import numpy as np
from utils import read_lines

def parseInput(filename):
    connectivity = {}
    lines = read_lines(filename)
    for line in lines:
        cave1, cave2 = line.split('-')
        if cave1 in connectivity:
            connectivity[cave1].add(cave2)
        else:
            connectivity[cave1] = set([cave2])
        if cave2 in connectivity:
            connectivity[cave2].add(cave1)
        else:
            connectivity[cave2] = set([cave1])
    return connectivity

connectivity = parseInput("/home/carl/Code/AdventOfCode/Day12/input.txt")
caves = list(connectivity.keys())
names_to_index = {cave : idx for idx, cave in enumerate(caves)}
visit_only_once = [cave[0].islower() for cave in caves]


num_visited = np.zeros(len(caves), dtype=int)
num_visited[names_to_index['start']] = 1

def findAllPathsPart1(start_node, visited_count):
    if start_node == 'end':
        return [['end']]

    paths = []
    for next_node in connectivity[start_node]:
        node_idx = names_to_index[next_node]
        if visit_only_once[node_idx] is True and visited_count[node_idx] > 0:
            continue # we can't visit this node again

        # Next node is legal to visit. Visit it
        new_visited_count = np.copy(visited_count)
        new_visited_count[node_idx] += 1
        new_paths = findAllPathsPart1(next_node, new_visited_count)
        for path in new_paths:
            path.append(start_node)
        paths = paths + new_paths

    return paths

def findAllPathsPart2(start_node, visited_count, visited_cave_twice):
    if start_node == 'end':
        return [['end']]

    paths = []
    for next_node in connectivity[start_node]:
        node_idx = names_to_index[next_node]
        if visit_only_once[node_idx] is True and visited_count[node_idx] > 0 and visited_cave_twice == True:
            continue # we can't visit this node again
        # Don't visit start or end nodes twice
        if next_node == 'start':
            continue

        # Next node is legal to visit. Visit it
        new_visited_count = np.copy(visited_count)
        new_visited_count[node_idx] += 1
        is_this_the_second_visit = new_visited_count[node_idx] > 1
        second_visit_used_up = is_this_the_second_visit and visit_only_once[node_idx]
        second_visit_used_up = visited_cave_twice or second_visit_used_up
        #second_visit_used_up = second_visit_used_up and visit_only_once[node_idx]
        new_paths = findAllPathsPart2(next_node, new_visited_count, second_visit_used_up)
        for path in new_paths:
            path.append(start_node)
        paths = paths + new_paths

    return paths

paths = findAllPathsPart1('start', num_visited)
print("Part 1:", len(paths))
paths = findAllPathsPart2('start', num_visited, False)
print("Part 2:", len(paths))