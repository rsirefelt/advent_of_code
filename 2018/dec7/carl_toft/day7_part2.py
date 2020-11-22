########### Read input ##########
with open('input.txt') as f:
    lines = f.readlines() 

alphabet = [chr(65+k) for k in range(0,26)]
graph = {letter: [] for letter in alphabet}  
for k in range(len(lines)): 
    graph[lines[k][36]].append(lines[k][5])
##################################

##################################
def checkIfReady(letter, graph, finishedLetters):
    isReady = True
    for testChar in graph[letter]:
        if testChar not in finishedLetters:
            isReady = False
    return isReady
###################################

topologicalOrdering = 'PFKQWJSVUXEMNIHGTYDOZACRLB'
lettersBeingProduced = [] 
numWorkers = 5
timeLeft = {chr(65+k): 61+k for k in range(0,26)}
nextLetter = 0
numFinishedLetters = 0
elapsedTime = 0 

finishedLetters = []

while numFinishedLetters != len(topologicalOrdering):

    for k in range(numWorkers): # for each worker 
        if (len(lettersBeingProduced) < numWorkers): # is there room to work on one letter? 
            for kk in range(len(topologicalOrdering)):
                if (topologicalOrdering[kk] not in finishedLetters and topologicalOrdering[kk] not in lettersBeingProduced and checkIfReady(topologicalOrdering[kk], graph, finishedLetters)): 
                    lettersBeingProduced.append(topologicalOrdering[kk])
                    nextLetter += 1 
                    break 
    
    # Increase time by one 
    elapsedTime += 1
    tmp = ''
    for letter in lettersBeingProduced:
        tmp = tmp + letter + ' ' 

    print(str(elapsedTime) + ': '+ tmp)
    lettersToRemove = [] 
    for letter in lettersBeingProduced:
        timeLeft[letter] -= 1
        if (timeLeft[letter] == 0):
            lettersToRemove.append(letter)
            numFinishedLetters += 1
            finishedLetters.append(letter) 
            print('Letter ' + letter + ' finished on second ' + str(elapsedTime)) 
    for letter in lettersToRemove:
        lettersBeingProduced.remove(letter)
    
print(elapsedTime)
