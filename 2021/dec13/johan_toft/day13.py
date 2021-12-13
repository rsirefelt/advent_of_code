with open('input.txt') as f:
    data = f.read()

def parse_data(data):
    lines = data.splitlines()
    points = []
    folds = []

    for line in lines:
        # If line 0 is a digit
        if len(line) > 0 and line[0].isdigit():
            # it is a coordinate
            x, y = line.split(',')
            points.append((int(x), int(y)))
        elif line.startswith('fold'):
            import re
            apa = (re.search('(x|y)=(\d+)', line).groups())
            folds.append((apa[0], int(apa[1])))

    return points, folds


points, folds = parse_data(data)
points = set(points)
print(folds)


def fold1d(line, value):
    if value > line:
        return line - (value - line)
    else:
        return value


for fold in folds:
    if fold[0] == 'x':
        points = set([(fold1d(fold[1], x), y) for x, y in points])
    else:
        points = set([(x, fold1d(fold[1], y)) for x, y in points])

# Create a grid
for y in range(0, max(points, key=lambda x: x[1])[1] + 1):
    for x in range(0, max(points, key=lambda x: x[0])[0] + 1):
        if (x, y) in points:
            print('█', end='')
        else:
            print(' ', end='')

