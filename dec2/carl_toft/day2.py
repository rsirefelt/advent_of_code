with open('input.txt') as f:
    lines = f.readlines()

for k in range(len(lines)):
    lines[k] = lines[k][0:-1]

## PART 1 ##
numTwos = 0
numThrees = 0
for line in lines:
    twoAppears = False
    threeAppears = False 
    for char in line:
        count = line.count(char)
        if count == 2:
            twoAppears = True
        if count == 3:
            threeAppears = True
    
    if (twoAppears == True): 
        numTwos += 1
    if (threeAppears == True):
        numThrees += 1

print(numTwos*numThrees)

## PART 2 ## 
def checkBoxPair(str1, str2):
    numMismatches = 0
    for k in range(len(str1)):
        if (str1[k] != str2[k]):
            numMismatches += 1
    if (numMismatches == 1):
        return True
    else:
        return False

for k in range(len(lines)):
    for kk in range(len(lines)):
        if (k == kk):
            continue
        foundPair = checkBoxPair(lines[k], lines[kk])
        if (foundPair == True): 
            print(lines[k] + ' ' + lines[kk])
