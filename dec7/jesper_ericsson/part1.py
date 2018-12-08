import numpy as np

def getAvailableSteps(allSteps, dependsOn):
    availableSteps =[]       
    for step in allSteps:
        if step not in dependsOn:
            availableSteps.append(step)
    availableSteps.sort()
    return availableSteps[0]

def removeDependencies(dependsOff, dependsOn, currentStep):
    if len(dependsOn) > 0:
        for step in dependsOff[currentStep]:
            dependsOn[step].remove(currentStep)
            if not dependsOn[step]:
                del dependsOn[step]
        
def main():
    dependsOn = {}
    dependsOff = {}
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
    
    for _ in range(len(allSteps)):
        availableStep = getAvailableSteps(allSteps, dependsOn)

        removeDependencies(dependsOff, dependsOn, availableStep)
        stepOrder += availableStep
        allSteps.remove(availableStep)

    print(stepOrder)

    
if __name__ == "__main__": main()
    
