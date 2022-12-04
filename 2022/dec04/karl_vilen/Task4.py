if __name__ == '__main__':

    f=open("Task4.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i.split(","))
    f.close()

    answer = 0
    answer2 = 0

    for i in theInput:

        num0 = i[0].split("-")
        num1 = i[1].split("-")

        lower0 = int(num0[0])
        upper0 = int(num0[1])
        lower1 = int(num1[0])
        upper1 = int(num1[1])

        if lower0 <= lower1 and upper0 >= upper1:
            answer += 1
        elif lower1 <= lower0 and upper1 >= upper0:
            answer += 1

        if upper0 >= lower1 and lower0 <= upper1:
            answer2 += 1

    print(answer)
    print(answer2)
