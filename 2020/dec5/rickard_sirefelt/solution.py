with open("input.txt", "r") as f:
    seats = f.read().translate(str.maketrans({"B": "1", "F": "0", "R": "1", "L": "0"}))

min_id, max_id = 2 ** 10, 0
occ_seats = set()
for s in seats.split("\n"):
    s_id = int(s, 2)
    occ_seats.add(s_id)

    if s_id > max_id:
        max_id = s_id
    if s_id < min_id:
        min_id = s_id

all_seats = {x for x in range(min_id, max_id + 1)}
correct_seat = all_seats - occ_seats

print(f"1) Maximum seat id: {max_id}")
print(f"2) Correct seat id: {correct_seat.pop()}")
