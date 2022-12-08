def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[0]

data = parseInput("input.txt")
for idx in range(14, len(data)):
    if len(set(data[idx-14:idx])) == 14:
        print(idx)
        break
