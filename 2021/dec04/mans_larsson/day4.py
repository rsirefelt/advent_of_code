import numpy as np

boards = []
with open('inputs/day4') as f:
    current_board = np.zeros((5, 5), dtype=np.int32)
    board_index = 0
    for line_nr, line in enumerate(f):
        if line_nr == 0:
            draws = [int(str) for str in line.rstrip().split(',')]
        elif len(line) > 1:
            current_board[board_index, :] = np.array(line.rstrip().split()).astype(np.int32)
            board_index += 1
            if board_index == 5:
                boards.append(current_board)
                current_board = np.zeros((5, 5), dtype=np.int32)
                board_index = 0


drawn_masks = [np.zeros((5, 5), dtype=bool) for i in range(len(boards))]
has_bingo = np.zeros((len(drawn_masks)), dtype=bool)
for number in draws:
    board_index = 0
    for board, drawn_mask in zip(boards, drawn_masks):
        if has_bingo[board_index]:
            board_index += 1
            continue
        drawn_mask |= board == number

        if np.any(np.sum(drawn_mask, axis=0) == 5) or np.any(np.sum(drawn_mask, axis=1) == 5):
            if not np.any(has_bingo):
                score_a = np.sum(board[~drawn_mask])*number
            score_b = np.sum(board[~drawn_mask])*number
            has_bingo[board_index] = True

        board_index += 1
    if np.all(has_bingo):
        break

print(score_a)
print(score_b)
