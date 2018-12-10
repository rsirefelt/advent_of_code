import numpy as np
import llist
import time
num_players = 458
marble_list = llist.dllist([0])
curr_marble_node = marble_list.first
curr_player_id = 0
player_scores = np.zeros(num_players, dtype=int)
t_start = time.time()
for i in range(1, 7201901):
    if i % 23 != 0:
        if curr_marble_node == marble_list.last:
            curr_marble_node = marble_list.insert(i, marble_list.first.next)
        elif curr_marble_node.next == marble_list.last:
            curr_marble_node = marble_list.append(i)
        else:
            curr_marble_node = marble_list.insert(i,
                                                  curr_marble_node.next.next)
    else:
        for _ in range(7):
            if curr_marble_node == marble_list.first:
                curr_marble_node = marble_list.last
            else:
                curr_marble_node = curr_marble_node.prev

        node_to_remove = curr_marble_node
        curr_marble_node = curr_marble_node.next

        player_scores[curr_player_id] += i + node_to_remove.value
        marble_list.remove(node_to_remove)

    curr_player_id = (curr_player_id + 1) % num_players

t_end = time.time()
print("Score: %d in %f sec" % (max(player_scores), t_end - t_start))
