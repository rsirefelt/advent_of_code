import numpy as np
import re
import matplotlib.pyplot as plt

re_coord = re.compile(r"([\d]*),([\d]*)")
re_fold = re.compile(r"(fold along )([xy])=([\d]*)")


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        x_pos = []
        y_pos = []
        fold_lines = []

        for line in input_lines:
            coords = re_coord.findall(line)
            fold = re_fold.findall(line)

            if coords:
                x_pos.append(int(coords[0][0]))
                y_pos.append(int(coords[0][1]))
            elif fold:
                fold_lines.append((fold[0][1], int(fold[0][2])))

        f.close()

    return np.array(x_pos), np.array(y_pos), fold_lines


def create_matrix(x_pos, y_pos):
    instruction_mat = np.zeros((y_pos.max() + 1, x_pos.max() + 1))
    for x, y in zip(x_pos, y_pos):
        instruction_mat[y, x] = 1
    return instruction_mat


def make_folding(pos_array, fold_line):
    pos_array -= fold_line
    pos_array[pos_array > 0] = -pos_array[pos_array > 0]
    pos_array -= pos_array.min()

    return pos_array


def prob1(x_pos, y_pos, fold_lines):

    if fold_lines[0][0] == "x":
        x_pos = make_folding(x_pos, fold_lines[0][1])
    else:
        y_pos = make_folding(y_pos, fold_lines[0][1])

    instruction_mat = create_matrix(x_pos, y_pos)
    print("Problem 1, number of visible points:", int(instruction_mat.sum()))


def prob2(x_pos, y_pos, fold_lines):

    for fold in fold_lines:
        if fold[0] == "x":
            x_pos = make_folding(x_pos, fold[1])
        else:
            y_pos = make_folding(y_pos, fold[1])

    instruction_mat = create_matrix(x_pos, y_pos)
    image = plt.imshow(instruction_mat, cmap="cividis")

    plt.show()


def main():
    x_pos, y_pos, fold_lines = readData()
    prob1(x_pos, y_pos, fold_lines)
    prob2(x_pos, y_pos, fold_lines)


if __name__ == "__main__":
    main()
