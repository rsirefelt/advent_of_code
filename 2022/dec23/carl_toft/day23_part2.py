def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def get_elf_positions(lines):
    elves = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "#":
                elves.add((row,col))
    return elves

def move_elves(elves):
    new_elves = set()
    proposed_moves = {}
    num_proposed_moves = {}
    for elf in elves:
        # Check if neighbours are empty
        any_neighbours = False
        for delta_row in [-1,0,1]:
            for delta_col in [-1,0,1]:
                if delta_row == 0 and delta_col == 0:
                    continue
                if (elf[0] + delta_row, elf[1] + delta_col) in elves:
                    any_neighbours = True
        if not any_neighbours:
            # If no neighbours, the elf remains in the same position
            proposed_moves[elf] = elf
            if elf not in num_proposed_moves:
                num_proposed_moves[elf] = 1
            else:
                num_proposed_moves[elf] = num_proposed_moves[elf] + 1
            continue

        for dir in positions_to_check:
            is_direction_free = True
            for pos in dir:
                if (elf[0]+pos[0], elf[1]+pos[1]) in elves:
                    is_direction_free = False

            # Propose a move in the current direction if it is free
            if is_direction_free:
                new_pos = (elf[0] + dir[1][0], elf[1] + dir[1][1])
                proposed_moves[elf] = new_pos
                if new_pos not in num_proposed_moves:
                    num_proposed_moves[new_pos] = 1
                else:
                    num_proposed_moves[new_pos] = num_proposed_moves[new_pos] + 1
                break
            # No free space to move! Stay where you are
            proposed_moves[elf] = elf
            if elf not in num_proposed_moves:
                num_proposed_moves[elf] = 1
            else:
                num_proposed_moves[elf] = num_proposed_moves[elf] + 1

    # Now all elves have proposed their moves. Move them!
    for elf in elves:
        if num_proposed_moves[proposed_moves[elf]] == 1:
            new_elves.add(proposed_moves[elf])
        else:
            new_elves.add(elf)

        # We have a neighbour. Move in one of the direction
    return new_elves

positions_to_check = [[(-1, -1), (-1, 0), (-1, 1)],
                      [(1, -1), (1, 0), (1, 1)],
                      [(-1, -1), (0, -1), (1, -1)],
                      [(-1, 1), (0, 1), (1, 1)],
]

elves = get_elf_positions(parseInput("input.txt"))

for round in range(1000000):
    new_elves = move_elves(elves)
    if new_elves == elves:
        print("Part 2: " + str(round+1))
        break
    positions_to_check.append(positions_to_check.pop(0))
    elves = new_elves

min_row = min([elf[0] for elf in elves])
max_row = max([elf[0] for elf in elves])
min_col = min([elf[1] for elf in elves])
max_col = max([elf[1] for elf in elves])

num_tiles = (max_row - min_row + 1)*(max_col - min_col + 1) - len(elves)
print("Part 1: " + str(num_tiles))


# Part 2:
# TODO: COMPUTE SIZE OF AREA - NUM ELVES
