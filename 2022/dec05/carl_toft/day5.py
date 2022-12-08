def parseInput(filename, num_stacks):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    lines = lines[:-1]

    # Find crates in each stack
    stacks = [[] for stack in range(num_stacks)]
    idx = 0
    while lines[idx][:2] != ' 1':
        stack_idx = 0
        for stack_idx in range(num_stacks):
            idx2 = 4 * stack_idx + 1
            crate_name = lines[idx][idx2]
            if crate_name != ' ':
                stacks[stack_idx].append(crate_name)

        idx = idx + 1

    # Reverse the stacks
    for k in range(len(stacks)):
        stacks[k].reverse()

    # Read the move sequence
    idx = idx + 2
    move_sequence = []
    for k in range(idx, len(lines)):
        split_line = lines[k].split(' ')
        move_sequence.append((int(split_line[1]), int(split_line[-3]), int(split_line[-1])))

    return stacks, move_sequence

# Read the input
stacks, move_sequence = parseInput("input.txt", num_stacks=9)

# Move the crates
for move in move_sequence:
    temp_stack = []
    for _ in range(move[0]):
        temp_stack.append(stacks[move[1]-1].pop())
    for _ in range(move[0]):
        stacks[move[2] - 1].append(temp_stack.pop())

answer = ''
for stack_idx in range(len(stacks)):
    answer = answer + stacks[stack_idx][-1]

print(answer)
