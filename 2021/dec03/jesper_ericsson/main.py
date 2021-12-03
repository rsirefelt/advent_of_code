import numpy as np


def prob1(data):
    num_bits = len(data[0].rstrip())
    ones = np.zeros(num_bits)
    zeros = np.zeros(num_bits)
    for line in data:
        for ind, l in enumerate(line.rstrip()):

            if l == "1":
                ones[ind] += 1
            else:
                zeros[ind] += 1

    most_common_ones = (ones > zeros).astype(int)

    gamma = 0
    epsilon = 0
    for ind in range(num_bits):
        gamma += most_common_ones[ind] * 2 ** (num_bits - ind - 1)
        epsilon += (1 - most_common_ones[ind]) * 2 ** (num_bits - ind - 1)
    print("Gamma:", gamma)
    print("Epsilon:", epsilon)
    print("Gamma * Epsilon:", gamma * epsilon)


def create_matrix(data, num_lines, num_bits):
    input_matrix = np.zeros((num_lines, num_bits))
    for row, line in enumerate(data):
        for ind, l in enumerate(line.rstrip()):
            if l == "1":
                input_matrix[row, ind] = 1
    return input_matrix


def update_matrix(matrix, bit_ind, most_common):
    col = matrix[:, bit_ind]
    num_rows = len(col)

    sum_of_elements = np.sum(col)
    if most_common:
        ones_common = sum_of_elements >= (num_rows / 2)
    else:
        ones_common = sum_of_elements < (num_rows / 2)

    if ones_common:
        one_indices = col == 0
        matrix = np.delete(matrix, one_indices, 0)
    else:
        one_indices = col == 1
        matrix = np.delete(matrix, one_indices, 0)

    return matrix


def prob2(data):
    num_bits = len(data[0].rstrip())
    num_lines = len(data)

    input_matrix = create_matrix(data, num_lines, num_bits)
    oxygen_matrix = input_matrix
    for bit_ind in range(num_bits):

        oxygen_matrix = update_matrix(oxygen_matrix, bit_ind, True)
        if len(oxygen_matrix) == 1:
            break

    co2_matrix = input_matrix
    for bit_ind in range(num_bits):
        co2_matrix = update_matrix(co2_matrix, bit_ind, False)

        if len(co2_matrix) == 1:
            break

    oxygen = 0
    co2 = 0
    for ind in range(num_bits):
        oxygen += oxygen_matrix[0, ind] * 2 ** (num_bits - ind - 1)
        co2 += co2_matrix[0, ind] * 2 ** (num_bits - ind - 1)

    print("Oxygen:", oxygen)
    print("CO_2:", co2)
    print("Oxygen * CO_2:", oxygen * co2)
    print(oxygen)
    print(co2)
    print(oxygen * co2)


def main():
    # with open('testdata.csv', 'r') as f:
    with open("data.csv", "r") as f:
        data_lines = f.readlines()

    prob1(data_lines)
    prob2(data_lines)


if __name__ == "__main__":
    main()
