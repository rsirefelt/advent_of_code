SPELLEDOUT = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def part_a():
    numbers = []
    with open('inputs/day1') as f:
        for line in f:
            number = 0
            data = line.rstrip()
            for c in data:
                if c.isnumeric():
                    number += 10*int(c)
                    break
            for c in reversed(data):
                if c.isnumeric():
                    number += int(c)
                    break

            numbers.append(number)
    return sum(numbers)


def part_b():
    numbers = []
    with open('inputs/day1') as f:
        for line in f:
            data = line.rstrip()

            leftmost_num = None
            rightmost_num = None
            leftmost_pos = len(line)
            rightmost_pos = -1

            for num_string, num in SPELLEDOUT.items():
                pos = data.find(num_string)
                rpos = data.rfind(num_string)

                if pos >= 0 and pos < leftmost_pos:
                    leftmost_pos = pos
                    leftmost_num = num
                if rpos > rightmost_pos:
                    rightmost_pos = rpos
                    rightmost_num = num

            for i in range(leftmost_pos):
                c = data[i]
                if c.isnumeric():
                    leftmost_num = int(c)
                    break

            for i in range(len(data)-1, rightmost_pos, -1):
                c = data[i]
                if c.isnumeric():
                    rightmost_num = int(c)
                    break

            numbers.append(10*leftmost_num + rightmost_num)
    return sum(numbers)


print(part_a())
print(part_b())
