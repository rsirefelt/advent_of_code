import re
from collections import deque
import itertools
import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

graph = nx.Graph()

edges = []
with open("./test.txt") as f:
    for line in f:
        matches = re.findall(r"([A-Z]{2}|\d+)", line)
        graph.add_node(matches[0], flow=int(matches[1]))
        edges.extend([(matches[0], e) for e in matches[2:]])

graph.add_edges_from(edges)


def calc_release(graph, path, lengths):
    t = 0
    t_max = 30
    release = 0
    flow_rate = 0
    for i in range(1, len(path)):
        dt = lengths[path[i-1]][path[i]]
        if t + dt <= t_max:
            release += flow_rate * dt
            t += dt
        else:
            break
        if t + 1 <= t_max:
            release += flow_rate
            flow_rate += graph.nodes[path[i]]['flow']
            t += 1
        else:
            break
        
    if t_max - t > 0:
        dt = t_max - t
        release += flow_rate * dt
        
    return release


high_flow_nodes = sorted(
    [n for n in graph if graph.nodes[n]["flow"] > 0],
    key=lambda x: graph.nodes[x]["flow"],
    reverse=True,
)

lengths = dict(nx.all_pairs_shortest_path_length(graph))

path = ['AA']
while len(high_flow_nodes) > 0:
    scores = []
    new = []
    candidates = high_flow_nodes
    for tmp in itertools.permutations(candidates, min(6, len(high_flow_nodes))):
        scores.append(calc_release(graph, path + list(tmp), lengths))
        new.append(tmp)
    imax = np.argmax(scores)
    path.append(new[imax][0])
    high_flow_nodes.pop(high_flow_nodes.index(path[-1]))

print(path, calc_release(graph, path, lengths))
