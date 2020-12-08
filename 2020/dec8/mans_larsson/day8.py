import numpy as np


ops = []
with open('inputs/day8') as f:
    for line in f:
        op, num = line.rstrip().split(' ')
        ops.append((op, int(num)))


def execute_instructions(operators):
    exec = np.zeros(len(operators), dtype=np.bool)
    acc = 0
    ptr = 0
    deadlock = True
    while True:
        exec[ptr] = True
        op, num = operators[ptr]
        if op == 'nop':
            ptr += 1
        elif op == 'acc':
            ptr += 1
            acc += num
        elif op == 'jmp':
            ptr += num
        else:
            raise RuntimeError('invalid operator')
        if ptr >= len(operators):
            deadlock = False
            break
        if exec[ptr]:
            break

    return acc, deadlock


acc, _ = execute_instructions(ops)
print(f'a) {acc}')

for ind in range(len(ops)):
    ops_copy = ops.copy()
    if ops_copy[ind][0] == 'nop':
        ops_copy[ind] = ('jmp', ops_copy[ind][1])
    elif ops_copy[ind][0] == 'jmp':
        ops_copy[ind] = ('nop', ops_copy[ind][1])

    acc, deadlock = execute_instructions(ops_copy)

    if not deadlock:
        break

print(f'b) {acc}')
