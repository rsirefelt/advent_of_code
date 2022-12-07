from dataclasses import dataclass
import numpy as np
import operator


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    @property
    def size(self):
        return sum([child.size for child in self.children])


@dataclass
class File:
    name: str
    size: int


def filter_size(dir, op, size):
    """Filter files based on size using function op"""
    matches = []
    if isinstance(dir, Dir):
        if op(dir.size, size):
            matches.append(dir)
        for child in dir.children:
            matches.extend(filter_size(child, op, size))
    return matches


class FileSystem:
    def __init__(self):
        self.root = Dir("/")
        self.cwd = self.root

    def cd(self, name):
        if name == "..":
            self.cwd = self.cwd.parent
        else:
            for child in self.cwd.children:
                if child.name == name:
                    self.cwd = child
                    break

    def mkdir(self, name):
        if name not in [c.name for c in self.cwd.children]:
            self.cwd.children.append(Dir(name, parent=self.cwd))

    def mkfile(self, name, size):
        if name not in [c.name for c in self.cwd.children]:
            self.cwd.children.append(File(name, size))


def deduce_filesystem(output_file):
    with open(output_file) as f:
        lines = f.read().splitlines()

    fs = FileSystem()
    for line in lines[1:]:
        lsplit = line.split()
        if lsplit[0] == "$":
            if lsplit[1] == "cd":
                name = lsplit[2]
                if name != "..":
                    fs.mkdir(name)
                fs.cd(name)
            else:  # ls
                continue
        else:
            name = lsplit[1]
            if lsplit[0] == "dir":
                fs.mkdir(name)
            else:
                size = int(lsplit[0])
                fs.mkfile(name, size)
    return fs


if __name__ == "__main__":

    # Part I
    fs = deduce_filesystem("input.txt")
    matches = filter_size(fs.root, operator.le, size=100000)
    print(sum([m.size for m in matches]))

    # Part II
    space_unused = 70000000 - fs.root.size
    space_to_free = 30000000 - space_unused
    matches = filter_size(fs.root, operator.ge, size=space_to_free)
    sizes = [m.size for m in matches]
    imin = np.argmin(sizes)
    print(matches[imin].size)
