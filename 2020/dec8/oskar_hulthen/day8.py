import regex as re


def task(instructions):
    num_instructions = len(instructions)
    used_instruction_idx = []

    repeated = False
    current_op_idx = 0
    accumulator = 0

    while not repeated:
        if current_op_idx == num_instructions:
            break

        instruction, idx_op = instructions[current_op_idx]
        used_instruction_idx.append(current_op_idx)

        if instruction == "nop":
            current_op_idx += 1
        elif instruction == "acc":
            current_op_idx += 1
            accumulator += idx_op
        elif instruction == "jmp":
            current_op_idx += idx_op

        if current_op_idx in used_instruction_idx:
            repeated = True

    return accumulator, repeated


def task2(instructions):
    for idx, (instruction, idx_op) in enumerate(instructions):
        if instruction == "nop":
            new_instruction = "jmp"
        elif instruction == "jmp":
            new_instruction = "nop"
        else:
            continue
        current_instructions = instructions.copy()
        current_instructions[idx] = (new_instruction, idx_op)
        accumulator, repeated = task(current_instructions)
        if repeated == False:
            return accumulator


if __name__ == "__main__":
    instructions = []
    with open("input") as f:
        lines = list(f.readlines())
        for line in lines:
            instruction, idx_op = line.split()
            instructions.append((instruction, int(idx_op)))

    print(task(instructions)[0])
    print(task2(instructions))
