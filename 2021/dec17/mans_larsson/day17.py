target_area = (241, 275, -75, -49)


def evaluate_initial_velocity(dx, dy):
    posx = 0
    posy = 0
    max_posy = -100
    while posx <= target_area[1] and posy >= target_area[2]:
        posx += dx
        posy += dy

        dy -= 1
        dx = max(0, dx - 1)

        if posy > max_posy:
            max_posy = posy

        if posx >= target_area[0] and posx <= target_area[1] and posy >= target_area[2] and posy <= target_area[3]:
            return max_posy
    return -100


any_max_y = -100
count = 0
for dx in range(1, target_area[1] + 1):
    for dy in range(target_area[2]-1, 100):
        max_y = evaluate_initial_velocity(dx, dy)
        if max_y > -100:
            count += 1
        if max_y > any_max_y:
            any_max_y = max_y

print(any_max_y)
print(count)
