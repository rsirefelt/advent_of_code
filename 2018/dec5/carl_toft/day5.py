def reactPolymer(polymer): 
    # Define patterns to remove 
    toRemove = []
    for k in range(26):
        toRemove.append(chr(97+k) + chr(65+k))
        toRemove.append(chr(65+k) + chr(97+k))

    shouldContinue = True
    while shouldContinue:
        shouldContinue = False
        for str in toRemove:
            currLen = len(polymer)
            polymer = polymer.replace(str, '')
            newLen = len(polymer)

            if (currLen != newLen):
                shouldContinue = True
    
    return polymer

# Read input 
with open('input.txt') as f:
    lines = f.readlines()

line = lines[0].strip()

# Part 1
line = reactPolymer(line)

print(line)
print(len(line))

# Part 2
lens = []
for k in range(0,26):
    polymer = line.replace(chr(k+97), '')
    polymer = polymer.replace(chr(k+65), '')
    polymer = reactPolymer(polymer)
    lens.append(len(polymer))

print(lens)
print(min(lens))
