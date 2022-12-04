if __name__ == '__main__':

    f=open("Task3.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    answer = 0

    for i in theInput:

        halfLength = int(len(i)/2)
        half1 = i[:halfLength]
        half2 = i[halfLength:]

        for j in half1:
            if j in half2:
                break

        if j.isupper():
            answer += ord(j) - ord("A") + 27
        else:
            answer += ord(j) - ord("a") + 1

    print(answer)

    answer2 = 0

    for i in range(0,len(theInput),3):

        packs = ["","",""]

        packs[0] = theInput[i]
        packs[1] = theInput[i+1]
        packs[2] = theInput[i+2]
        
        for j in packs[0]:
            if j in packs[1] and j in packs[2]:
                break

        if j.isupper():
            answer2 += ord(j) - ord("A") + 27
        else:
            answer2 += ord(j) - ord("a") + 1

    print(answer2)
