import numpy as np


def task():
    max_seat_id = 0
    seat_map = np.zeros((128 * 8))
    with open("input") as f:
        for line in f:
            line = line.rstrip()
            row_string = line[:7]
            col_string = line[-3:]

            row_index = 0
            for i, char_ in enumerate(row_string):
                if char_ == "B":
                    row_index += 2 ** (6 - i)

            col_index = 0
            for j, char_ in enumerate(col_string):
                if char_ == "R":
                    col_index += 2 ** (2 - j)

            seat_id = row_index * 8 + col_index
            seat_map[seat_id] = 1

            if seat_id >= max_seat_id:
                max_seat_id = seat_id

    print(max_seat_id)
    # Find number of leading zeros.
    offset = np.min(np.nonzero(seat_map))
    # Remove leading and trailing zeros from map.
    seat_map = np.trim_zeros(seat_map)
    # Locate seat by finding 0 value.
    seat = np.where(seat_map == 0)[0][0] + offset
    print(seat)


if __name__ == "__main__":
    task()
