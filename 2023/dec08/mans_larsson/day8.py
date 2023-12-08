import numpy as np


def get_periodicity(start_node, nodes):
    current_node = nodes[start_node][steps[0]]
    step = 1
    z_steps = []
    while current_node != start_node and step < 1e6:
        current_node = nodes[current_node][steps[step % len(steps)]]
        step += 1
        if current_node.endswith('Z'):
            z_steps.append(step)
    diffs = np.diff(z_steps)

    assert len(set(diffs)) == 1
    return diffs[0]


nodes = {}
with open('inputs/day8') as f:
    lines = f.readlines()

    steps = lines[0].rstrip()

    for line in lines[2:]:
        data = line.rstrip().split()
        nodes[data[0]] = {'L': data[2][1:-1], 'R': data[3][:-1]}

current_node = 'AAA'
step = 0
while current_node != 'ZZZ':
    current_node = nodes[current_node][steps[step % len(steps)]]
    step += 1

print(step)

start_nodes = [node for node in nodes if node.endswith('A')]

periods = []
for node in start_nodes:
    periods.append(get_periodicity(node, nodes))

lcm = np.lcm(periods[0], periods[1])
for period in periods[2:]:
    lcm = np.lcm(lcm, period)

print(lcm)
