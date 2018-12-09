import numpy as np 

# Read the input 
with open('input.txt') as f:
    lines = f.readlines()

for k in range(len(lines)):
    lines[k] = lines[k].strip()

# Sort the input into chronological order
timestamps = []
for line in lines:
    strs = line.split(']')
    tmp = strs[0]
    timestamps.append(tmp[1:5] + tmp[6:8] + tmp[9:11] + tmp[12:14] + tmp[15:17])

sortedPermutation = sorted(range(len(timestamps)), key=lambda k: timestamps[k])

sortedLines = []
for k in range(len(sortedPermutation)):
    sortedLines.append(lines[sortedPermutation[k]]) 

# Create a dictionary for all guards
guards = {} 

currGuard = -1 
currTime = -1
for line in sortedLines:
    strs = line.split(' ')
    # Find the new time 
    if strs[1][0:2] == '23':
        newTime = 0
    else:
        newTime = int(strs[1][3:5])
    
    # Initialize currTime if necessary 
    if currTime == -1:
        currTime = newTime 

    if ('begins shift' in line):
        # Set awake time for the previous guard
        if currGuard != -1:
            guards[currGuard][-1,currTime:60] = isAsleep

        currGuard = int(strs[3][1:])
        isAsleep = 0

        if not currGuard in guards:
            guards[currGuard] = np.zeros((1,60))
        else:
            guards[currGuard] = np.concatenate((guards[currGuard], np.zeros((1,60))), axis=0)
        # The line says either that the current guard falls asleep or wakes up 
        # strs = line.split(' ')
    else: 
        # The current line is that a guard either wakes up or falls asleep
        guards[currGuard][-1,currTime:newTime] = isAsleep
        if 'wakes up' in line:
            isAsleep = 0
        elif 'falls asleep' in line:
            isAsleep = 1
        currTime = newTime 

# Find the guard with the most sleep time 
sleepMinutes = {} 
totalSleep = {}
maxSleep = 0
mostSleepyMinute = 0
sleepOnMostSleepyMinute = 0
for key in guards.keys():
    sleepMinutes[key] = np.sum(guards[key],axis=0)
    totalSleep[key] = np.sum(sleepMinutes[key])

    if (np.max(sleepMinutes[key]) > sleepOnMostSleepyMinute):
        sleepOnMostSleepyMinute = np.max(sleepMinutes[key])
        mostSleepyMinute = np.argmax(sleepMinutes[key], axis=0)
        sleepyMinuteGuardIndex = key 

    if (totalSleep[key] > maxSleep):
        maxSleep = totalSleep[key]
        guardIndex = key

minuteIndex = np.argmax(sleepMinutes[guardIndex], axis=0)

print(guardIndex, minuteIndex)
print(sleepyMinuteGuardIndex, mostSleepyMinute)