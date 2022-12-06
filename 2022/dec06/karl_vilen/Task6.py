if __name__ == '__main__':

    f=open("Task6.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput = i
    f.close()

    theLength = 14

    for i in range(theLength-1,len(theInput)):
    
        subString = theInput[i-theLength+1:i+1]
        j = set(subString)
        if len(j) == theLength:
            answer = i+1
            break
        
    print(answer)