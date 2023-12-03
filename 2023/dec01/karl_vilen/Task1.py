if __name__ == '__main__':

    f=open("Task1.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(i)
    f.close()

    answer = 0

    theList = ["one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]
    theList2 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

    for i in theInput:

        position1 = 100000000
        position2 = -1
        number1 = 0
        number2 = 0

        for index, j in enumerate(theList):
            if j in i:
                pos1 = i.find(j)
                pos2 = i.rfind(j)
                if pos1 < position1:
                    position1 = pos1
                    number1 = theList2[index]
                if pos2 > position2:
                    position2 = pos2
                    number2 = theList2[index]

        answer1 += number1 * 10 + number2

    print(answer)
