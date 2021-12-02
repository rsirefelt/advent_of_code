import re

regex_instructions = re.compile(r'([a-z]*) ([0-9]*)')

def read_instructions(filename):
    instructions = []

    with open(filename, 'r') as f:
        data_lines = f.readlines()

        for string in data_lines:
            instruction = regex_instructions.findall(string)
            # print(instruction)
            instructions.append((instruction[0][0], int(instruction[0][1])))

    return instructions

def loop_instructions1(instructions):
    length = 0
    depth = 0

    for instruction in instructions:
        
        if instruction[0] == 'forward':
            length += instruction[1]
        elif instruction[0] == 'down':
            depth += instruction[1]
        elif instruction[0] == 'up':
            depth -= instruction[1]

    return length * depth

def loop_instructions2(instructions):
    length = 0
    aim = 0
    depth = 0

    for instruction in instructions:
        
        if instruction[0] == 'forward':
            length += instruction[1]
            depth += (aim * instruction[1])
        elif instruction[0] == 'down':
            aim += instruction[1]
        elif instruction[0] == 'up':
            aim -= instruction[1]

    return length * depth
def main():
    instructions = read_instructions('testdata.csv')
    instructions = read_instructions('data.csv')

    # Part 1
    distance_1 = loop_instructions1(instructions)
    print('Part1, The product is: %i' %distance_1)

    # Part 2
    distance_2 = loop_instructions2(instructions)
    print('Part2, The product is: %i' %distance_2)
            

if __name__ == "__main__": main()
	
