def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def move(data, indices, idx):
    if data[idx] == -2:
        xxx = 3

    value = data.pop(idx)
    idx2 = indices.pop(idx)

    new_pos = (idx + value) % len(data)
    if new_pos == 0:
        new_pos = len(data)
    data.insert(new_pos, value)
    indices.insert(new_pos, idx2)

data = [int(x)*811589153 for x in parseInput("input.txt")]
indices = [k for k in range(len(data))]

for iter in range(10):
    for k in range(len(data)):
        idx = indices.index(k)
        move(data, indices, idx)

index_of_zero = data.index(0)

num_1 = data[(index_of_zero + 1000) % len(data)]
num_2 = data[(index_of_zero + 2000) % len(data)]
num_3 = data[(index_of_zero + 3000) % len(data)]

print("Part 1: " + str(num_1+num_2+num_3))

xxx = 3