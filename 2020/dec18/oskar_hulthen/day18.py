import re


def task(lines, task=1):
    sum_ = 0
    for line in lines:
        sum_ += calculate(line, task)
    return sum_


def calculate(line, task):
    # Extract all internal paranthesis.
    pattern = re.findall("\(([0-9\* \+]*)\)", line)
    if not pattern:
        # No paranthesis left --> Calculate final expression
        entries = line.rstrip().split(" ")
        if task == 1:
            return evaluate_1(entries)
        else:
            return evaluate_2(entries)
    else:
        # Check paranthesis.
        for paranthesis in pattern:
            # Evaluate paranthesis.
            internal_result = str(calculate(paranthesis, task))
            # Replace paranthesis with new value.
            line = line.replace(f"({paranthesis})", internal_result)

        # Recursively calculate new line.
        return calculate(line, task)


def evaluate_1(entries):
    previous_value = int(entries[0])
    for idx in range(1, len(entries), 2):
        # Merge previous value, operation and next value into string.
        str_ = f"{previous_value}{entries[idx]}{entries[idx + 1]}"
        previous_value = eval(str_)
    return previous_value


def evaluate_2(entries):
    new_entries = []
    previous_value = int(entries[0])
    # Calculate all additions:
    for idx in range(1, len(entries), 2):
        if entries[idx] == "+":
            previous_value = previous_value + int(entries[idx + 1])
        else:
            new_entries.append(previous_value)
            new_entries.append("*")
            previous_value = int(entries[idx + 1])

    # If there is no multiplications to calculate:
    if len(new_entries) == 0:
        return previous_value

    # Add final value.
    new_entries.append(previous_value)

    previous_value = int(new_entries[0])
    # Calculate all multiplications:
    for idx in range(1, len(new_entries), 2):
        previous_value = previous_value * int(new_entries[idx + 1])
    return previous_value


if __name__ == "__main__":
    with open("input") as f:
        lines = list(f.readlines())
    print(f"Result task1: {task(lines)}")

    print(f"Result task2: {task(lines, 2)}")
