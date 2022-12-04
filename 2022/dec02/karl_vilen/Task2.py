if __name__ == '__main__':

    f=open("Task2.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i.split(" "))
    f.close()

    score1 = 0
    score2 = 0

    for i in theInput:

        if i[1] == "X":
            score1 += 1
            if i[0] == "A":
                score1 += 3
                score2 += 3
            elif i[0] == "B":
                score2 += 1
            elif i[0] == "C":
                score1 += 6
                score2 += 2
        
        elif i[1] == "Y":
            score1 += 2
            score2 += 3
            if i[0] == "A":
                score1 += 6
                score2 += 1
            elif i[0] == "B":
                score1 += 3
                score2 += 2
            elif i[0] == "C":
                score2 += 3
        
        elif i[1] == "Z":
            score1 += 3
            score2 += 6
            if i[0] == "A":
                score2 += 2
            elif i[0] == "B":
                score1 += 6
                score2 += 3
            elif i[0] == "C":
                score1 += 3
                score2 += 1

    print(score1)
    print(score2)
