import numpy as np

with open("input.txt", "r") as f:
    instructions_txt = (
        f.read()
        .replace("acc", "0")
        .replace("nop", "-1")
        .replace("jmp", "1")
        .split("\n")
    )

instructions = np.zeros((len(instructions_txt), 2), np.int32)


for idx, instruction_txt in enumerate(instructions_txt):
    instructions[idx, 0] = int(instruction_txt.split()[0])
    instructions[idx, 1] = int(instruction_txt.split()[1])

idx_to_flip = [-1] + list(np.argwhere(abs(instructions[:, 0]) > 0).squeeze())
flipped_idx = set()
correct_break = False
accumulator = [0, 0]
for idx in idx_to_flip:
    flip_instructions = instructions.copy()
    if idx != -1:
        flip_instructions[idx, 0] *= -1
    passed_idx = set()
    curr_accumulator, curr_idx = 0, 0
    while True:
        if curr_idx in passed_idx or curr_idx > len(instructions):
            break
        elif curr_idx == len(instructions):
            correct_break = True
            break

        passed_idx.add(curr_idx)
        if flip_instructions[curr_idx, 0] == 0:
            curr_accumulator += flip_instructions[curr_idx, 1]
            curr_idx += 1
        elif flip_instructions[curr_idx, 0] == 1:
            curr_idx += flip_instructions[curr_idx, 1]
        else:
            curr_idx += 1

    if idx == -1:
        accumulator[0] = curr_accumulator
    if correct_break:
        accumulator[1] = curr_accumulator
        break

print(f"1): Accumulator: {accumulator[0]}")
print(f"2): Accumulator: {accumulator[1]}")
