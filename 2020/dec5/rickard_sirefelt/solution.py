with open("input.txt", "r") as f:
    seats = f.read().translate(str.maketrans({"B": "1", "F": "0", "R": "1", "L": "0"}))

occ_seats = set(int(s, 2) for s in seats.split("\n"))
occ_seats_l = list(occ_seats)
all_seats = {x for x in range(occ_seats_l[0], occ_seats_l[-1] + 1)}

print(f"1) Maximum seat id: {occ_seats_l[-1]}")
print(f"2) Correct seat id: {(all_seats - occ_seats).pop()}")
