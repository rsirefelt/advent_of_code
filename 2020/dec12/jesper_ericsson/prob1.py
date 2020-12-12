import re
import numpy as np

regex_instructions = re.compile(r'([NSEWLRF])([0-9]*)')

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
    heading = 0
    nort_south = 0
    east_west = 0

    for instruction in instructions:
        
        if instruction[0] == 'N':
            nort_south += instruction[1]
        elif instruction[0] == 'S':
            nort_south -= instruction[1]
        elif instruction[0] == 'E':
            east_west += instruction[1]
        elif instruction[0] == 'W':
            east_west -= instruction[1]
        elif instruction[0] == 'R':
            heading = (heading - instruction[1])%360
        elif instruction[0] == 'L':
            heading = (heading + instruction[1])%360
        elif instruction[0] == 'F':
            if heading == 0:
                east_west += instruction[1]
            elif heading == 90:
                nort_south += instruction[1]
            elif heading == 180:
                east_west -= instruction[1]
            elif heading == 270:
                nort_south -= instruction[1]
    
    return abs(nort_south) + abs(east_west)

def loop_instructions2(instructions):
    nort_south = 0
    east_west = 0
    waypoint =np.array([10,1])

    for instruction in instructions:
        
        if instruction[0] == 'N':
            waypoint[1] += instruction[1]
        elif instruction[0] == 'S':
            waypoint[1] -= instruction[1]
        elif instruction[0] == 'E':
            waypoint[0] += instruction[1]
        elif instruction[0] == 'W':
            waypoint[0] -= instruction[1]
        elif instruction[0] == 'R':
            theta = np.radians(-instruction[1])
            r = np.array(( (np.cos(theta), -np.sin(theta)),
                        (np.sin(theta),  np.cos(theta)) ))

            waypoint = r.dot(waypoint)
        elif instruction[0] == 'L':
            theta = np.radians(instruction[1])
            r = np.array(( (np.cos(theta), -np.sin(theta)),
                        (np.sin(theta),  np.cos(theta)) ))

            waypoint = r.dot(waypoint)
        elif instruction[0] == 'F':
            nort_south +=  waypoint[1] * instruction[1]
            east_west +=  waypoint[0] * instruction[1]

    
    return round(abs(nort_south) + abs(east_west))

def main():
    instructions = read_instructions('testdata.csv')
    instructions = read_instructions('data.csv')

    # Part 1
    distance_1 = loop_instructions1(instructions)
    print('Part1, The manhatan distance is: %i' %distance_1)

    # Part2
    distance_2 = loop_instructions2(instructions)
    print('Part2, The manhatan distance is: %i' %distance_2)


if __name__ == "__main__": main()