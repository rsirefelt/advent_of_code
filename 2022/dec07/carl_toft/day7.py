class Directory:
    def __init__(self, name=None):
        self.name = name
        self.parent_dir = None
        self.subdirs = []
        self.files = []
        self.dir_size = None

    def computeSize(self):
        if self.dir_size is not None:
            return self.dir_size
        else:
            self.dir_size = 0
            for file in self.files:
                self.dir_size = self.dir_size + file[0]
            for subdir in self.subdirs:
                self.dir_size = self.dir_size + subdir.computeSize()
        return self.dir_size

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]

    return lines[:-1]

def parseDirectories(lines):
    line_idx = 1

    curr_dir = Directory("/")
    top_dir = curr_dir
    all_dirs = [curr_dir]

    # Loop over commands
    while line_idx < len(lines):
        words = lines[line_idx].split(" ")
        command = words[1]
        line_idx = line_idx + 1

        if command == "ls":
            # Loop over ls output. For each file and directory, create it if it does not exist already
            while line_idx < len(lines) and lines[line_idx][0] != "$":
                contents = lines[line_idx].split(" ")
                if contents[0] == "dir":
                    # Check if the directory currently exists
                    subdir_names = [subdir.name for subdir in curr_dir.subdirs]
                    if contents[1] in subdir_names:
                        assert False, "Subdirectory already exists!"
                    else:
                        new_dir = Directory(contents[1])
                        new_dir.parent_dir = curr_dir
                        curr_dir.subdirs.append(new_dir)
                        all_dirs.append(new_dir)
                else:
                    # Current line contains a file
                    curr_dir.files.append((int(contents[0]), contents[1]))
                line_idx = line_idx + 1

        elif command == "cd":
            target_dir = words[2]
            if target_dir == "..":
                assert curr_dir.name != "/", "Cant cd .. out of top directory!"
                curr_dir = curr_dir.parent_dir
            else:
                for idx in range(len(curr_dir.subdirs)):
                    if curr_dir.subdirs[idx].name == target_dir:
                        curr_dir = curr_dir.subdirs[idx]
                        break

    return top_dir, all_dirs


top_dir, all_dirs = parseDirectories(parseInput("input.txt"))

# Part 1
total_small_size = 0
for curr_dir in all_dirs:
    curr_size = curr_dir.computeSize()
    if curr_size < 100000:
        print(curr_dir.name + " " + str(curr_size))
        total_small_size = total_small_size + curr_size
print("Part 1: " + str(total_small_size))

# Part 2
total_unused_space = 70000000 - top_dir.computeSize()
total_space_needed = 30000000 - total_unused_space
smallest_found = 1e10
for curr_dir in all_dirs:
    curr_size = curr_dir.computeSize()
    if curr_size > total_space_needed:
        if curr_size < smallest_found:
            smallest_found = curr_size
print("Part 2: " + str(smallest_found))
xxx = 3
