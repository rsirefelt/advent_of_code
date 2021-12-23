import numpy as np
import matplotlib.pyplot as plt


def check_hit(v, box, num_steps=50):
    times = np.arange(0, num_steps)
    x = np.zeros((2, len(times)), dtype=int)
    v = np.asarray(v)
    hit = [False, False]
    for t in times[:-1]:
        x[0, t + 1] = x[0, t] + max(v[0] - t, 0)
        x[1, t + 1] = x[1, t] + (v[1] - t)
        hit[0] = box[0, 0] <= x[0, t + 1] <= box[0, 1]
        hit[1] = box[1, 0] <= x[1, t + 1] <= box[1, 1]
        if all(hit):
            break
    return hit


if __name__ == '__main__':
    # example data 
    box = np.array([[20, 30], [-10, -5]])

    # Part I: bruteforce search like:
    for v_y in range(1, 30):
        hit = check_hit([6, v_y], box, num_steps=30)
        if all(hit):
            print(f'y-pos: {v_y * (v_y + 1) // 2}')
            

    # Part II: bruteforce search like:
    count = 0
    for v_y in range(-30, 30):
        for v_x in range(1, 30):
            hit = check_hit([v_x, v_y], box, num_steps=300)
            if all(hit):
                count += 1
    print(count)
