def play_game(starting_numbers, last_turn):
    spoken_nums = {num: turn+1 for turn, num in enumerate(starting_numbers[:-1])}

    turn = len(starting_numbers) + 1
    previous_num = starting_numbers[-1]
    this_num = None
    while turn <= last_turn:
        if previous_num in spoken_nums:
            this_num = turn - 1 - spoken_nums[previous_num]
        else:
            this_num = 0

        spoken_nums[previous_num] = turn - 1
        previous_num = this_num
        turn += 1

    return this_num


puzzle_input = (16, 1, 0, 18, 12, 14, 19)
print(f'a) {play_game(puzzle_input, 2020)}')
print(f'b) {play_game(puzzle_input, 30000000)}')
