import numpy as np
import re

regex_mask = re.compile(r'(mask) = ([01X]{36})')
regex_mem = re.compile(r'mem\[([0-9]*)\] = ([0-9]*)')

def read_program(filename):
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        program = []
        for string in data_lines:
            mask = regex_mask.findall(string)
            if mask:
                program.append((mask[0][0], mask[0][1]))
            mem = regex_mem.findall(string)
            if mem:
                program.append((mem[0][0], mem[0][1]))

    return program

def apply_mask(number, mask):
    bin_num = f'{number:036b}'
    new_bin_num = ''
    for ind, mask_value in enumerate(mask):
        if mask_value == '0' or mask_value == '1':
            new_bin_num += mask_value
        else:
            new_bin_num += bin_num[ind]
    return int(new_bin_num, 2)



def run_program(program):
    memory = {}
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for program_row in program:
        if program_row[0] == 'mask':
            current_mask = program_row[1]
        else:
            masked_num = apply_mask(int(program_row[1]), current_mask)
            memory[program_row[0]] = masked_num

    return sum(memory.values())

def main():
    program = read_program('testdata.csv')
    program = read_program('data.csv')

    # Part 1
    memory_sum = run_program(program)
    print('The memory sum is: %i' %memory_sum)



if __name__ == "__main__": main()