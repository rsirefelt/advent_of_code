import numpy as np

num_players = 458
curr_marble_id = 0
curr_marble_val = 1
marble_list = [0]
curr_player_id = 0
player_scores = np.zeros(num_players, dtype=int)

while curr_marble_val != 72019:
    if curr_marble_val % 23 != 0:
        curr_marble_id = curr_marble_id + 2 
        if curr_marble_id > len(marble_list): 
            curr_marble_id = 1
        marble_list.insert(curr_marble_id, curr_marble_val)
    else:
        if curr_marble_id - 7 > -1:
            curr_marble_id = curr_marble_id - 7
        else:
            curr_marble_id = len(marble_list) - abs(curr_marble_id - 7)
        player_scores[
            curr_player_id] += curr_marble_val + marble_list[curr_marble_id]
        del marble_list[curr_marble_id]

    curr_player_id = (curr_player_id + 1) % num_players
    curr_marble_val += 1

print(max(player_scores))
