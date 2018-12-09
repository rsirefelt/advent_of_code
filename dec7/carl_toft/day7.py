# Read input 
with open('input.txt') as f:
    lines = f.readlines() 

alphabet = [chr(65+k) for k in range(0,26)]
graph = {letter: [] for letter in alphabet}  
for k in range(len(lines)): 
    graph[lines[k][36]].append(lines[k][5])

# Find first element of ordering 
topologicalOrdering = []
lettersBeingProduced = [] 

while len(topologicalOrdering) != 26:
    for letter in alphabet:
        # Skip the ones we are done with 
        if letter in topologicalOrdering:
            continue

        # If the current letter has no other requirements, add it 
        if len(graph[letter]) == 0:
            topologicalOrdering.append(letter)
            break

        # If the current letter has requirements, see if they all have
        # been met 
        allDone = True
        for testChar in graph[letter]:
            if testChar not in  topologicalOrdering:
                allDone = False

        if allDone == True:
            topologicalOrdering.append(letter)
            break 


str = ''
for letter in topologicalOrdering:
    str += letter

print(str)