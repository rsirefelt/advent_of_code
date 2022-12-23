def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def checkHumn(monkeys, humn):
    done = False
    lclcs = locals()
    while not done:
        done = True
        for monkey in monkeys:
            try:
                if "humn" in monkey.split("=")[0]:
                    continue
                exec(monkey, globals(), lclcs)
            except:
                done = False
    if int(pppw) == int(sjmn):
        return True
    else:
        return False

monkeys = parseInput("test_input.txt")
monkeys = [monkey.replace(': ', '=') for monkey in monkeys]

for humn in range(1000000):
    if checkHumn(monkeys, humn):
        print("Part 2: " + str(humn))
        break
xxx = 3

#print("Part 1: " + str(root))
#xxx = 3