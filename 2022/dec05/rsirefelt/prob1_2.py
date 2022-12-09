from collections import deque
import re

def create_dequeu_list(path):
    dequeu_list = []
    with open(path) as f:
        for i, line in enumerate(f):
            if line[1] == "1":
                return dequeu_list, i + 1

            if i == 0:
                for j in range(1, len(line), 4):
                    if line[j] == " ":
                        dequeu_list.append(deque())
                    else:
                        dequeu_list.append(deque(line[j]))
            else:
                for k, j in enumerate(range(1, len(line), 4)):
                    if line[j] != " ":
                        dequeu_list[k].appendleft(line[j])

def move_crates(path, line_idx, dequeu_list, mode):
    with open(path) as f:
        for i, line in enumerate(f):
            if i <= line_idx:
                continue
            
            [num, start, dest] = [int(x) - 1 for x in re.findall("[0-9]+", line)]
            
            if mode == 1:
                for j in range(num + 1):
                    crate = dequeu_list[start].pop()
                    dequeu_list[dest].append(crate)
            else:
                crates = deque()
                for j in range(num + 1):
                    crates.appendleft(dequeu_list[start].pop())
                dequeu_list[dest] += crates
    
    return dequeu_list

input_path = "input"
dequeu_list, line_idx = create_dequeu_list(input_path)
final_dequeu_list = move_crates(input_path, line_idx, dequeu_list, 2)

for crate_dequeu in final_dequeu_list:
    print(crate_dequeu[-1], end="")
print()
