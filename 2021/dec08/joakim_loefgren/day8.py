from collections import Counter 


def parse_input(file_path='./input_day8.txt'):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        inputs = []
        outputs = []
        for line in lines:
            lsplit = line.split('|')
            inputs.append([''.join(sorted(s)) for s in lsplit[0].strip().split()])
            outputs.append([''.join(sorted(s)) for s in lsplit[1].strip().split()])
        return inputs, outputs


def deduce_from_147(digits):
    """ numbers 1, 4, 7 """
    clues_raw = {
        'cf': set(next(d for d in iter(digits) if len(d) == 2)),
        'acf': set(next(d for d in iter(digits) if len(d) == 3)),
        'bcdf': set(next(d for d in iter(digits) if len(d) == 4)),
    }
    clues = {
        'a': clues_raw['acf'] - clues_raw['cf'],
        'cf': clues_raw['cf'], 
        'bd': clues_raw['bcdf'] - clues_raw['cf']
    }
    return clues


def deduce_segment_map(digits):
    freqs_true = {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}
    freqs = Counter(''.join(digits))
    inv_segment_map = {c: [] for c in freqs_true}
    for c in freqs_true:
        inv_segment_map[c].extend([d for d in freqs if freqs_true[c] == freqs[d]])
    inv_segment_map = {k: set(v) for k, v in inv_segment_map.items()} 

    clues = deduce_from_147(digits)

    # handle a, c which are mapped to the same segments
    inv_segment_map['c'] = inv_segment_map['c'] - clues['a']
    inv_segment_map['a'] = clues['a']

    # handle d, g which are also mappped to the same segments
    inv_segment_map['d'] = clues['bd'] - inv_segment_map['b']
    inv_segment_map['g'] = inv_segment_map['g'] - inv_segment_map['d']

    # invert & convert sets to strs
    segment_map = {v.pop(): k for k, v in inv_segment_map.items()}
    return segment_map


def decode_digits(segment_map, digits):
    codes = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
    digits_decoded = []
    for digit in digits:
        dec = ''.join(sorted(digit.translate(str.maketrans(segment_map))))
        digits_decoded.append(str(codes[dec]))
    number = int(''.join(digits_decoded))
    return number


if __name__ == '__main__':
    inputs, outputs = parse_input()

    # Part I
    counts = {n: 0 for n in range(2, 8)}
    for i in range(len(outputs)):
        for j in range(4):
            counts[len(outputs[i][j])] += 1
    print(sum([counts[n] for n in [2, 4, 3, 7]])) 

    # Part II
    sum_numbers = 0
    for i, digits in enumerate(inputs):
        segment_map = deduce_segment_map(digits)
        number = decode_digits(segment_map, outputs[i])
        sum_numbers += number
    print(sum_numbers)
