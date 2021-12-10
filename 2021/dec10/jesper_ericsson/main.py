import numpy as np
import re

regex_closed = re.compile(r"(\(\)|\[\]|\{\}|\<\>)")


def readData():
    filename = "testdata.csv"
    # filename = "data.csv"
    with open(filename, "r") as f:
        input_lines = f.readlines()
        system_rows = []

        for line in input_lines:
            system_rows.append(line.rstrip())

    return system_rows


def reduce_row(row):
    while len(row) > 0:
        if len(regex_closed.findall(row)) > 0:
            row = row.replace("()", "")
            row = row.replace("[]", "")
            row = row.replace("{}", "")
            row = row.replace("<>", "")
        else:
            break
    return row


def get_incomplete_score(row):
    end_signs = [")", "]", "}", ">"]
    scores = [3, 57, 1197, 25137]
    new_score = 0
    first_ind = 1000
    for score_ind, sign in enumerate(end_signs):
        ind = row.find(sign)
        if ind > -1 and ind < first_ind:
            first_ind = ind
            new_score = scores[score_ind]
    return new_score


def prob1(system_rows):
    sum_error_score = 0

    for row in system_rows:
        row = reduce_row(row)
        sum_error_score += get_incomplete_score(row)
    print("Problem 1, incomplete score:", sum_error_score)


def prob2(system_rows):
    score_dict = {"(": 1, "[": 2, "{": 3, "<": 4}
    complete_score = []
    for row in system_rows:
        row = reduce_row(row)
        if get_incomplete_score(row) == 0:
            row_score = 0
            for c in row[::-1]:
                row_score = row_score * 5 + score_dict[c]

            complete_score.append(row_score)

    median_score = np.median(complete_score)
    print("Problem 2, The middle complete score:", int(median_score))


def main():
    system_rows = readData()

    prob1(system_rows)
    prob2(system_rows)


if __name__ == "__main__":
    main()
