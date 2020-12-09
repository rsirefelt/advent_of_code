import numpy as np

msg = np.loadtxt("input.txt", dtype=np.int32)

# Part 1
invalid_num, i_invalid_num = -1, -1
for i in range(25, len(msg)):
    found = False
    for j in range(1, 26):
        diff = msg[i] - msg[i - j]
        if np.where(msg[i - 25 : i + 1] == diff)[0].size > 0:
            found = True
            break
    if not found:
        i_invalid_num = i
        invalid_num = msg[i]
        break

# Part 2
i_low = 0
i_high = 1
while True:
    sum_ = np.sum(msg[i_low : i_high + 1])
    if sum_ == invalid_num:
        break
    elif sum_ < invalid_num:
        i_high += 1
    elif sum_ > invalid_num:
        i_low += 1
encryption_weakness = msg[i_low] + msg[i_high]

print(f"1) Breaking number is {invalid_num}")
print(f"2) Encryption weakness is {encryption_weakness}")
