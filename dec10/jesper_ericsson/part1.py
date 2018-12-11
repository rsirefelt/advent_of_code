import numpy as np
import operator
import scipy.misc
def takeSecond(elem):
    return elem[1]

def updatePos(posVelList):
    for posVel in posVelList:
        posVel[0] += posVel[2]
        posVel[1] += posVel[3]

def plotPos(posVelList, i):
    posVelList.sort(key=operator.itemgetter(1, 0))
    minY = posVelList[0][1]
    maxY = posVelList[-1][1]
    minX = min(x[0] for x in posVelList )
    maxX = max(x[0] for x in posVelList )
    if maxY - minY < 15:
        oldY = minY
        
        startInd = -minX +1
        print(i)
        str = ''
        ind = 0
        for posVel in posVelList:
            if posVel[1] > oldY:
                for _ in range(ind, maxX - minX):
                    str += '.'
                print(str)
                str = ''
                ind = 0
                
            for _ in range(ind, startInd+posVel[0]-1):
                str += '.'
            if ind != startInd+posVel[0]:
                str+='#'
                ind =startInd+posVel[0]
            oldY = posVel[1]
        print(str)

def main():
    posVelList = [] #np.array([0,0,0,0])
    # with open('testdata.csv', 'r') as f:
    with open('input.txt', 'r') as f:

        for line in f:
            line = line.rstrip().lstrip().replace('position=<', '')\
                .replace('> velocity=<', ',').replace('>','').split(',')
            posVelList.append([int(i) for i in line])

    for i in range(11000):
        plotPos(posVelList, i)
        updatePos(posVelList)

if __name__ == "__main__": main()
	
