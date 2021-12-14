if __name__ == '__main__':

    f=open("Task14.txt","r")
    lines=f.readlines()
    theInput = []
    polymer = ""
    counts = dict()

    for i in lines:
        i = i.rstrip()

        if "->" in i:
            i = i.split(" -> ")
            theInput.append([i[0],i[1]])
            counts[i[1]] = 0
        elif len(i) > 0:
            polymer = i
    f.close()

    templates = dict()
    pairs = dict()

    for i in theInput:
        templates[i[0]] = i[1]
        pairs[i[0]] = 0

    for i in range(len(polymer)-1):

        pairs[polymer[i]+polymer[i+1]] += 1

    newPairs = dict()
    emptyDict = pairs.copy()

    for i in theInput:

        pair1 = i[0][0] + templates[i[0]]
        pair2 = templates[i[0]] + i[0][1]

        newPairs[i[0]] = [pair1,pair2]

    for i in range(40):

        createdPairs = emptyDict.copy()

        for key, value in pairs.items():

            pair1 = newPairs[key][0]
            pair2 = newPairs[key][1]

            createdPairs[pair1] += value
            createdPairs[pair2] += value

        pairs = createdPairs.copy()

    for key,value in pairs.items():

        counts[key[0]] += value
        counts[key[1]] += value

    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1

    theMin = min(counts.values())//2
    theMax = max(counts.values())//2

    print("Done")
    print(theMax-theMin)
