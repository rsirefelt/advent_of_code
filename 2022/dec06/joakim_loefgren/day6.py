from collections import deque

# O(maxlen) in memory for fun
maxlen = 4  # use 4 for part I
window = deque(maxlen=maxlen)

stop = None
with open('./input.txt', 'r') as f:
    i = 1
    while True:
        c = f.read(1)  # assume 1 byte/char encoding
        if not c:
            break

        window.append(ord(c))
        if len(set(window)) == maxlen:
            break

        i += 1

print(i)
