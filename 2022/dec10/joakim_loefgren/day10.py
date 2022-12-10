with open('./input.txt') as f:
    lines = iter(f.read().splitlines())

X = 1
cycle = 0
executing = 0
inc = 0
signal = []
image = ''
pixel = 0
try:
    while True:
        cycle += 1
        if executing == 0:
            if inc:
                X += inc
                inc = 0
            instr = next(lines)
            if instr != 'noop':
                inc = int(instr.split()[1])
                executing += 1
        else:
            executing -= 1

        if cycle == 20 or (cycle - 20) % 40 == 0:
            signal.append(cycle*X)

        pixel = (cycle - 1) % 40
        if cycle > 1 and pixel == 0:
            image += '\n'
        if pixel in [X - 1, X, X + 1]:
            image += '#'
        else:
            image += '.'
except StopIteration:
    pass

# part I
print(sum(signal))

# part II
print(image)
