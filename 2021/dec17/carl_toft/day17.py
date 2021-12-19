import numpy as np

# Define target area
#x_min = 20
#x_max = 30
#y_min = -10
#y_max = -5
x_min = 185
x_max = 221
y_min = -122
y_max = -74

def doesItHit(v_x, v_y, x_min, x_max, y_min, y_max):
    x = 0
    y = 0

    done = False
    maximal_height = 0
    while not done:
        x = x + v_x
        y = y + v_y
        if v_x > 0:
            v_x = v_x - 1
        if v_x < 0:
            v_x = v_x + 1
        v_y = v_y - 1

        if y > maximal_height:
            maximal_height = y

        # Check if we are done
        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            return maximal_height

        # Probe has fallen below the target area
        if y < y_min:
            return None

        if x > x_max:
            return None

num_possible_velocities = 0
max_height = 0
for v_x in range(0,x_max+1):
    print(v_x)
    for v_y in range(y_min-1, 400):
        maximal_height = doesItHit(v_x, v_y, x_min, x_max, y_min, y_max)
        if maximal_height is not None:
            num_possible_velocities = num_possible_velocities + 1
            if maximal_height > max_height:
                max_height = maximal_height
                best_vx = v_x
                best_vy = v_y

print("Part 1:", max_height)
print("Part 2:", num_possible_velocities)













