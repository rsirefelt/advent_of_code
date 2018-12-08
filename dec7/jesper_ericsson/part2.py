import numpy as np

def getAvailableSteps(allSteps, dependsOn):
    availableSteps =[]       
    for step in allSteps:
        if step not in dependsOn:
            availableSteps.append(step)
    availableSteps.sort()
    return availableSteps
    
def addToWorkers(allSteps, timeLeft, availableSteps, availableWorkers):
    for step in availableSteps:
        if availableWorkers > 0:
            timeLeft[step] = ord(step) - 4
            availableWorkers -= 1
            allSteps.remove(step)
        else:
            break
    return availableWorkers
            
def updateTime(timeLeft, availableWorkers):
    stepsDone = []
    for worker in timeLeft:
        timeLeft[worker] -= 1
        if timeLeft[worker] == 0:
            stepsDone.append(worker)
            availableWorkers += 1
    for step in stepsDone:
        del timeLeft[step]
            
    return stepsDone, availableWorkers
        
def removeDependencies(dependsOff, dependsOn, doneSteps):
    if len(dependsOn) > 0:
        for currentStep in doneSteps: 
            for step in dependsOff[currentStep]:
                dependsOn[step].remove(currentStep)
                if not dependsOn[step]:
                    del dependsOn[step]
            
def main():
    dependsOn = {}
    dependsOff = {}
    timeLeft = {}
    availableWorkers = 5
    allSteps = set()
    stepOrder = ''
    
    # with open('testdata.csv', 'r') as f:
    with open('input.txt', 'r') as f:

        for line in f:
            data_line = line.rstrip().replace('Step ','')\
                .replace(' must be finished before step ',',')\
                .replace(' can begin.','').split(',')
            allSteps.add(data_line[0])
            allSteps.add(data_line[1])
            if data_line[1] in dependsOn:
                dependsOn[data_line[1]].append(data_line[0])
            else:
                dependsOn[data_line[1]] = [data_line[0]]
                
            if data_line[0] in dependsOff:
                dependsOff[data_line[0]].append(data_line[1])
            else:
                dependsOff[data_line[0]] = [data_line[1]]
    time = 0
    while True:
        if timeLeft:
            doneSteps, availableWorkers = updateTime(timeLeft, availableWorkers)
            removeDependencies(dependsOff, dependsOn, doneSteps)
            for step in doneSteps:
                stepOrder += step 
     
        availableSteps = getAvailableSteps(allSteps, dependsOn)
        availableWorkers = addToWorkers(allSteps, timeLeft, availableSteps, availableWorkers)
        
        if len(allSteps) > 0 or timeLeft:
            time +=1
        else:
            break
    print(time)
    print(stepOrder)

    
if __name__ == "__main__": main()
    
