import numpy as np
from utils import read_lines

# Read the input as a matrix of booleans
input = read_lines("/home/carl/Code/AdventOfCode/Day3/input.txt")
A = np.zeros((len(input), len(input[0])), dtype=np.bool)
for row in range(len(input)):
    for col in range(len(input[0])):
        A[row, col] = int(input[row][col])

# Compute binary representation of gamma and epsilon numbers
num_ones = np.sum(A, axis=0)
num_zeros = np.sum(A==False, axis=0)
gamma = num_ones > num_zeros
epsilon = num_zeros > num_ones

# Convert the binary representation to decimal
conversion = {True : '1', False : '0'}
gamma_dec = int(''.join([conversion[digit] for digit in gamma]), 2)
epsilon_dec = int(''.join([conversion[digit] for digit in epsilon]), 2)

print('Part 1: ', gamma_dec*epsilon_dec)

# Part 2. First determine the oxygen generator rating
A_oxygen = np.copy(A)
for k in range(len(input[0])):
    # Find the desired bit at this position
    num_ones = np.sum(A_oxygen[:,k])
    num_zeros = np.sum(A_oxygen[:,k] == False)
    desired_bit = num_ones >= num_zeros

    # Remove all strings without this bit
    rows_to_keep = A_oxygen[:, k] == desired_bit
    A_oxygen = A_oxygen[rows_to_keep, :]

    # Stop when there is only one value left
    if A_oxygen.shape[0] == 1:
        break

oxygen_rating = int(''.join([conversion[digit] for digit in A_oxygen[0]]), 2)
xxx = 3

# Now find the CO2 scrubber rating
A_scrubber = np.copy(A)
for k in range(len(input[0])):
    # Find the desired bit at this position
    num_ones = np.sum(A_scrubber[:,k])
    num_zeros = np.sum(A_scrubber[:,k] == False)
    desired_bit = num_zeros > num_ones

    # Remove all strings without this bit
    rows_to_keep = A_scrubber[:, k] == desired_bit
    A_scrubber = A_scrubber[rows_to_keep, :]

    # Stop when there is only one value left
    if A_scrubber.shape[0] == 1:
        break

scrubber_rating = int(''.join([conversion[digit] for digit in A_scrubber[0]]), 2)

print('Part 2:', scrubber_rating*oxygen_rating)