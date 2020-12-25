def solveWinner(player1Cards, player2Cards, depth):

    player1 = player1Cards.copy()
    player2 = player2Cards.copy()

    prevOrd1 = []
    prevOrd2 = []

    while len(player1) > 0 and len(player2) > 0:

        if ((player1 in prevOrd1) and (player2 in prevOrd2)) and (prevOrd1.index(player1) == prevOrd2.index(player2)):
            return 1
        else:
            prevOrd1.append(player1.copy())

            prevOrd2.append(player2.copy())

        card1 = player1[0]
        card2 = player2[0]

        player1.pop(0)
        player2.pop(0)

        if card1 <= len(player1) and card2 <= len(player2):
            winner = solveWinner(player1[:card1].copy(), player2[:card2].copy(),depth+1)
        else:
            if card1 > card2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    if len(player1) == 0:
        winner = 2
    else:
        winner = 1

    if depth == 0:
        if len(player1) == 0:
            return player2
        else:
            return player1
    else:
        return winner

if __name__ == '__main__':

    f=open("Task22.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    player1 = []
    player2 = []

    player = 1

    for i in theInput:
        if i == "Player 2:":
            player = 2
            continue
        elif i == "Player 1:":
            continue
        elif i == "":
            continue
        else:
            if player == 1:
                player1.append(int(i))
            else:
                player2.append(int(i))

    theWinner = solveWinner(player1, player2, 0)

    answer = 0

    for index, value in enumerate(theWinner):
        answer += (len(theWinner)-index)*value


    print("Done")
    print(answer)