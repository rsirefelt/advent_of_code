def decode_boarding_pass(boarding_pass):

    row = 0
    for pow, pos in enumerate(range(6, -1, -1)):
        if boarding_pass[pos] == 'B':
            row += 2**pow

    column = 0
    for pow, pos in enumerate(range(9, 6, -1)):
        if boarding_pass[pos] == 'R':
            column += 2**pow
    return row, column, row*8+column


max_id = 0
ids = []
with open('inputs/day5') as f:
    for line in f:
        _, _, id = decode_boarding_pass(line.rstrip())
        ids.append(id)
        if id > max_id:
            max_id = id

print(f'max id {max_id}')

sorted_ids = sorted(ids)
my_id = None
for i in range(1, len(sorted_ids)-1):
    if sorted_ids[i+1] - sorted_ids[i] == 2:
        my_id = sorted_ids[i] + 1
        break

print(f'my id {my_id}')
