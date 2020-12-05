with open("input.txt", "r") as f:
    seats = f.read().translate(str.maketrans({"B": "1", "F": "0", "R": "1", "L": "0"}))
occ_seats = set(int(s, 2) for s in seats.split("\n"))
all_seats = set(x for x in range(list(occ_seats)[0], list(occ_seats)[-1] + 1))
print(f"1) Maximum seat id: {list(occ_seats)[-1]}")
print(f"2) Correct seat id: {(all_seats - occ_seats).pop()}")
