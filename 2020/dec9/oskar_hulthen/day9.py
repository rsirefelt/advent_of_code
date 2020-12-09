from itertools import product, combinations


def task1(int_list, preamble_length=25):
    previous_set = int_list[:preamble_length]
    int_list = int_list[preamble_length:]
    for key in int_list:
        # This can be speed up by not re-counting combinations from the middle.
        # Instead you can just append new number + all previous numbers.
        # But this is simple & fast enough...
        current_allowed_keys = [sum(combo) for combo in combinations(previous_set, 2)]

        if key in current_allowed_keys:
            # Update set through queue.
            previous_set.append(key)
            previous_set.pop(0)
        else:
            return key


def task2(int_list, invalid_num):
    len_list = len(int_list)
    for i in range(len_list):
        # Check remainder of list
        for j in range(i + 1, len_list):
            current_sum = sum(int_list[i:j])

            # If sum is breached --> try again
            if current_sum > invalid_num:
                break

            if current_sum == invalid_num:
                return min(int_list[i:j]) + max(int_list[i:j])


if __name__ == "__main__":
    with open("input") as f:
        lines = list(f.readlines())
        int_list = [int(i) for i in lines]

    invalid_num = task1(int_list)
    print(invalid_num)

    enc_weakness = task2(int_list, invalid_num)
    print(enc_weakness)
