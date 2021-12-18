start = 'FSHBKOOPCFSFKONFNFBB'


with open('real_input.txt') as f:
    rules = {x[0].strip(): x[1].strip() for x in [x.split('->') for x in f.read().splitlines()]}

def next_polymer(polymer):
    # Scan the string pairwise and insert characters from matching rules in between the pair
    next_polymer = ''
    for i in range(len(polymer)):
        if polymer[i:i + 2] in rules:
            next_polymer += polymer[i] + rules[polymer[i:i + 2]]
        else:
            next_polymer += polymer[i]
    return next_polymer


def get_bigrams_count(polymer):
    bigrams = {}
    for i in range(len(polymer) - 1):
        bigrams[polymer[i:i + 2]] = bigrams.get(polymer[i:i + 2], 0) + 1
    return bigrams


def part1_inefficient_style():
    # Apply the rules 10 times
    start2 = start
    for i in range(10):
        start2 = next_polymer(start2)
        print(i, start2)

    # Count frequencies of each letter
    freqs = {}
    for c in start2:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    return freqs


def new_style(bigrams):
    # Get the bigrams count
    from collections import defaultdict
    updated = defaultdict(lambda: 0)
    # Set default value to zero for dict

    # Run the rules for all bigrams
    for bigram, count in bigrams.items():
        if bigram in rules:
            new_bigrams = get_bigrams_count(next_polymer(bigram))
            for new_bigram, new_count in new_bigrams.items():
                updated[new_bigram] += new_count * count

        else:
            updated[bigram] = count
    return updated


if __name__ == '__main__':

    freqs = part1_inefficient_style()

    bigrams = get_bigrams_count(start)

    print(bigrams)
    for i in range(40):
        bigrams = new_style(bigrams)

    # Count frequencies of each letter ( count only first letter in bigram since they are overlapping )
    freqs2 = {}
    for bigram, count in bigrams.items():
        if bigram[0] in freqs2:
            freqs2[bigram[0]] += count
        else:
            freqs2[bigram[0]] = count
    # Add non counted letter at the end of the original string
    freqs2[start[-1]] += 1

    print(freqs)
    print(freqs2)

    # Print the difference between the shortest and the longest polymer
    print(min(freqs.values()), max(freqs.values()))

    print(f'Difference: {max(freqs.values()) - min(freqs.values())}')

    # Print same with new style
    print(min(freqs2.values()), max(freqs2.values()))

    print(f'Difference: {max(freqs2.values()) - min(freqs2.values())}')
