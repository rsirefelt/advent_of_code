if __name__ == '__main__':

    f=open("Task5.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    stacks = dict()
    stacks2 = dict()

    for i in theInput:
    
        if "[" in i:

            index = 1

            for j in range(1,len(i),4):
            
                if i[j] == " ":
                    index += 1
                    continue
                
                if index not in stacks.keys():
                    stacks[index] = i[j]
                else:
                    stacks[index] = stacks[index] + i[j]

                index += 1
        elif "from" not in i:
            stacks2 = stacks.copy()
            continue
        else:
            instr = i.replace("move ","")
            instr = instr.replace(" from ",",")
            instr = instr.replace(" to ",",")
            instr = instr.split(",")

            for j in range(int(instr[0])):
                
                stacks[int(instr[2])] = stacks[int(instr[1])][0] + stacks[int(instr[2])]
                stacks[int(instr[1])] = stacks[int(instr[1])][1:]

            stacks2[int(instr[2])] = stacks2[int(instr[1])][0:int(instr[0])] + stacks2[int(instr[2])]
            stacks2[int(instr[1])] = stacks2[int(instr[1])][int(instr[0]):]

    answer = ""
    answer2 = ""

    for i in range(1,len(stacks)+1):
        answer += stacks[i][0]
        answer2 += stacks2[i][0]
        
    print(answer)
    print(answer2)