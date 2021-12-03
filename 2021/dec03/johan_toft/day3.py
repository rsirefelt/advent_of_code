from aoc_helper import download_advent_of_code_input


def main():
    download_advent_of_code_input(2021, 3)

    with open('input.txt', 'r') as f:
        input_data = f.read().splitlines()

    def count_bits(inputs):
        # Create a dict to count the number of times each bit appears at a certain position
        bit_counts = {}

        for bitstring in inputs:
            for pos, bitval in enumerate((bitstring)):
                # Create initial '0' and '1' in dict
                if pos not in bit_counts:
                    bit_counts[pos] = {'0': 0, '1': 0}
                bit_counts[pos][bitval] += 1
        return bit_counts

    bit_counts = count_bits(input_data)

    # For each position, find the most common bit and create a new bitstring with that bit set at that position
    # and an inverted string for the least common bits
    most_common_bitstring = []
    least_common_bitstring = []
    for pos in bit_counts:
        most_common_bit = '1' if bit_counts[pos]['1'] >= bit_counts[pos]['0'] else '0'
        most_common_bitstring.append(most_common_bit)
        least_common_bitstring.append(str(1 - int(most_common_bit)))

    # Convert the bitstrings to ints
    gamma_val = int(''.join(most_common_bitstring), 2)
    epsilon_val = int(''.join(least_common_bitstring), 2)

    print(f"Part 1 {gamma_val * epsilon_val}")

    # Part 2

    """The bit criteria depends on which type of rating value you want to find:

    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
    """

    oxygen_candidates = set(input_data)
    co2_candidates = set(input_data)

    for pos in bit_counts:

        oxygen_counts = count_bits(oxygen_candidates)
        co2_counts = count_bits(co2_candidates)

        # Find the most common bit, if they are equally common, keep values with a 1 in the position being considered
        most_common_bit = '1' if oxygen_counts[pos]['1'] >= oxygen_counts[pos]['0'] else '0'
        # Find the least common bit, if they are equally common, keep values with a 0 in the position being considered
        least_common_bit = '0' if co2_counts[pos]['0'] <= co2_counts[pos]['1'] else '1'

        if len(oxygen_candidates) != 1:
            oxygen_candidates = list(filter(lambda x: x[pos] == most_common_bit, oxygen_candidates))

        if len(co2_candidates) != 1:
            co2_candidates = list(filter(lambda x: x[pos] == least_common_bit, co2_candidates))

    # Convert the remaining bitstrings to ints
    oxygen_val = int(''.join(oxygen_candidates[0]), 2)
    co2_val = int(''.join(co2_candidates[0]), 2)

    print("Part 2: Life support rating:", oxygen_val * co2_val)


if __name__ == "__main__":
    main()
