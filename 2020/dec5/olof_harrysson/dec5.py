import itertools

with open("input.txt") as f:
  lines = f.read().replace("F", "0").replace("B", "1")
  lines = lines.replace("L", "0").replace("R", "1")
  lines = lines.splitlines()

max_seat_id = 0
seats = {}
for line in lines:
  row = int(line[:-3], 2)
  col = int(line[-3:], 2)
  seat_id = row * 8 + col
  if seat_id > max_seat_id:
    max_seat_id = seat_id
  seats[(row, col)] = True

# print(max_seat_id)

for row, col in itertools.product(range(128), range(8)):
  if not (row, col) in seats:
    seat_id = row * 8 + col
    print(row, col, seat_id)
