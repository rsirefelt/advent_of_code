import numpy as np
from datetime import datetime
import operator

def sortInput(inputList):
    inputList.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M'))
    #print(inputList)
    
def isInt(astring):
    """ Is the given string an integer? """
    try: int(astring)
    except ValueError: return 0
    else: return 1


def main():
    input = []

    # with open('testdata.csv', 'r') as f:
    with open('input.txt', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            input.append(string.rstrip().replace('[','').split(']'))
    
        sortInput(input)
        sleepTimes = {}
        totalSleep = {}
        startSleep = 0
        endSleep = 0
        for day in input:
            event=day[1].lstrip().replace('Guard #','').replace(' begins shift','')\
                .replace(' asleep','').replace(' up','')
            #print(event)
            if isInt(event):
                guard = event
                if guard not in sleepTimes:
                    sleepTimes[guard] = np.zeros(60)
                    totalSleep[guard] = 0

            elif event=='falls':
                startSleep = int(day[0].split(' ')[1].replace('00:',''))
                
            elif event=='wakes':
                endSleep = int(day[0].split(' ')[1].replace('00:',''))
                
                sleepTimes[guard][startSleep-1:endSleep-1] += 1
                totalSleep[guard] += endSleep - startSleep


        maxSleepGuard = max(totalSleep.items(), key=operator.itemgetter(1))[0]
        print("Part1: " +str((np.argmax(sleepTimes[maxSleepGuard])+1)*int(maxSleepGuard)))
        maxIndexTimes = 0
        maxIndex = 0
        maxGuard = 0
        for guard, sleepTimes in sleepTimes.items():
            indexTimes = np.max(sleepTimes)
            if indexTimes > maxIndexTimes:
                maxIndexTimes = indexTimes
                maxIndex = np.argmax(sleepTimes)
                maxGuard = guard
            
        print("Part2: " +str((maxIndex+1)*int(maxGuard)))

if __name__ == "__main__": main()
	
