import re

def createRegexString(thisRule, rules, depth, maxDepth):
    if depth > maxDepth:
        return ''

    if rules[thisRule][0] == '"':
        return rules[thisRule][1]

    currentRules = []
    for theseRules in rules[thisRule].split('|'):
        answers = []
        for thisRule in theseRules.split():
            answers.append(createRegexString(thisRule, rules, depth + 1, maxDepth))
        currentRules.append("".join(answers))

    returnString = '(' + '|'.join(currentRules) + ')'

    return returnString

if __name__ == '__main__':
    
    f=open("Task19.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        i = i.split(": ")
        theInput.append(i)
    f.close()

    allMessages = []
    allRules = dict()
    messages = False

    for i in theInput:
        if len(i) == 1 and messages == False:
            messages = True
            continue

        if messages == False:
            allRules[i[0]] = i[1]
        else:
            allMessages.append(i[0])

    allRules["8"] = "42 | 42 8"
    allRules["11"] = "42 31 | 42 11 31"

    regex = re.compile(createRegexString("0", allRules, 0, 20))

    count = 0

    for i in allMessages:
        if regex.fullmatch(i):
            count += 1


    print("Done")
    print(count)