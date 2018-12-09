with open('input.txt') as f:
    lines = f.readlines() 
    
for k in range(len(lines)):
    lines[k] = lines[k].strip()

xStart = []
yStart = []
widths = []
heights = []
# Find the maximum width and height 
maxX = 0
maxY = 0
for line in lines: 
    strs = line.split(' ')

    width, height = strs[3].split('x')
    width = int(width)
    height = int(height)

    x, y = strs[2].split(',')
    x = int(x)
    y = int(y[:-1])

    xStart.append(x)
    yStart.append(y)
    widths.append(width)
    heights.append(height)
    
    maxX = max([x+width, maxX])
    maxY = max([y+height, maxY])

# Now loop over all squares and check how many overlap 
#numOverlappingSquares = 0
#for x in range(maxX):
#    for y in range(maxY):
#        numOccurences = 0
#        for k in range(len(lines)):
#            if (x >= xStart[k] and x < xStart[k] + widths[k]):
#                if (y >= yStart[k] and y < yStart[k] + heights[k]):
#                    numOccurences += 1
#        if (numOccurences > 1):
#            numOverlappingSquares += 1

#print(numOverlappingSquares)

def checkIfClaimsOverlap(index1, index2, xStart, yStart, widths, heights): 
    for x in range(xStart[index1], xStart[index1] + widths[index1]):
        for y in range(yStart[index1], yStart[index1] + heights[index1]):
            if (x >= xStart[index2] and x < xStart[index2] + widths[index2]):
                if (y >= yStart[index2] and y < yStart[index2] + heights[index2]):
                    return True
    return False 

for k in range(len(lines)):
    overlapsAnything = False
    for kk in range(len(lines)):
        if (k == kk):
            continue
        if checkIfClaimsOverlap(k, kk, xStart, yStart, widths, heights):
            overlapsAnything = True
            break
    if (overlapsAnything == False):
        print(k)

