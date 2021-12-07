import numpy as np
from utils import read_lines

def parseInput(filename):
    """Read input and return boards as a 3D numpy array, and the list of numbers as an array."""
    lines = read_lines(filename)
    numbers = [int(num) for num in lines[0].split(',')]
    num_boards = (len(lines) - 1) // 6
    boards = np.zeros((num_boards,5,5), dtype=int)
    for board_id in range(0, num_boards):
        for row_num in range(5):
            start_row = 2 + 6*board_id
            row = [int(num) for num in [num for num in lines[start_row+row_num].strip().split(' ') if num != '']]
            boards[board_id, row_num, :] = row

    return numbers, boards

# Load the input and instantiate an empty Numpy array for all the marked numbers on the boards
numbers, boards = parseInput("/home/carl/Code/AdventOfCode/Day4/input.txt")
marked_numbers = np.zeros_like(boards, dtype=bool)
winners = [] # keep track of winning boards in the order they win
winning_scores = []
already_won = np.zeros(boards.shape[0], dtype=bool)

# Loop over all the numbers and mark them on the board
for num in numbers:
    marked_numbers[boards == num] = True

    # Check for any new winners. Check rows first
    winning_board_ids_rows = np.nonzero(np.any(np.sum(marked_numbers, axis=2) == 5, axis=1) & ~already_won)[0]
    for winning_board_id in winning_board_ids_rows:
        print('Found a winner: board ', winning_board_ids_rows[0])
        winning_board = boards[winning_board_id, :, :]
        winners.append(winning_board_id)
        winning_scores.append(np.sum(winning_board[marked_numbers[winning_board_id] == False])*num)
        already_won[winning_board_id] = True


    # Check the columns for new winners
    winning_board_ids_cols = np.nonzero(np.any(np.sum(marked_numbers, axis=1) == 5, axis=1) & ~already_won)[0]
    for winning_board_id in winning_board_ids_cols:
        print('Found a winner: board ', winning_board_ids_cols[0])
        winning_board = boards[winning_board_id, :, :]
        winners.append(winning_board_id)
        winning_scores.append(np.sum(winning_board[marked_numbers[winning_board_id] == False]) * num)
        already_won[winning_board_id] = True

print('Part 1:', winning_scores[0])
print('Part 2:', winning_scores[-1])
