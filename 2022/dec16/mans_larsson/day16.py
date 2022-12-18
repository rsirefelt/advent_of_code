from collections import defaultdict
from dataclasses import dataclass
from typing import List, Set
from copy import deepcopy


def remove_bad_paths(inp_paths, step):
    paths_to_output = defaultdict(list)

    highest_score = max([max([p.score for p in paths]) for paths in inp_paths.values()])
    for node, paths in inp_paths.items():
        max_dict = dict()
        for path in paths:
            dict_key = ''.join(sorted(list(path.open_valves)))
            if dict_key not in max_dict or path.score > max_dict[dict_key].score:
                max_dict[dict_key] = path

        # ugly heuristic to speed things up
        margin = 500 if step < 20 else 100
        paths_to_output[node] = [val for val in max_dict.values() if val.score >= highest_score - margin]
    return paths_to_output


@dataclass
class Valve:
    flow: int
    paths: List[str]


@dataclass
class Path:
    score: int
    open_valves: Set[str]


with open('inputs/day16') as f:
    data = f.read().splitlines()

valves = dict()
for line in data:
    line_info = line.replace(',', '').replace(';', '').split()
    valves[line_info[1]] = Valve(int(line_info[4][5:]), paths=line_info[9:])

paths = {'AA': [Path(0, set())]}

all_valves_that_can_be_open = set(key for key, valve in valves.items() if valve.flow > 0)
n_tot_steps = 30
for step in range(n_tot_steps):
    next_step_paths = defaultdict(list)
    for current_node, all_paths in paths.items():
        for path in all_paths:
            if path.open_valves == all_valves_that_can_be_open:
                next_step_paths[current_node].append(path)
                continue
            if valves[current_node].flow > 0 and current_node not in path.open_valves:
                to_add = valves[current_node].flow * (n_tot_steps - step - 1)
                next_step_paths[current_node].append(Path(path.score + to_add, path.open_valves | {current_node}))
            for neighbor in valves[current_node].paths:
                next_step_paths[neighbor].append(Path(path.score, path.open_valves))
    paths = remove_bad_paths(next_step_paths, step)

max_of_all = 0
for paths_to_eval in paths.values():
    for path in paths_to_eval:
        if path.score > max_of_all:
            max_of_all = path.score

print(max_of_all)

paths = {('AA', 'AA'): [Path(0, set())]}

n_tot_steps = 26
for step in range(n_tot_steps):
    next_step_paths = defaultdict(list)
    for (my_current_node, elephant_current_node), all_paths in paths.items():
        for path in all_paths:
            my_options, elephant_options = [], []
            if path.open_valves == all_valves_that_can_be_open:
                next_step_paths[(my_current_node, elephant_current_node)].append(path)
                continue

            if valves[my_current_node].flow > 0 and my_current_node not in path.open_valves:
                my_options.append('open')
            if valves[elephant_current_node].flow > 0 and elephant_current_node not in path.open_valves:
                elephant_options.append('open')

            for neighbor in valves[my_current_node].paths:
                my_options.append(neighbor)
            for neighbor in valves[elephant_current_node].paths:
                elephant_options.append(neighbor)

            for my_option in my_options:
                for elephant_option in elephant_options:
                    if my_option == 'open' and elephant_option == 'open' and my_current_node == elephant_current_node:
                        continue
                    to_add = 0
                    open_valves = deepcopy(path.open_valves)
                    if my_option == 'open':
                        my_new_node = my_current_node
                        to_add += valves[my_current_node].flow * (n_tot_steps - step - 1)
                        if my_current_node in open_valves:
                            asd = 0
                        open_valves.add(my_current_node)
                    else:
                        my_new_node = my_option
                    if elephant_option == 'open':
                        elephant_new_node = elephant_current_node
                        to_add += valves[elephant_current_node].flow * (n_tot_steps - step - 1)
                        if elephant_current_node in open_valves:
                            asd = 0
                        open_valves.add(elephant_current_node)
                    else:
                        elephant_new_node = elephant_option
                    next_step_paths[(my_new_node, elephant_new_node)].append(Path(path.score + to_add, open_valves))
    paths = remove_bad_paths(next_step_paths, step)

max_of_all = 0
best_path = None
for paths_to_eval in paths.values():
    for path in paths_to_eval:
        if path.score > max_of_all:
            max_of_all = path.score
            best_path = path

print(max_of_all)
