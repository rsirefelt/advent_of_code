import numpy as np 

def getDists(coords, point):
    dists = np.sum(np.abs(coords-point), axis=1)
    minVal = int(np.min(dists))
    minIndex = np.argmin(dists)
    numMinVals = 0
    for k in range(coords.shape[0]):
        if (int(dists[k]) == minVal):
            numMinVals += 1
    if (numMinVals > 1):
        return -1
    else:
        return minIndex

def getAreas(coords, xMin, xMax, yMin, yMax):
    scores = np.zeros(coords.shape[0])
    for x in range(xMin, xMax):
        for y in range(yMin, yMax):
            point = np.array([[x,y]])
            closestInd = getDists(coords, np.array([[x,y]]))
            if (closestInd != -1):
                scores[closestInd] += 1
    return scores

def isSafe(coords, point):
    dists = np.sum(np.abs(coords-point), axis=1)
    if np.sum(dists) < 10000:
        return True
    else:
        return False 

coords = np.zeros((0,2))
# Load input 
with open('input.txt') as f: 
    lines = f.readlines()

for k in range(len(lines)):
    str = lines[k].strip() 
    strs = str.split(', ')
    currPoint = np.array([[int(strs[0]), int(strs[1])]])
    coords = np.concatenate((coords, currPoint), axis=0)

# Part 1 

''' # Find areas 
xMax = 1.5*np.max(coords[:,0])
xMax = int(xMax)
yMax = 1.5*np.max(coords[:,1])
yMax = int(yMax)
scores = getAreas(coords, -xMax, xMax, -yMax, yMax)

isInfinite = []
xMax = xMax*2
yMax = yMax*2
newScores = getAreas(coords, -xMax, xMax, -yMax, yMax)
for k in range(len(newScores)):
    if (newScores[k] != scores[k]):
        isInfinite.append(True)
    else:
        isInfinite.append(False)

finiteScores = []
for k in range(len(scores)):
    if not isInfinite[k]:
        finiteScores.append(newScores[k])

maxArea = max(finiteScores)
print(maxArea) '''

# Part 2
xMax = 1.5*np.max(coords[:,0])
xMax = int(xMax)
yMax = 1.5*np.max(coords[:,1])
yMax = int(yMax)

numSafe = 0
for x in range(-xMax, xMax):
    for y in range(-yMax, yMax):
        if isSafe(coords, np.array([[x,y]])):
            numSafe += 1

print(numSafe)