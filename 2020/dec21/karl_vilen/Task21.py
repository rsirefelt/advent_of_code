from copy import deepcopy

if __name__ == '__main__':

    f=open("Task21.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.replace("(","")
        i = i.replace(")","")
        i = i.replace(",","")
        i = i.split(" ")
        theInput.append(i)
    f.close()

    allergens = dict()
    allFoods = dict()

    for i in theInput:
        
        startJ = i.index("contains")

        firstAdditions = dict()

        for k in range(startJ):
            if i[k] not in allFoods:
                allFoods[i[k]] = 1
            else:
                allFoods[i[k]] += 1

        for j in range(startJ+1, len(i)):

            firstAdditions = dict()

            if i[j] not in allergens:

                firstAdditions[i[j]] = True
                emptyList = []
                allergens[i[j]] = deepcopy(emptyList)

            thisFood = []

            for k in range(startJ):

                thisFood.append(i[k])

                if i[j] in firstAdditions.keys():
                    allergens[i[j]].append(i[k])

            if i[j] not in firstAdditions:

                toRemove = []
                for k in allergens[i[j]]:
                    if k not in thisFood:
                        toRemove.append(k)

                for k in toRemove:
                    allergens[i[j]].remove(k)

    answer = 0

    for keys1, values1 in allFoods.items():
        present = False
        for keys, values in allergens.items():
            if keys1 in values:
                present = True
                break
        if present == False:
            answer += values1


    print("Done1")
    print(answer)

    foundAllergens = []

    while (True):

        anyRemoved = False

        for key, value in allergens.items():
            if len(value) == 1:
                if value[0] not in foundAllergens:
                    theValue = value[0]
                    foundAllergens.append(value[0])
                    break

        for key in allergens.keys():

            if theValue in allergens[key] and len(allergens[key]) > 1:
                allergens[key].remove(theValue)
                anyRemoved = True

        if anyRemoved == False:
            break

    allAllergens = list(allergens.keys())
    allAllergens.sort()

    answerString = ""

    for i in allAllergens:
        answerString = answerString + allergens[i][0] + ","


    answerString = answerString[:-1]

    print("Done")
    print(answerString)