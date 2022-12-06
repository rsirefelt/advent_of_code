
points = 0
with open("input") as f:
    for i in f:
        b, a = ord(i[0]) - 64, ord(i[2]) - 87
        points += a

        if (a - b == 0):
            points += 3
        elif (a > 1 and a - b == 1):
            points += 6
        elif (a == 1 and a - b == -2):
            points += 6

print(points)
