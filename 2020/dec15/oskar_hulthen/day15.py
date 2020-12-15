import copy


def task(inputs, last_number, limit):
    memory = copy.deepcopy(inputs)
    start_index = len(inputs)
    for idx in range(start_index, limit):
        # Shift for zero index start.
        idx += 1

        mem = memory[last_number]
        # First time
        if len(mem) == 1:
            memory[0].append(idx)
            last_number = 0
        else:
            # Get previous occurrences.
            largest = mem[-1]
            second_largest = mem[-2]
            diff = largest - second_largest

            if diff in memory:
                memory[diff].append(idx)
            else:
                memory[diff] = [idx]
            last_number = diff
    return last_number


if __name__ == "__main__":
    inputs = [15, 5, 1, 4, 7, 0]
    # Populate start info
    last_number = inputs[-1]
    inputs = {val: [index + 1] for index, val in enumerate(inputs)}

    res1 = task(inputs, last_number, limit=2020)
    print(res1)

    res2 = task(inputs, last_number, limit=30000000)
    print(res2)
