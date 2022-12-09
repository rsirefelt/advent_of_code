
def follow(knot1_position, knot2_position):
    position_diff = tuple(h - t for h, t in zip(knot1_position, knot2_position))
    if abs(position_diff[0]) > 1 and abs(position_diff[1]) > 1:
        knot2_position = (knot2_position[0] + position_diff[0]//2, knot2_position[1] + position_diff[1]//2)
    elif abs(position_diff[0]) > 1:
        # knot1_position[1] to make diag moves
        knot2_position = (knot2_position[0] + position_diff[0]//2, knot1_position[1])
    elif abs(position_diff[1]) > 1:
        knot2_position = (knot1_position[0], knot2_position[1] + position_diff[1]//2)
    return knot2_position


def run_task(num_knots):
    knot_positions = [(0, 0) for _ in range(num_knots)]
    visited_tail_positions = set()
    visited_tail_positions.add(knot_positions[-1])

    with open('inputs/day9') as f:
        moves = f.read().splitlines()

    directions = {'L': (0, -1), 'R': (0, 1), 'U': (1, 0), 'D': (-1, 0)}
    for move in moves:
        move = move.split()
        direction = move[0]
        steps = int(move[1])

        for _ in range(steps):
            knot_positions[0] = tuple(a + d for a, d in zip(knot_positions[0], directions[direction]))
            for knot_i in range(num_knots - 1):
                knot_positions[knot_i+1] = follow(knot_positions[knot_i], knot_positions[knot_i+1])
            visited_tail_positions.add(knot_positions[-1])

    return len(visited_tail_positions)


print(run_task(2))
print(run_task(10))
