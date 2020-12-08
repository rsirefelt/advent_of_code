def read_instructions(filename):
    instructions = []

    with open(filename, 'r') as f:
        data_lines = f.readlines()

        for string in data_lines:
            instruction_value = string.split()
            instructions.append((instruction_value[0], int(instruction_value[1])))

    return instructions

def loop_instructions(instructions, num_instructions):
    current_ind = 0
    accumelator = 0
    visited_ind = set()

    while True:
        if current_ind in visited_ind:
            return (accumelator, False)
        elif current_ind == num_instructions:
            return (accumelator, True)
        else:
            visited_ind.add(current_ind)
            if instructions[current_ind][0] == 'nop':
                current_ind +=1
            elif instructions[current_ind][0] == 'acc':
                accumelator += instructions[current_ind][1]
                current_ind +=1
            elif instructions[current_ind][0] == 'jmp':
                current_ind += instructions[current_ind][1]


def fix_instructions(instructions):
    num_instructions = len(instructions)
    for instruction_ind in range(num_instructions):
        if instructions[instruction_ind][0] == 'nop':
            instructions[instruction_ind] = ('jmp', instructions[instruction_ind][1])
            (accumelator, completed) = loop_instructions(instructions, num_instructions)
            if not completed:
                instructions[instruction_ind] = ('nop', instructions[instruction_ind][1])
            else:
                return accumelator
        elif instructions[instruction_ind][0] == 'jmp':
            instructions[instruction_ind] = ('nop', instructions[instruction_ind][1])
            (accumelator, completed) = loop_instructions(instructions, num_instructions)
            if not completed:
                instructions[instruction_ind] = ('jmp', instructions[instruction_ind][1])
            else:
                return accumelator
    print('None change worked!')

def main():
    instructions = read_instructions('testdata.csv')
    instructions = read_instructions('data.csv')
    
    #Part 1
    num_instructions = len(instructions)
    (accumelator, _) = loop_instructions(instructions, num_instructions)
    print('Part1, when reaching the infinity loop is the output accumelator value: %i' %accumelator)


    #Part2
    accumelator = fix_instructions(instructions)
    print('Part2, After the fix is the output accumelator value: %i' %accumelator)


if __name__ == "__main__": main()