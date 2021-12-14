from collections import Counter


def parse_input(file_path): 
    with open(file_path, 'r') as f:
        text = f.read()
        tsplit = text.split('\n\n')
        template = tsplit[0]
        insertions_raw = tsplit[1]
        insertions = {}
        for line in insertions_raw.splitlines():
            lsplit = line.split('->')
            insertions[lsplit[0].strip()] = lsplit[1].strip()
    return template, insertions


if __name__ == '__main__':

    template, insertions = parse_input('./input_day14.txt')

    # Part I & II
    for num_steps in [10, 40]:
        counter = Counter([template[i: i + 2] for i in range(len(template) - 1)])
        for _ in range(num_steps):
            for pair, count in zip(list(counter.keys()), list(counter.values())):
                ins = insertions[pair]
                counter[pair] -= count
                counter[pair[0] + ins] += count
                counter[ins + pair[1]] += count

        most_common_pairs = filter(None, counter.most_common())
        most_common_elems = {e: 0 for e in ''.join(counter.keys())}
        for pair, count in most_common_pairs:
            most_common_elems[pair[0]] += count
            most_common_elems[pair[1]] += count

        # adjust for double counting and edge elements
        for elem, count in most_common_elems.items():
            if elem in [template[0], template[-1]]:
                most_common_elems[elem] = (count - 1)//2 + 1 
            else:
                most_common_elems[elem] = count//2
        print(max(most_common_elems.values()) - min(most_common_elems.values()))
