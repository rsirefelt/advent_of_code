import numpy as np


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        # with open("data.csv", "r") as f:
        number_serie = [int(i) for i in f.readline().rstrip().split(",")]
        number_of_boards = int(len(f.readlines()) / 6)

    list_of_boards = []
    list_of_matches = []

    for board_num in range(number_of_boards):
        test_mat = np.loadtxt(filename, skiprows=2 + board_num * 6, max_rows=5)
        list_of_boards.append(test_mat)
        list_of_matches.append(np.zeros((5, 5), dtype=bool))

    return (list_of_boards, list_of_matches, number_serie)


def check_bingo(board):
    col_sums = board.sum(0)
    row_sums = board.sum(1)
    if 5 in col_sums or 5 in row_sums:
        return True
    else:
        return False


def calc_score(board, match_board, num):
    sum = np.sum(board, where=np.invert(match_board))
    return sum * num


def prob1(list_of_boards, list_of_matches, number_serie):

    for num in number_serie:
        for ind, board in enumerate(list_of_boards):
            list_of_matches[ind] = np.logical_or(board == num, list_of_matches[ind])

            if check_bingo(list_of_matches[ind]):
                score = calc_score(board, list_of_matches[ind], num)
                print("Problem 1:", int(score))
                return


def prob2(list_of_boards, list_of_matches, number_serie):

    for num in number_serie:
        boards_to_remove = []
        for ind, board in enumerate(list_of_boards):
            list_of_matches[ind] = np.logical_or(board == num, list_of_matches[ind])

            if check_bingo(list_of_matches[ind]):
                boards_to_remove.append(ind)

        if boards_to_remove:
            if len(list_of_boards) == 1:
                score = calc_score(list_of_boards[0], list_of_matches[0], num)
                print("Problem 2:", int(score))

            boards_to_remove.sort(reverse=True)
            for ind in boards_to_remove:
                list_of_matches.pop(ind)
                list_of_boards.pop(ind)


def main():
    (list_of_boards, list_of_matches, number_serie) = readData()

    prob1(list_of_boards, list_of_matches, number_serie)
    prob2(list_of_boards, list_of_matches, number_serie)


if __name__ == "__main__":
    main()
