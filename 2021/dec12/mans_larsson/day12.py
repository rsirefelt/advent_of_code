
connectivity = dict()
with open('inputs/day12') as f:
    for line in f:
        startstop = line.rstrip().split('-')
        first_entry = connectivity.get(startstop[0], [])
        second_entry = connectivity.get(startstop[1], [])
        first_entry.append(startstop[1])
        second_entry.append(startstop[0])
        connectivity[startstop[0]] = first_entry
        connectivity[startstop[1]] = second_entry


def valid_next_step_a(path, node):
    if node == 'start':
        return False
    if node.lower() == node and node in path:  # small node
        return False
    return True


def valid_next_step_b(path, node):
    if node == 'start':
        return False
    if node.lower() == node:  # small node
        if node not in path:
            return True
        for visited_node in set(path):
            if visited_node.lower() == visited_node:
                if len([n for n in path if n == visited_node]) > 1:
                    return False
    return True


def step(paths, validity_checker):
    new_paths = []
    any_change = False
    for path in paths:
        if path[-1] == 'end':
            new_paths.append(path)
            continue
        neighbors = connectivity[path[-1]]
        for neighbor_node in neighbors:
            if validity_checker(path, neighbor_node):
                new_path = path.copy()
                new_path.append(neighbor_node)
                new_paths.append(new_path)
                any_change = True
    return new_paths, any_change


paths = [['start']]
while True:
    paths, any_change = step(paths, valid_next_step_a)
    if not any_change:
        break

print(len(paths))

paths = [['start']]
while True:
    paths, any_change = step(paths, valid_next_step_b)
    if not any_change:
        break

print(len(paths))
