from tqdm import tqdm

def parse():
    map_names = ('seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity')

    with open('inputs/day5') as f:
        lines = [line.rstrip() for line in f]

    seeds = [int(c) for c in lines[0].rstrip()[7:].split()]

    maps = {}
    line_index = 0
    current_map_name = None
    while line_index < len(lines) - 1:
        line_index += 1
        if len(lines[line_index]) == 0:
            current_map_name = None
            continue

        if current_map_name is None:
            for mn in map_names:
                if lines[line_index].startswith(mn):
                    current_map_name = mn
                    maps[current_map_name] = []
                    break
        else:
            maps[current_map_name].append(tuple(int(c) for c in lines[line_index].split()))

    return seeds, maps


def eval_seed(seed, maps):
    current_val = seed
    for map in maps.values():
        for rang in map:
            if current_val >= rang[1] and current_val < rang[1] + rang[2]:
                current_val = current_val - rang[1] + rang[0]
                break
    return current_val


def run_seeds(seeds, maps):
    lowest_val = 1e10
    for seed in tqdm(seeds):
        current_val = eval_seed(seed, maps)
        if current_val < lowest_val:
            lowest_val = current_val

    return lowest_val


def run_range(low, high, maps):
    diff = high - low

    loc_low = eval_seed(low, maps)
    loc_high = eval_seed(high, maps)

    if loc_high - loc_low == diff:  # linear area, we can return lowest
        return loc_low
    else:
        middle = low + diff // 2
        lower_half = run_range(low, middle, maps)
        upper_half = run_range(middle + 1, high, maps)

        return min(lower_half, upper_half)


if __name__ == '__main__':
    seeds, maps = parse()

    print(run_seeds(seeds, maps))

    lowest = 1e10
    for start, len in zip(seeds[0::2], seeds[1::2]):
        current = run_range(start, start + len, maps)
        if current < lowest:
            lowest = current

    print(lowest)
