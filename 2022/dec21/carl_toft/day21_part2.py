def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

monkeys = parseInput("input.txt")
monkeys = [monkey.replace(': ', '=') for monkey in monkeys]

done = False
loop_iter = 0
solved_vars = set()
while not done:
    loop_iter = loop_iter + 1
    print(loop_iter)
    done = True
    did_anything = False
    for monkey in monkeys:
        try:
            curr_var = monkey.split("=")[0]
            if curr_var == "humn":
                continue
            exec(monkey)
            if curr_var not in solved_vars:
                solved_vars.add(curr_var)
                did_anything = True
        except:
            done = False
    if not did_anything:
        break

variables = locals()

variables["hppd"] = variables["czdp"]
done = False
curr_variable = "hppd"
while not done:
    # Find where current variable is used
    for monkey in monkeys:
        if monkey.split("=")[0] == curr_variable:
            vars = monkey.split("=")[1].split(" ")
            operator = vars[1]
            var1 = vars[0]
            var2 = vars[2]
            break

    if var1 not in variables:
        if operator == "+":
            variables[var1] = variables[curr_variable] - variables[var2]
        elif operator == "-":
            variables[var1] = variables[curr_variable] + variables[var2]
        elif operator == "*":
            variables[var1] = variables[curr_variable] / variables[var2]
        elif operator == "/":
            variables[var1] = variables[curr_variable] * variables[var2]
        else:
            assert False, "We should never get here!"
        curr_variable = var1
    if var2 not in variables:
        if operator == "+":
            variables[var2] = variables[curr_variable] - variables[var1]
        elif operator == "-":
            variables[var2] = variables[var1] - variables[curr_variable]
        elif operator == "*":
            variables[var2] = variables[curr_variable] / variables[var1]
        elif operator == "/":
            variables[var2] = variables[var1] / variables[curr_variable]
        else:
            assert False, "We should never get here!"
        curr_variable = var2
    print("Solved " + curr_variable + " = " + str(variables[curr_variable]))

    if curr_variable == "humn":
        print("Part 2: " + str(variables[curr_variable]))
        break

# Unroll the calculation from the root

#if int(hppd) == int(czdp):
#    #if int(pppw) == int(sjmn):
#    print("Part 2: " + str(humn))

xxx = 3