import numpy as np

lows = []
highs = []
letters = []
passwords = []
with open('inputs/day2') as f:
    for line in f:
        content = line.rstrip().split(' ')
        letters.append(content[1][0])
        passwords.append(content[2])
        highlow = content[0].split('-')
        lows.append(int(highlow[0]))
        highs.append(int(highlow[1]))

lows = np.array(lows)
highs = np.array(highs)

# a)
count = 0
for low, high, letter, password in zip(lows, highs, letters, passwords):
    occurences = password.count(letter)
    if occurences >= low and occurences <= high:
        count += 1
print(f'a) Valid passwords {count}')

# b)
count = 0
for low, high, letter, password in zip(lows, highs, letters, passwords):
    if (password[low - 1] == letter) != (password[high - 1] == letter):
        count += 1
print(f'b) Valid passwords {count}')
