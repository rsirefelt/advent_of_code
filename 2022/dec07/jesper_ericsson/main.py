import os
import numpy as np

def get_folder(file_system, path):
    tmp_folder = file_system
    for folder in path:
        tmp_folder = tmp_folder[folder]
    
    return tmp_folder

def read_data(filename):
    file_system = {"/":{}}
    current_folder_path = []
    current_folder = {}
    with open(filename, "r") as f:
        line = f.readline().rstrip()
        while line != "":
            # Move folder
            if line[0:4] == "$ cd":
                if line[5:] == "..":
                    current_folder_path.pop()
                else:
                    current_folder_path.append(line[5:])
                line = f.readline().rstrip()
            # List members(Create file and dicts) 
            elif line[0:4] == "$ ls":
                current_folder = get_folder(file_system, current_folder_path)

                while True:
                    line = f.readline().rstrip()
                    if line == "" or line[0] == "$":
                        break
                    elif line[0:3] == "dir":
                        current_folder[line[4:]] = {}
                    else:
                        size, name = line.split(" ")
                        current_folder[name] = int(size)
         

    return file_system


def find_folder_sizes(path, folder_list):

    if type(path) is int:
        return path
    else:
        sum_tot_size = 0

        for file in path.values():
            tot_size = find_folder_sizes(file, folder_list)
            sum_tot_size += tot_size

        folder_list.append(sum_tot_size)
        return sum_tot_size

def prob1(file_system):
    folder_list = []
    _ = find_folder_sizes(file_system, folder_list)
    folder_sizes = np.array(folder_list)

    print(f"Sum folder sizes: {np.sum(folder_sizes[folder_sizes < 100000])}")


def prob2(file_system):

    folder_list = []
    tot_size = find_folder_sizes(file_system, folder_list)
    tot_disk_space = 70000000
    needed_space = tot_size + 30000000 - tot_disk_space

    folder_sizes = np.array(folder_list)
    sorted_sizes = np.sort(folder_sizes)

    value_ind = np.argmax(sorted_sizes-needed_space > 0)

    print(f"Folder to delete: {sorted_sizes[value_ind]}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"
    file_system = read_data(filename)

    prob1(file_system)
    prob2(file_system)


if __name__ == "__main__":
    main()
