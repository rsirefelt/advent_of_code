import re
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
from joblib import Parallel, delayed


class Blueprint:
    def __init__(self, id: int, costs: Tuple[int, int, Tuple[int, int], Tuple[int, int]]):
        self.id = id
        self.costs = np.array([[costs[0], 0, 0, 0], [costs[1], 0, 0, 0], [
                              costs[2][0], costs[2][1], 0, 0], [costs[3][0], 0, costs[3][1], 0]], dtype=int)

    def get_build_options(self, resources):
        options = []
        for i, cost in enumerate(self.costs):
            if np.all(cost <= resources):
                options.append(i)
        return options if 3 not in options else [3]


@dataclass
class BuildSequence:
    robots: np.ndarray
    robots_building: np.ndarray
    resources: np.ndarray
    currently_building_index: Optional[int]

    def gather(self):
        self.resources += self.robots

    def build(self, costs):
        if self.currently_building_index is not None:
            self.robots[self.currently_building_index] += 1
            self.resources -= costs[self.currently_building_index]
        self.currently_building_index = None

    def keep(self, max_cost_per_resource):
        return np.all(self.robots[:3] <= max_cost_per_resource[:3])


def refine(build_sequences):
    bs_as_dict = defaultdict(list)

    for build_seq in build_sequences:
        key = tuple(build_seq.robots)
        bs_as_dict[key].append(build_seq)

    keep_indices = defaultdict(list)
    for key, bs_list in bs_as_dict.items():
        keep_indices[key].append(0)
        for i in range(1, len(bs_list)):
            add_this = True
            to_remove = []
            for j, keep_index in enumerate(keep_indices[key]):
                if np.all(bs_list[i].resources <= bs_list[keep_index].resources):
                    add_this = False
                elif np.all(bs_list[i].resources >= bs_list[keep_index].resources):
                    to_remove.append(j)

            for ind in reversed(to_remove):
                del keep_indices[key][ind]
            if add_this:
                keep_indices[key].append(i)

    to_keep = []
    for key, bss in bs_as_dict.items():
        to_keep.extend([bs for i, bs in enumerate(bss) if i in keep_indices[key]])
    return to_keep


def eval_quality_level(blueprint, n_minutes=24):
    build_sequences = [BuildSequence(np.array([1, 0, 0, 0], dtype=int),
                                     np.array(4*[0], dtype=int),
                                     np.array(4*[0], dtype=int),
                                     None)]

    max_cost_per_resource = blueprint.costs.max(axis=0)
    for i in range(n_minutes):
        build_sequences = [bs for bs in build_sequences if bs.keep(max_cost_per_resource)]
        build_sequences = refine(build_sequences)

        build_sequences_to_add = []
        for build_sequence in build_sequences:
            build_options = blueprint.get_build_options(build_sequence.resources)
            for build_option in build_options:
                new_build_sequence = deepcopy(build_sequence)
                new_build_sequence.currently_building_index = build_option
                build_sequences_to_add.append(new_build_sequence)
        build_sequences.extend(build_sequences_to_add)

        for build_sequence in build_sequences:
            build_sequence.gather()
            build_sequence.build(blueprint.costs)

    return max([bs.resources[3] for bs in build_sequences])


with open('inputs/day19') as f:
    blueprint_data = f.read().splitlines()

blueprints = []
pat = re.compile(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian '
                 r'robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
for blueprint_line in blueprint_data:
    match = pat.match(blueprint_line)

    blueprints.append(Blueprint(id=int(match.groups()[0]),
                                costs=(int(match.groups()[1]), int(match.groups()[2]),
                                (int(match.groups()[3]), int(match.groups()[4])),
                                (int(match.groups()[5]), int(match.groups()[6])))))

max_geodes = Parallel(n_jobs=6)(delayed(eval_quality_level)(blueprint) for blueprint in blueprints)
print(sum([i*mg for i, mg in enumerate(max_geodes, 1)]))

max_geodes = Parallel(n_jobs=3)(delayed(eval_quality_level)(blueprint, n_minutes=32) for blueprint in blueprints[:3])
print(np.prod(max_geodes))
