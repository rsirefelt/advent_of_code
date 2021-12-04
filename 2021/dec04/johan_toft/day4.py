import sys

from aoc_helper import download_advent_of_code_input


def main():
    download_advent_of_code_input(2021, 4)

    with open('input.txt', 'r') as f:
        input_data = f.read().splitlines()

    # First line of the input is the drawn numbers of the bingo
    numbers = input_data[0].split(',')
    numbers = [int(x) for x in numbers]

    print(numbers)
    drawn_numbers = set()

    # Split the remaining lines by empty lines
    lines = input_data[2:]
    bingo_boards = []

    current_board = []
    for line in lines:
        if line == '':
            bingo_boards.append(current_board)
            current_board = []
            continue
        else:
            current_board.append([int(x) for x in line.split()])

    class BingoBoard:
        def __init__(self, bingo_board, numbers, board_id):
            self.bingo_board = bingo_board
            self.numbers = numbers
            self.board_id = board_id

        def check_bingo(self):
            for line in self.bingo_board:
                if set(line).issubset(self.numbers):
                    return True
            # Check columns
            for i in range(5):
                column = [self.bingo_board[j][i] for j in range(5)]
                if set(column).issubset(self.numbers):
                    return True

            return False

        def calculate_board_score(self, last_number):
            # The score is the sum of all non-drawn numbers times last number
            board_numbers = set()
            for line in self.bingo_board:
                board_numbers.update(line)
            assert len(board_numbers) == 25
            unmarked_numbers = board_numbers.difference(self.numbers)
            if sum(unmarked_numbers) == 0:
                print(self.numbers, self.bingo_board)
            return sum(unmarked_numbers) * last_number

        def __eq__(self, other):
            return self.board_id == other.board_id

        def __hash__(self):
            return hash(self.board_id)

    bingo_boards = [BingoBoard(board, drawn_numbers, id) for (id, board) in enumerate(bingo_boards)]

    winning_boards = []
    winning_scores = []

    for number in numbers:
        drawn_numbers.add(number)
        remaining_boards = set(bingo_boards).difference(winning_boards)

        for board in remaining_boards:
            if board.check_bingo():
                winning_boards.append(board)
                winning_scores.append((board.calculate_board_score(number), board.board_id, number))


    # Part 1
    print(winning_scores[0][0])

    # Part 2
    print(winning_scores[-1][0])


if __name__ == "__main__":
    main()
