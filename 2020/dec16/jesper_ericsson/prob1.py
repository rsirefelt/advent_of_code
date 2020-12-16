import numpy as np
import re
import time

regex_rule = re.compile(r'([a-z ]*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)')

regex_tickets = re.compile(r'([0-9]*,)')

def read_input(filename):
    rules = {}
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        your_ticket_bool = False
        your_ticket = []
        tickets = []
        for string in data_lines:
            rule = regex_rule.findall(string)
            if rule:
                rule_ints = []
                for rule_value in rule[0][1:]:
                    rule_ints.append(int(rule_value))
                rules[rule[0][0]] = rule_ints
            elif string.rstrip() == 'your ticket:':
                your_ticket_bool = True
            elif your_ticket_bool:
                ticket_fields = string.rstrip().split(',')
                for ticket_field in ticket_fields:
                    your_ticket.append(int(ticket_field))
                your_ticket_bool = False
            elif regex_tickets.match(string.rstrip()):
                ticket_fields = string.rstrip().split(',')
                current_ticket = []
                for ticket_field in ticket_fields:
                    current_ticket.append(int(ticket_field))

                tickets.append(np.array(current_ticket))

            
    return rules, your_ticket, np.array(tickets)

def main():
    rules, your_ticket, tickets = read_input('testdata.csv')
    rules, your_ticket, tickets = read_input('data.csv')

    start = time.time()
    # Part 1
    valid_tickets_bool = np.zeros(tickets.shape, dtype=bool)
    for rule in rules.values():

        current_rule1 = np.logical_and(tickets >= rule[0], tickets <= rule[1])
        current_rule2 = np.logical_and(tickets >= rule[2], tickets <= rule[3])
        valid_tickets_bool = np.logical_or(valid_tickets_bool, current_rule1)
        valid_tickets_bool = np.logical_or(valid_tickets_bool, current_rule2)
    
    print('The sum of invalid tickets is: %i' %tickets[~valid_tickets_bool].sum())

    # Remove unvalid tickets
    valid_tickets = tickets[valid_tickets_bool.all(axis=1)]

    # Apply the rules on all tickets
    num_rules = len(rules)
    valid_rules = np.empty((0,num_rules),dtype=bool)
    rule_names = []
    for rule_name in rules:
        rule_names.append(rule_name)
        rule = rules[rule_name]
        current_rule1 = np.logical_and(valid_tickets >= rule[0], valid_tickets <= rule[1])
        current_rule2 = np.logical_and(valid_tickets >= rule[2], valid_tickets <= rule[3])
        current_rule = np.logical_or(current_rule1, current_rule2)

        valid_rules = np.append(valid_rules, current_rule.all(axis=0).reshape(1,num_rules),axis=0)


    rule_with_field = {}
    for i in range(num_rules):
        sum_valid = valid_rules.sum(axis=0)
        # Find the field where only one rule works on all tickets
        current_field = np.where(sum_valid == 1)[0][0]
        # Find which rule it is
        rule_num = np.where(valid_rules[:,current_field])[0][0]
        # Remove 
        valid_rules[rule_num][:] = np.zeros((1,num_rules), dtype=bool)
        rule_with_field[rule_names[rule_num]] = current_field


    regex_departure = re.compile(r'departure ')
    field_multiple = 1
    for key in rule_with_field:
        if regex_departure.match(key):
            field_num = rule_with_field[key]
            field_multiple *= your_ticket[field_num]

    print('The product of the valid fields: %i' %field_multiple)

    end = time.time()
    print(['Runtime: ', end - start])


if __name__ == "__main__": main()