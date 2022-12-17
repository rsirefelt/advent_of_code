import numpy as np

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line[:-1] for line in lines]
    return lines[:-1]

def parseGraph(lines):
    graph = {}
    for line in lines:
        node = line.split(' ')[1]
        flow_rate = int(line.split(' ')[4].split('=')[1][:-1])
        if "valves" in line:
            neighbours = line.split(' valves ')[1].split(', ')
        else:
            neighbours = line.split(' valve ')[1].split(', ')

        graph[node] = {'flow_rate' : flow_rate, "neighbours" : neighbours}
    return graph

def getScoreFromState(graph, state, num_valves_with_nonzero_flow):
    state = bin(state)[2:].zfill(num_valves_with_nonzero_flow)
    total_score = 0
    for idx, on_off in enumerate(state):
        on_off = int(on_off)
        if on_off == 1:
            total_score = total_score + graph[nodes_with_nonzero_flow_rate[idx]]["flow_rate"]
    return total_score


graph = parseGraph(parseInput("test_input.txt"))
nodes_with_nonzero_flow_rate = [name for name in graph.keys() if graph[name]["flow_rate"] != 0]
num_valve_states = 2**len(nodes_with_nonzero_flow_rate)

# Fill out initial solutions at t=30
solutions = {name : np.zeros((num_valve_states, 31)) for name in graph.keys()}
for node in graph.keys():
    for state in range(num_valve_states):
        solutions[node][state, 30] = getScoreFromState(graph, state, len(nodes_with_nonzero_flow_rate))

# Now, fill out the solution table
optimal_path = {node : [[None for m in range(31)] for s in range(num_valve_states)] for node in graph.keys()}
for minute in range(29, -1, -1):
    for node in graph.keys():
        for state in range(num_valve_states):
            possible_scores = []
            score_this_minute = getScoreFromState(graph, state, len(nodes_with_nonzero_flow_rate))
            # Either we turn on the valve
            if node in nodes_with_nonzero_flow_rate:
                new_state = bin(state)[2:].zfill(len(nodes_with_nonzero_flow_rate))
                index = nodes_with_nonzero_flow_rate.index(node)
                new_state = new_state[:index] + '1' + new_state[index + 1:]
                new_state = int(new_state, 2)

                possible_scores.append(score_this_minute + solutions[node][new_state, minute+1])

            # Or, we move to one of the neighbouring nodes
            for neighbour in graph[node]["neighbours"]:
                possible_scores.append(score_this_minute + solutions[neighbour][state, minute+1])

            # The best solution is the best of these
            solutions[node][state, minute] = max(possible_scores)
            best_idx = np.argmax(possible_scores)
            if best_idx == 0 and len(possible_scores) > len(graph[node]["neighbours"]):
                optimal_path[node][state][minute] = "opened valve " + node
            else:
                if len(possible_scores) > len(graph[node]["neighbours"]):
                    optimal_path[node][state][minute] = graph[node]["neighbours"][best_idx - 1]
                else:
                    optimal_path[node][state][minute] = graph[node]["neighbours"][best_idx]

print("Part 1: " + str(solutions["AA"][0, 1]))

# Unravel the path
curr_node = "AA"
curr_state = 0
for minute in range(1, 31):
    if "opened valve" in optimal_path[curr_node][curr_state][minute]:
        print(optimal_path[curr_node][curr_state][minute])
        curr_state = bin(curr_state)[2:].zfill(len(nodes_with_nonzero_flow_rate))
        index = nodes_with_nonzero_flow_rate.index(curr_node)
        curr_state = curr_state[:index] + '1' + curr_state[index + 1:]
        curr_state = int(curr_state, 2)
    else:
        curr_node = optimal_path[curr_node][curr_state][minute]

xxx = 3