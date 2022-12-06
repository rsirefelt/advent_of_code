from collections import deque

with open('./input.txt', 'r') as f:
    data = f.read().strip()
    
maxlen = 14  # use 4 for part I
window = deque(maxlen=maxlen)
for c in data[:maxlen - 1]:
    window.append(ord(c))

stop = None
for i, c in enumerate(data[maxlen - 1:]):
    window.append(ord(c))
    if len(set(window)) == maxlen:
        stop = i + maxlen
        break
        
print(stop)
