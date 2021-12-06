if __name__ == '__main__':

    f=open("Task6.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput = i.split(",")
    f.close()

    theInput = [int(i) for i in theInput]

    fish = [0 for i in range(9)]

    for i in theInput:
        fish[i] += 1
    
    totalDays = 256

    for i in range(totalDays):
        newFish = fish[0]

        for j in range(8):
            fish[j] = fish[j+1]

        fish[6] += newFish
        fish[8] = newFish


    print("Done")
    print(sum(fish))
