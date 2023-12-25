from functools import cache

@cache
def checkFullPattern(currentPattern, instructions):

    if len(instructions) == 0:
        if "#" in currentPattern:
            return 0
        else:
            return 1
    
    if len(currentPattern) == 0:
        if len(instructions) > 0:
            return 0
        else:
            return 1

    combinations = 0

    if currentPattern[0] in "?.":
        combinations += checkFullPattern(currentPattern[1:], instructions)

    if currentPattern[0] in "?#":
        if instructions[0] <= len(currentPattern):
            if "." not in currentPattern[:instructions[0]]:
                if instructions[0] == len(currentPattern) or currentPattern[instructions[0]] != "#":
                    combinations += checkFullPattern(currentPattern[instructions[0] + 1:], instructions[1:])

    return combinations


if __name__ == '__main__':

    f=open("Task12.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.split(" ")
        theInput.append(i)
    f.close()

    totalValid = 0

    for thisIndex, i in enumerate(theInput):

        spring = i[0] + "?" + i[0] + "?" + i[0] + "?" + i[0] + "?" + i[0]

        instructions = i[1].split(",")

        for j in range(0, len(instructions)):
            instructions[j] = int(instructions[j])

        instructionsOrig = instructions.copy()

        instructions.extend(instructionsOrig)
        instructions.extend(instructionsOrig)
        instructions.extend(instructionsOrig)
        instructions.extend(instructionsOrig)

        instructions = tuple(instructions)

        thisValue = checkFullPattern(spring, instructions)
        totalValid += thisValue

    print(totalValid)
