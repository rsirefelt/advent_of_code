with open('input.txt') as f:
    lines = f.read().splitlines()

print(len(lines))


def split_segments(line):
    segments = line.split('|')
    return segments[0].strip(), segments[1].strip()


output = [segment[1] for segment in map(split_segments, lines)]

# Count the number of occurences of length 2,3,4 and 7
# in the output

counts = {2: 0, 3: 0, 4: 0, 7: 0}

for line in output:
    # Split the line
    words = line.split()
    # Count the number of occurances of each length
    for word in words:
        if len(word) in counts:
            counts[len(word)] += 1

# Print the result
for length in counts:
    print(f'{length} {counts[length]}')

# Print sum
print(sum(counts.values()))

# Part 2, did a really dumb part 1...

values = []

for line in lines:

    # Split the line
    words = line.split('|')

    wiring = words[0].strip()
    segment = words[1].strip()

    # Frequency of each letter
    freq = {}
    for letter in wiring:
        if letter in freq and letter != ' ':
            freq[letter] += 1
        elif letter != ' ':
            freq[letter] = 1

    # Find 2 letter word which is 1
    for word in wiring.split():
        if len(word) == 2:
            one = word
        if len(word) == 4:
            four = word

    # Figure out mapping to agnostic 7 segment display

    # Find the letter that occurs 9 times it is segment f
    mapping = {}
    for letter in freq:
        if freq[letter] == 9:
            mapping[letter] = 'f'
        elif freq[letter] == 4:
            mapping[letter] = 'e'
        elif freq[letter] == 6:
            mapping[letter] = 'b'
        elif freq[letter] == 8 and letter not in one:
            mapping[letter] = 'a'
        elif freq[letter] == 8 and letter in one:
            mapping[letter] = 'c'
        elif freq[letter] == 7 and letter in four:
            mapping[letter] = 'd'
        elif freq[letter] == 7 and letter not in four:
            mapping[letter] = 'g'


    # Segments originals
    originals = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }
    #
    value = 0
    tens = 1000
    for output in segment.split():
        # Find the original segment
        output_prim = [mapping[letter] for letter in output]
        output_prim = ''.join(sorted(output_prim))
        print(output_prim)
        print(originals[output_prim])
        value += originals[output_prim] * tens
        tens /= 10
    values.append(value)

print(values)
print(sum(values))
