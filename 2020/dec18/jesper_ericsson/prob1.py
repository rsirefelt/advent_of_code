import numpy as np
import time
import re
import time

regex_inner_parts = re.compile(r'(\([0-9*+ ]*\))')
regex_operation = re.compile(r'(\+ [0-9]+|\* [0-9]+)')
regex_plus = re.compile(r'([0-9]+ \+ [0-9]+)')

def read_expressions(filename):
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        expressions = []
        for string in data_lines:
            expressions.append(string.rstrip())
    return expressions

def evaluate_exp(exp):
    exp = exp.lstrip('(').rstrip(')')
    first_value = exp.split(' ')[0]
    result = int(first_value)
    operations = regex_operation.findall(exp)
    for operation in operations:
        if operation[0] == '+':
            result += int(operation[2:])
        elif operation[0] == '*':
            result *= int(operation[2:])

    return str(result)

def replace_plus(exp):
    replace_indices = [(m.start(0), m.end(0)) for m in regex_plus.finditer(exp)]
    
    for index in reversed(replace_indices):
        exp = exp[:index[0]] + '(' + exp[index[0]:index[1]] + ')' + exp[index[1]:]

    return exp

def main():
    expressions = read_expressions('testdata.csv')
    expressions = read_expressions('data.csv')

    sum_expressions = 0
    for expression in expressions:
        inner_parts = regex_inner_parts.findall(expression)
        while inner_parts:

            for parenthes in inner_parts:
                new_value = evaluate_exp(parenthes)
                expression = expression.replace(parenthes, new_value, 1)
            inner_parts = regex_inner_parts.findall(expression)
        sum_expressions += int(evaluate_exp(expression))

    print('Part 1 sum: %i' %sum_expressions)

    sum_expressions = 0
    for expression in expressions: 
        expression = replace_plus(expression)
        inner_parts = regex_inner_parts.findall(expression)
        while inner_parts:
            for parenthes in inner_parts:
                new_value = evaluate_exp(parenthes)
                expression = expression.replace(parenthes, new_value, 1)

            expression = replace_plus(expression)
            inner_parts = regex_inner_parts.findall(expression)

        sum_expressions += int(evaluate_exp(expression))

    print('Part 2 sum: %i' %sum_expressions)

if __name__ == "__main__": main()