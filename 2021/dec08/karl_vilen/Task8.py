from itertools import permutations

if __name__ == '__main__':

    f=open("Task8.txt","r")
    lines=f.readlines()
    theInput = []
    theInputP2 = []

    for i in lines:
        i = i.rstrip()
        a = i.split(" | ")
        theInput.append(a[0].split(" "))
        theInputP2.append(a[1].split(" "))
    f.close()

    theAnswer = 0

    for kIndex, k in enumerate(theInput):

        theConfig = dict()

        for i in k:

            if len(i) == 2:
                theConfig[1] = i[0] + i[1]
            elif len(i) == 3:
                theConfig[7] = i[0] + i[1] + i[2]
            elif len(i) == 4:
                theConfig[4] = i[0] + i[1] + i[2] + i[3]
            elif len(i) == 7:
                theConfig[8] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6]

        for i in k:

            if len(i) == 6:

                if 0 in theConfig and 6 in theConfig:
                    theConfig[9] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5]
                    continue
                elif 0 in theConfig and 9 in theConfig:
                    theConfig[6] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5]
                    continue
                elif 6 in theConfig and 9 in theConfig:    
                    theConfig[0] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5]
                    continue
                    
                firstSum = 0

                for j in i:

                    if j in theConfig[1]:
                        firstSum+=1

                if firstSum == 1:
                    theConfig[6] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5]
                    continue

                secondSum = 0

                for j in i:

                    if j in theConfig[4]:
                        secondSum += 1

                if secondSum == 4:
                    theConfig[9] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5]
                    continue
                else:
                    theConfig[0] = i[0] + i[1] + i[2] + i[3] + i[4] + i[5]
                    continue

        for i in k:
            if len(i) == 5:

                if 2 in theConfig and 3 in theConfig:
                    theConfig[5] = i[0] + i[1] + i[2] + i[3] + i[4]

                    continue
                elif 2 in theConfig and 5 in theConfig:
                    theConfig[3] = i[0] + i[1] + i[2] + i[3] + i[4]
                    continue
                elif 3 in theConfig and 5 in theConfig:
                    theConfig[2] = i[0] + i[1] + i[2] + i[3] + i[4]
                    continue

                is5 = True
                for j in i:

                    if j not in theConfig[6]:
                        is5 = False
                if is5 == True:
                    theConfig[5] = i[0] + i[1] + i[2] + i[3] + i[4]
                    continue

                thirdSum = 0

                for j in i:
                    
                    if j in theConfig[1]:
                        thirdSum+=1
                    if thirdSum == 2:
                        theConfig[3] = i[0] + i[1] + i[2] + i[3] + i[4]
                        break

                if thirdSum != 2 and is5 == False:
                    theConfig[2] = i[0] + i[1] + i[2] + i[3] + i[4]

        multiplier = 1000
        thisAnswer = 0

        for j in theInputP2[kIndex]:
            isFound = False
            for key, value in theConfig.items():
                
                if isFound == True:
                    break
                variants = [''.join(p) for p in permutations(value)]

                for l in variants:
                    if j in l and len(j) == len(l):
                        thisAnswer += multiplier * key
                        multiplier = multiplier // 10
                        isFound = True
                        break
                        
        theAnswer += thisAnswer

    print("Done")
    print(theAnswer)
