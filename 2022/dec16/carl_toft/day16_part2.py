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


graph = parseGraph(parseInput("input.txt"))
nodes_with_nonzero_flow_rate = [name for name in graph.keys() if graph[name]["flow_rate"] != 0]
num_valve_states = 2**len(nodes_with_nonzero_flow_rate)
scores = [getScoreFromState(graph, state, len(nodes_with_nonzero_flow_rate)) for state in range(num_valve_states)]

# Fill out initial solutions at t=30
prev_solutions = {name : {name2 : np.zeros(num_valve_states) for name2 in graph.keys()} for name in graph.keys()}
solutions = {name : {name2 : np.zeros(num_valve_states) for name2 in graph.keys()} for name in graph.keys()}
for state in range(num_valve_states):
    print(state)
    score = scores[state]
    for node in graph.keys():
        for elephant_node in graph.keys():
            prev_solutions[node][elephant_node][state] = score

# Now, fill out the solution table
for minute in range(25, 0, -1):
    print(minute)
    for node in graph.keys():
        print(node)
        for elephant_node in graph.keys():
            for state in range(num_valve_states):
                possible_scores = []
                score_this_minute = scores[state]
                new_state = state

                for new_node in [node, *graph[node]["neighbours"]]:
                    if new_node == node and node in nodes_with_nonzero_flow_rate:
                        new_state = bin(state)[2:].zfill(len(nodes_with_nonzero_flow_rate))
                        index = nodes_with_nonzero_flow_rate.index(node)
                        new_state = new_state[:index] + '1' + new_state[index + 1:]
                        new_state = int(new_state, 2)
                    else:
                        new_state = state

                    for new_elephant_node in [elephant_node, *graph[elephant_node]["neighbours"]]:
                        # Either we turn on the valve
                        if new_elephant_node == elephant_node and elephant_node in nodes_with_nonzero_flow_rate and new_elephant_node != new_node:
                            neww_state = bin(new_state)[2:].zfill(len(nodes_with_nonzero_flow_rate))
                            index = nodes_with_nonzero_flow_rate.index(elephant_node)
                            neww_state = neww_state[:index] + '1' + neww_state[index + 1:]
                            neww_state = int(neww_state, 2)
                        else:
                            neww_state = new_state
                        possible_scores.append(score_this_minute + prev_solutions[new_node][new_elephant_node][neww_state])
                solutions[node][elephant_node][state] = max(possible_scores)
    prev_solutions = {name: {name2: np.zeros(num_valve_states) for name2 in graph.keys()} for name in graph.keys()}
    for n in graph.keys():
        for nn in graph.keys():
            prev_solutions[n][nn] = np.copy(solutions[n][nn])


print("Part 1: " + str(solutions["AA"]["AA"][0]))
xxx = 3
