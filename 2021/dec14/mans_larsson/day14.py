from collections import Counter, defaultdict

rules = dict()
with open('inputs/day14') as f:
    for line_nr, line in enumerate(f):
        if line_nr == 0:
            orig_seq = line.rstrip()
        elif len(line) > 1:
            data = line.rstrip().split(' -> ')
            rules[data[0]] = data[0][0] + data[1]


def expand_seq(seq, steps):
    for _ in range(steps):
        new_seq = ''
        for i in range(len(seq) - 1):
            new_seq += rules[seq[i:i+2]]
        seq = new_seq + seq[-1]
    return seq

# a
expanded = expand_seq(orig_seq, 10)
counts = Counter(expanded).most_common()
print(counts[0][1] - counts[-1][1])

# b
# calculate how each pair is expanded after 10 steps
calculation_lookup = dict()
for pair in rules.keys():
    calculation_lookup[pair] = expand_seq(pair, 10)


def expand_and_count_pair(pair, depth, count_dict_lookup):
    # avoid redoing calcs
    lookup_key = pair + str(depth)
    if lookup_key in count_dict_lookup:
        counting_dict = count_dict_lookup[lookup_key]
        return counting_dict, count_dict_lookup
    
    counting_dict = defaultdict(lambda: 0)
    if depth == 3:
        counts = Counter(calculation_lookup[pair][:-1]).most_common()
        for count in counts:
            counting_dict[count[0]] += count[1]
    else:
        expansion = calculation_lookup[pair]
        for i in range(len(expansion) - 1):
            this_pair = expansion[i:i+2]
            counts, count_dict_lookup = expand_and_count_pair(this_pair, depth + 1, count_dict_lookup)
            for key, val in counts.items():
                counting_dict[key] += val

    count_dict_lookup[lookup_key] = counting_dict
    return counting_dict, count_dict_lookup
        


count_dict_lookup = dict()
counting_dict = defaultdict(lambda: 0)
for i in range(len(orig_seq) - 1):
    this_pair = orig_seq[i:i+2]
    counts, _ = expand_and_count_pair(this_pair, 0, count_dict_lookup)
    for key, val in counts.items():
        counting_dict[key] += val

counting_dict[orig_seq[-1]] += 1
print(max(counting_dict.values())-min(counting_dict.values()))