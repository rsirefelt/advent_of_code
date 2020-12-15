def get_final_num_said(final_num):
    said_numbers = {7: 1, 12: 2, 1: 3, 0: 4, 16: 5, 2: 6}
    last_num = 2
    last_num_first_time = True
    for i in range(len(said_numbers.keys()) + 1, final_num + 1):
        if last_num_first_time:
            said_num = 0
        else:
            said_num = i - 1 - said_numbers[last_num]

        if said_num in said_numbers or said_num == last_num:
            last_num_first_time = False
        else:
            last_num_first_time = True

        said_numbers[last_num] = i - 1
        last_num = said_num

    return said_num


print(f"2020th number said: {get_final_num_said(2020)}")
print(f"30000000th number said: {get_final_num_said(30000000)}")
