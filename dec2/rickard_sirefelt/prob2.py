import numpy as np

with open("dec2/rickard_sirefelt/input.txt", 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    correct_line = None

    for l1 in range(len(lines)):
        line1 = np.array([ord(c) for c in lines[l1]])
        for l2 in range(l1 + 1, len(lines)):
            line2 = np.array([ord(c) for c in lines[l2]])

            diff = line1 - line2
            if sum(diff != 0) == 1:
                correct_line = line1[diff == 0]
                break

        if correct_line is not None:
            break

    print("".join(chr(c) for c in correct_line))
