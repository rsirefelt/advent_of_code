from collections import deque

num_distinct_char = 14

with open("input") as f:
    line = f.readline().strip()

seq = deque()
copies = False
for i, c in enumerate(line):
    if i < num_distinct_char:
        seq.append(c)
    else:
        if len(set(seq)) == num_distinct_char:
            print(i)
            break
        else:
            seq.popleft()
            seq.append(c)



