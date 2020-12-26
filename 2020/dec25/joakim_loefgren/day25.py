""" Advent of Code Day 25 """


def transform(loop_size, subject_number):
    val = 1
    div = 20201227
    for i in range(loop_size):
        val *= subject_number
        val = val % div
    return val


def get_loop_size(key_target):
    key = 0
    subject_number = 7
    loop_size = 0
    div = 20201227
    val = 1
    i = 0
    while val != key_target:
        i += 1
        val *= subject_number
        val = val % div
    return i


if __name__ == "__main__":
    key_card = 1717001
    key_door = 523731
    loop_size_card = get_loop_size(key_card)
    loop_size_door = get_loop_size(key_door)
    key_encrypt1 = transform(loop_size_card, key_door)
    key_encrypt2 = transform(loop_size_door, key_card)
    print(key_encrypt1, key_encrypt2)
