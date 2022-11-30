import numpy as np
import re

regex_target = re.compile(r"(-?\d*)\.\.(-?\d*)")


def readData():
    filename = "testdata.csv"
    filename = "data.csv"
    with open(filename, "r") as f:
        input = f.readline()

        target_area = regex_target.findall(input)
    f.close()
    return (int(target_area[0][0]), int(target_area[0][1])), (
        int(target_area[1][0]),
        int(target_area[1][1]),
    )


def calculate_trajectory(x_limits, y_limits, velocity):
    pos_list = [np.array([0, 0])]

    while True:
        pos_list.append(pos_list[-1] + velocity)
        # print(pos_list[-1])
        if (
            x_limits[0] <= pos_list[-1][0] <= x_limits[1]
            and y_limits[0] <= pos_list[-1][1] <= y_limits[1]
        ):
            return True, pos_list
        elif pos_list[-1][0] > x_limits[1] or pos_list[-1][1] < y_limits[0]:
            return False, pos_list

        if velocity[0] > 0:
            velocity[0] -= 1
        elif velocity[0] < 0:
            velocity[0] += 1
        velocity[1] -= 1

        # return pos_list


def prob1(x_limits, y_limits):
    max_heights = []
    count = 0
    for x_v in range(1, 150):
        for y_v in range(-150, 400):
            hit, pos_list = calculate_trajectory(
                x_limits, y_limits, np.array([x_v, y_v])
            )
            if hit:
                max_heights.append(max(pos_list, key=lambda x: x[1])[1])
                count += 1
                # print(x_v, y_v)
            # print("Problem 1, incomplete score:", sum_error_score)

    print(max(max_heights))
    print(count)


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
    x_limits, y_limits = readData()

    print(x_limits, y_limits)
    prob1(x_limits, y_limits)
    # prob2(system_rows)


if __name__ == "__main__":
    main()
