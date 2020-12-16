""" Advent of Code Day 16 """

import re
from itertools import product

import numpy as np


def parse_input(input_file):
    with open(input_file, "r") as fp:
        text_split = fp.read().split("your ticket:")
    text_rules = text_split[0]
    text_tickets = text_split[1]

    regex_rule = r"([a-z]+\s?[a-z]*):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"
    rules = {}
    for line in text_rules.split("\n"):
        if m := re.search(regex_rule, line):
            rules[m.group(1)] = np.array(
                [[int(m.group(2)), int(m.group(3))], [int(m.group(4)), int(m.group(5))]]
            )
    tickets = []
    for line in text_tickets.splitlines():
        if len(line) > 0 and line[0].isdigit():
            tickets.append(np.array(line.split(","), np.int64))
    my_ticket = np.array(tickets[0])
    nearby_tickets = np.array(tickets[1:])

    return rules, my_ticket, nearby_tickets


# def validate1(rules, ticket):
#     valid_fields = [False]*len(rules)
#     i = 0
#     for field, bounds in zip(ticket, rules.values()):
#         if (bounds[0, 0] <= field <= bounds[0, 1]) \
#         or (bounds[1, 0] <= field <= bounds[1, 1]):
#             valid_fields[i] = True
#     return valid_fields


def get_invalid_fields(rules, ticket):
    inv_fields = []
    for field in ticket:
        if not any(
            [
                (bounds[0, 0] <= field <= bounds[0, 1])
                or (bounds[1, 0] <= field <= bounds[1, 1])
                for bounds in rules.values()
            ]
        ):
            inv_fields.append(field)
    return inv_fields


if __name__ == "__main__":

    rules, my_ticket, nearby_tickets = parse_input('./input_day16.txt')
    # rules, my_ticket, nearby_tickets = parse_input("./test.txt")

    # Part I
    all_invalid_fields = []
    valid_tickets = []
    for ticket in nearby_tickets:
        invalid_fields = get_invalid_fields(rules, ticket)
        if len(invalid_fields) == 0:
            valid_tickets.append(ticket)
        all_invalid_fields.extend(invalid_fields)

    valid_tickets = np.array(valid_tickets)
    print(sum(all_invalid_fields))

    # Part II
    # Calculate which rules match which columns in a bool matrix.
    num_fields = valid_tickets.shape[1]
    field_names = np.array(list(rules.keys()))
    matches = np.zeros((num_fields, num_fields), dtype=np.int64)
    for irule, name in enumerate(rules):
        bounds = rules[name]
        for icol in range(num_fields):
            col = valid_tickets[:, icol]
            in_bound1 = np.logical_and(bounds[0, 0] <= col, col <= bounds[0, 1])
            in_bound2 = np.logical_and(bounds[1, 0] <= col, col <= bounds[1, 1])
            if np.all(np.logical_or(in_bound1, in_bound2)):
                matches[irule, icol] = 1

    # Order the cols of the match matrix in terms of increasing matches:
    # the col diff will then give the index of the matching field.
    isort = np.argsort(matches.sum(axis=0))
    matches_sort = matches[:, isort]
    matches_sort = np.hstack((matches_sort[:, 0][:,None], np.diff(matches_sort)))
    ifields = np.argwhere(matches_sort.T == 1)[:, 1]
    iunsort = isort.argsort()
    field_order = field_names[ifields[iunsort]]

    prod = 1
    for i, name in enumerate(field_order):
        if 'departure' in name:
            prod *= my_ticket[i]
    print(prod)
