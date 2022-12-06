with open('inputs/day6') as f:
    sequence = f.read().rstrip()

for seq_length in (4, 14):
    for i in range(len(sequence)-seq_length):
        if len(set(sequence[i:i+seq_length])) == seq_length:
            print(i+seq_length)
            break
