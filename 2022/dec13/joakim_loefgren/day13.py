import functools


def compare_packets(p1, p2):
    iter_p1 = iter(p1)
    iter_p2 = iter(p2)
    while True:
        p1_out = False
        p2_out = False
        try:
            left = next(iter_p1)
        except StopIteration:
            p1_out = True
        try: 
            right = next(iter_p2)
        except StopIteration:
            p2_out = True

        if p1_out and not p2_out:
            return True
        elif p2_out and not p1_out:
            return False
        elif p1_out and p2_out:
            return 'None'

        type_left, type_right = type(left), type(right)
        if type_left is type_right is int:
            if left < right:
                return True
            if left > right:
                return False
            else:
                continue
        else:
            if type_left is int:
                left = [left]
            elif type_right is int:
                right = [right]
            comp = compare_packets(left, right)
            if comp == True:
                return True
            elif comp == False:
                return False

if __name__ == '__main__':
    with open('./input.txt') as f:
        pairs_text = f.read().split('\n\n')

    pairs = []
    for text in pairs_text:
        lines = text.splitlines()
        pairs.append((eval(lines[0]), eval(lines[1])))

    # part I
    sum_ind = 0
    ind = 1
    for left, right in pairs:
        if compare_packets(left, right):
            sum_ind += ind
        ind += 1

    print(sum_ind)

    # part II
    packets = [p for pair in pairs for p in pair]
    dividers = [[[2]], [[6]]]
    packets.extend(dividers)
    custom_sort = lambda p1, p2: -1 if compare_packets(p1, p2) else 1
    packets_sorted = sorted(packets, key=functools.cmp_to_key(custom_sort))
    ind_prod = 1
    for ind, pack in enumerate(packets_sorted):
        if pack in dividers:
            ind_prod *= ind + 1

    print(ind_prod)
