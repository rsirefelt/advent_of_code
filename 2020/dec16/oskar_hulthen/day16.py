import math
import regex as re
import numpy as np


def task1(rules, tickets):
    errors = []
    previous_check = np.ones(tickets.shape, dtype=bool)
    for conditions in rules.values():
        for condition in conditions:
            check = np.logical_or(tickets < condition[0], tickets > condition[1])
            previous_check = np.logical_and(previous_check, check)

    errors = tickets[previous_check]
    filtered_tickets = tickets[np.all(~previous_check, axis=1), :]
    return sum(errors), filtered_tickets


def task2(rules, tickets, our_ticket):
    found_matches = {}
    num_rules = len(rules)
    for name, conditions in rules.items():

        for i in range(num_rules):
            # Extract ticket column.
            column = tickets[:, i]
            previous_check = np.zeros(column.shape, dtype=bool)
            for condition in conditions:
                check = np.logical_and(column >= condition[0], column <= condition[1])
                previous_check = np.logical_or(previous_check, check)

            # If all values in column is within the condition, add as a match.
            if previous_check.all():
                prev_matches = found_matches.get(name, [])
                prev_matches.append(i)
                found_matches[name] = prev_matches

    # Find 1-1 matches for columns
    matched = [None for _ in range(num_rules)]
    while None in matched:
        for name, match_idxs in found_matches.items():
            if len(match_idxs) == 1:
                match_idx = match_idxs[0]
                # Add match
                matched[match_idx] = name
                # Remove the column_idx from matches to check.
                found_matches = {
                    key: [val for val in values if val != match_idx]
                    for key, values in found_matches.items()
                }
                break

    mul_ = 1
    for ticket_val, column in zip(our_ticket, matched):
        if "departure" in column:
            mul_ *= ticket_val
    return mul_


if __name__ == "__main__":
    rules = {}
    tickets = []
    our_ticket = None

    with open("input") as f:
        lines = list(f.readlines())
        num_lines = len(lines)
        # Load rules
        for i in range(0, num_lines):
            line = lines[i]
            line = line.rstrip()
            if line == "":
                break
            line = line.split(":")
            name = line[0]
            conditions = line[1].split(" or ")
            rule = []
            for condition in conditions:
                low, high = condition.split("-")
                rule.append((int(low), int(high)))

            rules[name] = rule
        # Load our ticket
        for j in range(i + 1, num_lines):
            line = lines[j]
            line = line.rstrip()
            if line == "your ticket:" or line == "":
                continue

            our_ticket = [int(val) for val in line.split(",")]
            break

        for k in range(j + 1, num_lines):
            line = lines[k]
            line = line.rstrip()
            if line == "nearby tickets:" or line == "":
                continue

            tickets.append([int(val) for val in line.split(",")])

    our_ticket = np.array(our_ticket)
    tickets = np.array(tickets)

    res1, filtered_tickets = task1(rules, tickets)
    print(res1)

    res2 = task2(rules, filtered_tickets, our_ticket)
    print(res2)
