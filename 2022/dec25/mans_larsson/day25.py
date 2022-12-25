def snafu_to_b10(snafu_num: str):
    multiplier = 1
    b10 = 0
    for ch in reversed(snafu_num):
        if ch == '=':
            b10 -= 2*multiplier
        elif ch == '-':
            b10 -= multiplier
        else:
            b10 += int(ch)*multiplier
        multiplier *= 5
    return b10


def b10_to_snafu(b10: int):
    digit_to_snafu_digit = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
    snafu = []
    largest_multiplier = 1
    while b10 // largest_multiplier > 2:
        largest_multiplier *= 5

    this_digit = round(b10 / largest_multiplier)
    snafu.append(digit_to_snafu_digit[this_digit])
    b10 -= this_digit * largest_multiplier
    while largest_multiplier != 1:
        largest_multiplier //= 5
        this_digit = round(b10 / largest_multiplier)
        snafu.append(digit_to_snafu_digit[this_digit])
        b10 -= this_digit * largest_multiplier
    return ''.join(s for s in snafu)


with open('inputs/day25') as f:
    snafu_lines = f.read().splitlines()

print(b10_to_snafu(sum([snafu_to_b10(sl) for sl in snafu_lines])))
