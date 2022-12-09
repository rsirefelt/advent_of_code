from collections import deque
import re

def create_deque_list(path):
    deque_list = []
    with open(path) as f:
        for i, line in enumerate(f):
            if line[1] == "1":
                return deque_list, i + 1

            if i == 0:
                for j in range(1, len(line), 4):
                    if line[j] == " ":
                        deque_list.append(deque())
                    else:
                        deque_list.append(deque(line[j]))
            else:
                for k, j in enumerate(range(1, len(line), 4)):
                    if line[j] != " ":
                        deque_list[k].appendleft(line[j])

def move_crates(path, line_idx, deque_list, mode):
    with open(path) as f:
        for i, line in enumerate(f):
            if i <= line_idx:
                continue
            
            [num, start, dest] = [int(x) - 1 for x in re.findall("[0-9]+", line)]
            
            if mode == 1:
                for j in range(num + 1):
                    crate = deque_list[start].pop()
                    deque_list[dest].append(crate)
            else:
                crates = deque()
                for j in range(num + 1):
                    crates.appendleft(deque_list[start].pop())
                deque_list[dest] += crates
    
    return deque_list

input_path = "input"
deque_list, line_idx = create_deque_list(input_path)
final_deque_list = move_crates(input_path, line_idx, deque_list, 2)

for crate_deque in final_deque_list:
    print(crate_deque[-1], end="")
print()
