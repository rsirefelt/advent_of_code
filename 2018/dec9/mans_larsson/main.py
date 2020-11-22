import numpy as np
numplayers = 405
pointslast = 717000

scores = np.zeros(numplayers)
marbles = [0, 1]
marble_position = 1
current_player = 0

for marble_value in range(2, pointslast+1):
    if (marble_value % 23) == 0:
        mm = marble_position - 7
        marble_position = (marble_position - 7) % len(marbles)
        score = marble_value + marbles.pop(marble_position)
        scores[current_player] += score          
        marble_positions = marble_position % len(marbles)
    else:
        marble_position += 2 
        if marble_position > len(marbles):
            marble_position = marble_position % len(marbles)
        marbles.insert(marble_position, marble_value)
    if marble_value % 50000 == 0:
        print('%d/%d' % (marble_value, pointslast))
    current_player = (current_player + 1) % numplayers

print(scores.max())