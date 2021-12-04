import numpy as np


class Board:
    def __init__(self, data):
        self.data = data
        self.marked = np.zeros_like(data, dtype=bool)

    def mark(self, num):
        inds = (self.data == num).nonzero()
        for i, j in zip(inds[0], inds[1]):
            self.marked[i, j] = True

    def is_winner(self):
        return 5 in np.sum(self.marked, axis=0) or 5 in np.sum(self.marked, axis=1)

    def score(self, num_called):
        return np.sum(self.data[~self.marked]) * num_called


def fromstring_2d(arr_str, sep, dtype=float):
    arr = np.array(
        [np.fromstring(row, sep=sep, dtype=dtype) for row in arr_str.split("\n")]
    )
    return arr


def parse_input(file_path="./input_day4.txt"):
    with open(file_path, "r") as f:
        elements = f.read().split("\n\n")
    elements[-1] = elements[-1][:-1]
    bingo_seq = np.fromstring(elements[0], sep=",", dtype=int)
    board_data = [fromstring_2d(elem, sep=" ", dtype=int) for elem in elements[1:]]
    return bingo_seq, board_data


if __name__ == "__main__":
    bingo_seq, board_data = parse_input()
    boards = [Board(data) for data in board_data]

    # Part I
    winner_scores = []
    for num in bingo_seq:
        for board in boards:
            board.mark(num)
            if board.is_winner():
                winner_scores.append(board.score(num))
        if len(winner_scores) > 0:
            break
    print(f"Winner scores: {winner_scores}")

    # Part II
    has_won = []
    bingo_seq = iter(bingo_seq)
    while len(has_won) < len(boards):
        num = next(bingo_seq)
        for i in set(range(len(boards))) - set(has_won):
            boards[i].mark(num)
            if boards[i].is_winner():
                has_won.append(i)

    print(f"Last winner score: {boards[has_won[-1]].score(num)}")
