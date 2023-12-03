if __name__ == '__main__':

    f=open("Task2.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.strip()
        i = i.replace("Game ","")
        i = i.replace(": ",";")
        i = i.split(";")
        theInput.append(i)
    f.close()

    answer = 0

    for indexI, i in enumerate(theInput):

        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        valid = True
        breakTwice = False

        for indexJ, j in enumerate(i):

            if indexJ == 0:
                continue

            thisSet = j.split(", ")

            for k in thisSet:

                if " green" in k:
                    balls = k.replace(" green", "")
                    balls = int(balls)
                    if balls > maxGreen:
                        maxGreen = balls
                elif " red" in k:
                    balls = k.replace(" red", "")
                    balls = int(balls)
                    if balls > maxRed:
                        maxRed = balls
                elif " blue" in k:
                    balls = k.replace(" blue", "")
                    balls = int(balls)
                    if balls > maxBlue:
                        maxBlue = balls

        answer += maxBlue * maxGreen * maxRed

    print(answer)
