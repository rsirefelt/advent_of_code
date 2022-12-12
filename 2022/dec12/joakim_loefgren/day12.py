from string import ascii_lowercase

import numpy as np


class Navigator:
    def __init__(self, heights):
        self.heights = heights

    def get_neighbors(self, node):
        neighbors = []
        i, j = node
        if i > 0:
            neighbors.append([i - 1, j])
        if i < self.heights.shape[0] - 1:
            neighbors.append([i + 1, j])
        if j > 0:
            neighbors.append([i, j - 1])
        if j < self.heights.shape[1] - 1:
            neighbors.append([i, j + 1])
        return neighbors

    def _get_min_node(self, paths, visited):
        inds = np.where(~visited)
        imin = np.argmin(paths[~visited])
        node = (inds[0][imin], inds[1][imin])
        return node

    def find_shortest(self, start):
        """Dijkstra"""
        heights = self.heights
        paths = np.ones_like(heights, dtype=np.int64) * heights.size * 100
        visited = np.zeros_like(heights, dtype=bool)
        paths[start[0], start[1]] = 0
        while not np.all(visited):
            node = self._get_min_node(paths, visited)
            visited[node[0], node[1]] = True
            neighbors = self.get_neighbors(node)
            for nb in neighbors:
                if (
                    heights[nb[0], nb[1]] <= heights[node[0], node[1]] + 1
                    and not visited[nb[0], nb[1]]
                ):
                    new_len = paths[node[0], node[1]] + 1
                    if paths[nb[0], nb[1]] > new_len:
                        paths[nb[0], nb[1]] = new_len
        return paths


if __name__ == "__main__":
    char_to_height = {c: i for i, c in enumerate(ascii_lowercase)}
    char_to_height["E"] = char_to_height["z"]
    char_to_height["S"] = char_to_height["a"]
    heights_char = np.loadtxt("./input.txt", dtype=str)
    heights_char = np.array([list(row) for row in heights_char])
    end = [inds.item() for inds in np.where(heights_char == "E")]
    start = [inds.item() for inds in np.where(heights_char == "S")]
    heights = np.array([[char_to_height[c] for c in row] for row in heights_char])

    # Part I
    nav = Navigator(heights)
    paths = nav.find_shortest(start)
    print(paths[end[0], end[1]])

    # Part II
    nav.heights = -nav.heights
    paths = nav.find_shortest(end)
    print(np.min(paths[nav.heights == 0]))
