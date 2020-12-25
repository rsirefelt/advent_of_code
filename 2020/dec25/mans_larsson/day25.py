divisor = 20201227
initial_subject_number = 7


def get_loop_size(target_number):
    n_loops = 0
    num = 1
    while num != target_number:
        num *= initial_subject_number
        num = num % divisor
        n_loops += 1
    return n_loops


def transform(subject_number, n_loops):
    num = 1
    for _ in range(n_loops):
        num *= subject_number
        num = num % divisor
    return num


card_pub = 8184785
door_pub = 5293040

door_loop_size = get_loop_size(door_pub)
encryption_key = transform(card_pub, door_loop_size)

print(f'a) {encryption_key}')
