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

def apply_mask(in_mem, mask, current_string, bit_ind, mem_list):
    if bit_ind == 36:
        return [current_string]

    if mask[bit_ind] == '0':
        current_string += in_mem[bit_ind]
        bit_ind += 1
        mem_list.extend(apply_mask(in_mem, mask, current_string, bit_ind,[]))
        return mem_list
    elif mask[bit_ind] == '1':
        current_string += '1'
        bit_ind += 1
        mem_list.extend(apply_mask(in_mem, mask, current_string, bit_ind,[]))
        return mem_list
    elif mask[bit_ind] == 'X':
        bit_ind += 1
        mem_list.extend(apply_mask(in_mem, mask, current_string + '0', bit_ind,[]))
        mem_list.extend(apply_mask(in_mem, mask, current_string + '1', bit_ind,[]))
        return mem_list

def run_program(program):
    memory = {}
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for program_row in program:
        if program_row[0] == 'mask':
            current_mask = program_row[1]
        else:
            bin_mem = f'{int(program_row[0]):036b}'
            mem_list = apply_mask(bin_mem, current_mask,'', 0,[])

            for mem in mem_list:
                memory_key = int(mem, 2)
                memory[memory_key] = int(program_row[1])

    return sum(memory.values())

def main():
    program = read_program('testdata.csv')
    program = read_program('data.csv')

    # Part 2
    memory_sum = run_program(program)
    print('The memory sum is: %i' %memory_sum)


if __name__ == "__main__": main()