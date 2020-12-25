if __name__ == '__main__':
    
    f=open("Task25.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    cardKey = int(theInput[0])
    doorKey = int(theInput[1])

    divider = 20201227
    subjectNumber = 7
    theValue = 1
    i = 0

    while True:
        theValue = theValue * subjectNumber
        theValue = theValue % divider
        if theValue == cardKey:
            cardLoops = i
            break
        i+=1

    cardLoops +=1

    theValue = 1

    i = 0

    while True:
        theValue = theValue * subjectNumber
        theValue = theValue % divider
        if theValue == doorKey:
            doorLoops = i
            break
        i+=1

    doorLoops +=1
    encryptionKey = cardKey
    for i in range(doorLoops-1):
        encryptionKey = encryptionKey * cardKey
        encryptionKey = encryptionKey % divider
    print("Key1")
    print(encryptionKey)
    encryptionKey2 = doorKey


    for i in range(cardLoops-1):
        encryptionKey2 = encryptionKey2 * doorKey
        encryptionKey2 = encryptionKey2 % divider
    print("Key2")
    print(encryptionKey2)

    if encryptionKey2 == encryptionKey:
        print("Done")
        print(encryptionKey)
