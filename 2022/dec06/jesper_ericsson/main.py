import os

def read_data(filename):
    datastreams = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            datastreams.append(line.rstrip())

    return datastreams


def message_check(datastream, num_check):
    for char_ind in range(num_check, len(datastream)):
        last_four = set(datastream[char_ind-num_check:char_ind])
        if len(last_four) == num_check:
            return char_ind


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"
    datastreams = read_data(filename)

    for datastream in datastreams:
        prob1 = message_check(datastream, 4)
        prob2 = message_check(datastream, 14)

        print(f"Prob 1, message ind: {prob1}")
        print(f"Prob 2, message ind: {prob2}")


if __name__ == "__main__":
    main()
