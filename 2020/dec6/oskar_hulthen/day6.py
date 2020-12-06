import regex as re


def task(task=1):
    sum_counts = 0
    with open("input") as f:
        lines = list(f.readlines())
        current_set = set()
        # Add last newline (to not have to individually handle last group)
        lines.append("\n")
        # Have to handle first entry specifically, because if answers are [a][a][c]
        # c would otherwise count
        first_entry = True
        for line in lines:
            line = line.rstrip()
            if line == "":
                sum_counts += len(current_set)

                current_set = set()
                first_entry = True
                continue

            # Add current persons answer (always task 1, only for first person task 2)
            if task == 1 or first_entry:
                for question in line:
                    current_set.update(question)
                first_entry = False
            else:
                # Only keeps answers that were previously stated.
                current_set = {answer for answer in current_set if answer in line}
    print(sum_counts)


if __name__ == "__main__":
    task()
    task(2)
