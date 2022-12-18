import re
import itertools

import networkx as nx


def calc_release(graph, path, lengths, t_max=26):
    t = 0
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

if __name__ == '__main__':

    graph = nx.Graph()
    edges = []
    with open("./input.txt") as f:
        for line in f:
            matches = re.findall(r"([A-Z]{2}|\d+)", line)
            graph.add_node(matches[0], flow=int(matches[1]))
            edges.extend([(matches[0], e) for e in matches[2:]])

    graph.add_edges_from(edges)


    lengths = dict(nx.all_pairs_shortest_path_length(graph))


    path1 = ['AA']
    path2 = ['AA']
    high_flow_nodes = sorted(
        [n for n in graph if graph.nodes[n]["flow"] > 0],
        key=lambda x: graph.nodes[x]["flow"],
        reverse=True,
    )
    candidates = high_flow_nodes
    
    max_release = 0
    max_paths = None
    i = 0
    for cands1 in itertools.combinations(candidates, len(candidates)//2):
        i += 1
        print(f'Iteration: {i} / 6435', end='\r', flush=True)
        paths = [None, None] 
        cands1 = list(cands1)
        cands2 = list(set(candidates) - set(cands1))

        release1 = 0
        for per1 in itertools.permutations(cands1):
            path1_tmp = path1 + list(per1)
            rel = calc_release(graph, path1_tmp , lengths)
            if rel > release1:
                release1 = rel
                paths[0] = path1_tmp

        release2 = 0
        for per2 in itertools.permutations(cands2):
            path2_tmp = path2 + list(per2)
            rel = calc_release(graph, path2_tmp , lengths)
            if rel > release2:
                release2 = rel
                paths[1] = path2_tmp
                
        release = release1 + release2
        if release > max_release:
            max_release = release
            max_paths = paths

    print(max_release)
    print(max_paths)
