""" Advent of Code Day 8 """


class Interpreter:
    def __init__(self):
        self.accumulator = 0
        self.index = 0
        self.instructions = None

    def nop(self, num):
        self.index += 1

    def jmp(self, num):
        self.index += num

    def acc(self, num):
        self.accumulator += num
        self.index += 1

    def reset(self):
        self.index = 0
        self.accumulator = 0

    def load_instructions(self, input_file):
        self.instructions = []
        with open(input_file, "r") as f:
            for line in f:
                lsplit = line.split()
                self.instructions.append((lsplit[0], int(lsplit[1])))

    def execute(self):
        visited = []
        success = True
        try:
            while True:
                if self.index in visited:
                    success = False
                    break
                elif self.index == len(self.instructions):
                    break

                visited.append(self.index)
                self._execute_next()
        except IndexError as e:
            success = False
        return success

    def _execute_next(self):
        name, num = self.instructions[self.index]
        getattr(self, name)(num)

    def substitute(self, at_index, rule):
        inst = self.instructions[at_index]
        self.instructions[at_index] = rule(inst)


if __name__ == "__main__":

    interp = Interpreter()
    interp.load_instructions("./input_day8.txt")

    # Part I
    interp.execute()
    print(interp.accumulator)

    # Part II
    def rule(inst):
        subs = {"jmp": "nop", "nop": "jmp"}
        return subs.get(inst[0], inst[0]), inst[1]

    # find the corrupted instruction
    for ind in range(len(interp.instructions)):
        interp.substitute(ind, rule)
        success = interp.execute()
        if success:
            break
        interp.substitute(ind, rule)
        interp.reset()
    else:
        print("Repair unsuccessful")

    print(interp.accumulator)
