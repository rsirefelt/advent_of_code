def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines][:-1]
    instructions = []
    for line in lines:
        parts = line.split(" ")
        instructions.append([parts[0], int(parts[1])])
    return instructions

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0

def isAdjacent(head, tail):
    manhattan_dist = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    if manhattan_dist < 2:
        return True
    if manhattan_dist > 2:
        return False
    if head[0] == tail[0] or head[1] == tail[1]:
        return False
    return True


instructions = parseInput("input.txt")
visited_positions = set()
head = [0, 0]
tail = [0, 0]
visited_positions.add((tail[0], tail[1]))
for move in instructions:
    # Move the head
    while move[1] > 0:
        if move[0] == "R":
            head[0] = head[0] + 1
        elif move[0] == "L":
            head[0] = head[0] - 1
        elif move[0] == "U":
            head[1] = head[1] + 1
        elif move[0] == "D":
            head[1] = head[1] - 1
        else:
            assert False, "Invalid move!"

        # Move the tail if necessary
        if not isAdjacent(head, tail):
            tail[0] = tail[0] + sign(head[0] - tail[0])
            tail[1] = tail[1] + sign(head[1] - tail[1])
            visited_positions.add((tail[0], tail[1]))
        move[1] = move[1] - 1
    xxx = 3

print("Part 1: " + str(len(visited_positions)))

# Part 2: Copy and Paste
instructions = parseInput("input.txt")
visited_positions = set()
rope = [[0, 0] for k in range(10)]
visited_positions.add((rope[9][0], rope[9][1]))
for move in instructions:
    # Move the head
    while move[1] > 0:
        if move[0] == "R":
            rope[0][0] = rope[0][0] + 1
        elif move[0] == "L":
            rope[0][0] = rope[0][0] - 1
        elif move[0] == "U":
            rope[0][1] = rope[0][1] + 1
        elif move[0] == "D":
            rope[0][1] = rope[0][1] - 1
        else:
            assert False, "Invalid move!"

        # Move the rest of the rope
        for k in range(0, 9):
            if not isAdjacent(rope[k], rope[k+1]):
                rope[k+1][0] = rope[k+1][0] + sign(rope[k][0] - rope[k+1][0])
                rope[k+1][1] = rope[k+1][1] + sign(rope[k][1] - rope[k+1][1])

        visited_positions.add((rope[9][0], rope[9][1]))
        move[1] = move[1] - 1

print("Part 2: " + str(len(visited_positions)))