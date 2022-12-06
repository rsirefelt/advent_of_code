
points = 0
with open("input") as f:
    for i in f:
        b, a = ord(i[0]) - 64, ord(i[2]) - 87
        points += (a - 1) * 3

        if (a == 2):
            points += b
        elif (a == 1):
            if (b == 1):
                points += 3
            else:
                points += b - 1
        elif (a == 3):
            if (b == 3):
                points += 1
            else:
                points += b + 1

print(points)
