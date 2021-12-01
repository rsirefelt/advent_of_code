if __name__ == '__main__':

    f=open("Task1.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        theInput.append(int(i))
    f.close()

    increased = 0

    for i in range(3,len(theInput)):
        a = theInput[i-1] + theInput[i-2] + theInput[i-3]
        b = theInput[i] + theInput[i-1] + theInput[i-2]
        if b > a:
            increased +=1

    print(increased)

