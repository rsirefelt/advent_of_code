import numpy as np

all_signal_patterns = []
all_outputs = []
with open('inputs/day8') as f:
    for line in f:
        data = line.rstrip().split('|')
        all_signal_patterns.append([set(pattern) for pattern in data[0].split()])
        all_outputs.append([set(pattern) for pattern in data[1].split()])

count_a = 0
sum_b = 0
for signal_patterns, outputs in zip(all_signal_patterns, all_outputs):
    pattern_dict = {}
    pattern_dict[1] = [pattern for pattern in signal_patterns if len(pattern) == 2][0]
    pattern_dict[4] = [pattern for pattern in signal_patterns if len(pattern) == 4][0]
    pattern_dict[7] = [pattern for pattern in signal_patterns if len(pattern) == 3][0]
    pattern_dict[8] = [pattern for pattern in signal_patterns if len(pattern) == 7][0]

    two_three_five = [pattern for pattern in signal_patterns if len(pattern) == 5]
    zero_six_nine = [pattern for pattern in signal_patterns if len(pattern) == 6]

    # four is subset of nine but not zero and six
    pattern_dict[9] = [pattern for pattern in zero_six_nine if pattern_dict[4].issubset(pattern)][0]
    zero_six = [pattern for pattern in zero_six_nine if pattern != pattern_dict[9]]

    # one is subset of zero but not six
    pattern_dict[0] = [pattern for pattern in zero_six if pattern_dict[1].issubset(pattern)][0]
    pattern_dict[6] = [pattern for pattern in zero_six if pattern != pattern_dict[0]][0]

    # seven is subset of three but not two and five
    pattern_dict[3] = [pattern for pattern in two_three_five if pattern_dict[7].issubset(pattern)][0]
    two_five = [pattern for pattern in two_three_five if pattern != pattern_dict[3]]

    # difference between six and five is 1 and between six and two is two
    pattern_dict[2] = [pattern for pattern in two_five if len(pattern_dict[6] - pattern) == 2][0]
    pattern_dict[5] = [pattern for pattern in two_five if len(pattern_dict[6] - pattern) == 1][0]

    number_outputs = []
    for output in outputs:
        number_outputs.append([number for number, pattern in pattern_dict.items() if pattern == output][0])

    number_outputs = np.array(number_outputs)
    for number in (1, 4, 7, 8):
        count_a += np.sum(number_outputs == number)

    for number, power in zip(number_outputs, (1000, 100, 10, 1)):
        sum_b += number*power

print(count_a)
print(sum_b)
