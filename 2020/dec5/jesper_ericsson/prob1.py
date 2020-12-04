
def read_boardingpasses(filename):
    boardingpass = []

    with open(filename, 'r') as f:
        data_lines = f.readlines()
        # print(data_lines)
        for string in data_lines:
            boardingpass.append(string.rstrip())

    return boardingpass

def get_row(row_string):
    row = 0
    for exponent,letter in enumerate(row_string):
        if letter == 'B':
            row = row + 2**(6-exponent)
    return row

def get_col(row_string):
    col = 0
    for exponent,letter in enumerate(row_string):
        if letter == 'R':
            col = col + 2**(2-exponent)
    return col

def get_rows_and_cols(boardingpasses):
    rows = []
    cols = []
    for boardingpass in boardingpasses:
        rows.append(get_row(boardingpass[0:7]))
        cols.append(get_col(boardingpass[-3:]))

    return zip(rows, cols)

def get_seat_ids(rows_cols):
    seat_ids = []
    for rows, cols in rows_cols:
        seat_ids.append(rows*8 + cols)
    return seat_ids

def find_missing_seat_id(seat_ids):
    seat_ids.sort()
    missing_set = set(range(seat_ids[0], seat_ids[-1]+1)) - set(seat_ids)
    missing_set = set(range(seat_ids[0], 922)) - set(seat_ids)
    
    if len(missing_set) == 1:
        return missing_set.pop()
    else:
        for seat in missing_set:
            #Do something smart here...


def main():
    
    # boardingpasses = read_boardingpasses('testdata.csv')
    boardingpasses = read_boardingpasses('data.csv')
    rows_cols = get_rows_and_cols(boardingpasses)


    
    seat_ids = get_seat_ids(rows_cols)
    print('Part1 max seat id: %i' %max(seat_ids))
    your_seat = find_missing_seat_id(seat_ids)
    print('Part2 your seat id: %i' %your_seat)

if __name__ == "__main__": main()