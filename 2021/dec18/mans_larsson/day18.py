def add(left, right):
    return '[' + left + ','+right + ']'


def reduce(number):
    while True:
        # check for explode
        exploded = False
        nest_level = -1
        for i in range(len(number)):
            if number[i] == '[':
                nest_level += 1
            if number[i] == ']':
                nest_level -= 1

            # Exploding pairs will always consist of two regular numbers.
            if nest_level == 4:
                start_of_nest_exp = i
                stop_of_nest_exp = i+1
                while number[stop_of_nest_exp] != ']':
                    stop_of_nest_exp += 1

                # left part
                pos_left = start_of_nest_exp - 1
                while pos_left > -1 and number[pos_left] in {'[', ']', ','}:
                    pos_left -= 1
                pos_left += 1

                if pos_left > 0:  # assign number
                    explode_left_number = int(number[start_of_nest_exp+1:stop_of_nest_exp].split(',')[0])
                    for nstr in reversed(number[:start_of_nest_exp-1].replace(']', ',').replace('[', ',').split(',')):
                        if len(nstr) > 0:
                            next_left_number = int(nstr)
                            break
                    new_left_number = explode_left_number + next_left_number
                    if start_of_nest_exp - pos_left < 2:
                        keep_ind = number[:start_of_nest_exp].rfind('[')
                        left_part_of_number = number[:keep_ind+1] + f'{new_left_number},'
                    else:
                        pos_of_left_num = number[:pos_left].rfind(str(next_left_number))
                        left_part_of_number = number[:pos_of_left_num] + \
                            str(new_left_number) + number[pos_left:start_of_nest_exp] + '0,'
                else:  # just remove an [ and add a 0
                    left_part_of_number = number[:start_of_nest_exp] + '0,'

                # right part
                pos_right = stop_of_nest_exp + 1
                while pos_right < len(number) and number[pos_right] in {'[', ']', ','}:
                    pos_right += 1
                pos_right -= 1

                if pos_right < len(number) - 1:  # assign number
                    explode_right_number = int(number[start_of_nest_exp+1:stop_of_nest_exp].split(',')[1])
                    for nstr in number[pos_right+1:].replace(']', ',').replace('[', ',').split(','):
                        if len(nstr) > 0:
                            next_right_number = int(nstr)
                            break
                    new_right_number = explode_right_number + next_right_number

                    if pos_right - stop_of_nest_exp < 2:
                        keep_ind = number[stop_of_nest_exp+1:].find(']')
                        right_part_of_number = f'{new_right_number}' + number[stop_of_nest_exp+1+keep_ind:]
                    else:  # locate number to be replaced
                        ind = number[pos_right+1:].replace('[', ']').replace(',', ']').find(']')
                        last_right_part = number[pos_right] + str(new_right_number) + number[pos_right + ind + 1:]
                        right_part_of_number = '0' + number[stop_of_nest_exp+1:pos_right] + last_right_part
                else:  # just remove an ] and add a 0
                    right_part_of_number = '0' + number[stop_of_nest_exp+1:]

                number = left_part_of_number + right_part_of_number
                exploded = True
                break

            if exploded:
                break
        if exploded:
            continue

        # check for split
        split = False
        for nstr in number.replace('[', ',').replace(']', ',').split(','):
            nstr_len = len(nstr)
            if nstr_len > 1:
                num = int(nstr)
                left = num // 2
                right = num // 2 + num % 2

                pos = number.find(nstr)
                number = number[:pos] + f'[{left},{right}]' + number[pos+nstr_len:]

                split = True
                break

        if not exploded and not split:
            break

    return number


def magnitude(number):
    while '[' in number or ']' in number:
        last_open_pos = 0
        for i in range(len(number)):
            if number[i] == '[':
                last_open_pos = i
            if number[i] == ']':
                if ',' in number[last_open_pos+1:i]:
                    nums = number[last_open_pos+1:i].split(',')
                    new_num = 3*int(nums[0]) + 2*int(nums[1])
                else:
                    nums = number[last_open_pos+1:i]
                number = number[:last_open_pos] + str(new_num) + number[i+1:]
                break
    return int(number)


numbers = []
with open('inputs/day18') as f:
    for line in f:
        numbers.append(line.rstrip())

sum = numbers[0]
for i in range(1, len(numbers)):
    sum = add(sum, numbers[i])
    sum = reduce(sum)
print(magnitude(sum))

max_magnitude = 0
for num1 in numbers:
    for num2 in numbers:
        mag = magnitude(reduce(add(num1, num2)))
        if mag > max_magnitude:
            max_magnitude = mag
print(max_magnitude)
