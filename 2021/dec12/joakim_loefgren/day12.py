import numpy as np
from dataclasses import dataclass


def parse_input(file_path="./input_day12.txt"):
    with open(file_path, "r") as f:
        connections_raw = []
        for line in f:
            connections_raw.append(line.strip().split("-"))
    return np.array(connections_raw)


@dataclass
class Explorer:
    path: list
    visit_count: dict


class CaveSystem:
    def __init__(self, connections_raw):
        labels = list(np.unique(connections_raw))
        labels.pop(labels.index("start"))
        labels.pop(labels.index("end"))
        self.labels = np.array(["start"] + sorted(labels) + ["end"])
        self.small = np.array([c.islower() for c in self.labels])
        self.small[0] = False
        self.small[-1] = False
        self.num_nodes = len(self.labels)
        self.indices = np.arange(self.num_nodes)
        self.label_to_index = {l: i for l, i in zip(self.labels, self.indices)}
        self.paths = None
        self.explorers = None

        # build  adjacency matrix
        row = [self.label_to_index[v] for v in connections_raw[:, 0]]
        col = [self.label_to_index[v] for v in connections_raw[:, 1]]
        data = np.ones(len(row), dtype=int).astype(bool)
        self.graph = np.zeros((self.num_nodes,) * 2, dtype=bool)
        self.graph[row, col] = data
        self.graph += self.graph.T
        self.graph[:, 0] = False
        self.graph[-1, :] = False

    def condition1(self, explorer, node):
        return explorer.visit_count[node] == 0

    def condition2(self, explorer, node):
        return explorer.visit_count[node] == 0 or (
            explorer.visit_count[node] == 1
            and 2 not in explorer.visit_count.values()
        )

    def explore(self, part=1):
        visit_count = {n: 0 for n in self.indices if self.small[n]}
        self.explorers = [Explorer([0], visit_count)]
        self.paths = []

        if part == 1:
            condition = self.condition1
        else:
            condition = self.condition2

        while len(self.explorers) > 0:
            explorers_new = []
            for expl in self.explorers:
                neighbors = self.indices[self.graph[expl.path[-1], :]]
                for node in neighbors:
                    if node == self.indices[-1]:
                        self.paths.append(self.labels[expl.path + [node]])
                    elif self.small[node]:
                        if condition(expl, node):
                            visit_count = expl.visit_count.copy()
                            visit_count[node] += 1
                            expl_new = Explorer(expl.path + [node], visit_count)
                            explorers_new.append(expl_new)
                    else:
                        expl_new = Explorer(expl.path + [node], expl.visit_count)
                        explorers_new.append(expl_new)
            self.explorers = explorers_new


if __name__ == "__main__":
    connections_raw = parse_input("./input_day12.txt")
    cs = CaveSystem(connections_raw)

    # Part I
    cs.explore(part=1)
    print(len(cs.paths))

    # Part 2
    cs.explore(part=2)
    print(len(cs.paths))
