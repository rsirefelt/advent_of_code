import re
import numpy as np


def evaluate_expression(expr, mode=1):
    searchres = re.finditer('\([\d\+\* ]+\)', expr)

    for sr in searchres:
        par_val = evaluate_expression(expr[sr.start(0)+1:sr.end(0)-1], mode=mode)
        expr = expr[:sr.start(0)] + str(par_val) + expr[sr.end(0):]
        return evaluate_expression(expr, mode=mode)

    expr = expr.split(' ')
    val = int(expr[0])
    ind = 1
    if mode == 1:
        while ind < len(expr):
            if expr[ind] == '+':
                val += int(expr[ind+1])
            elif expr[ind] == '*':
                val *= int(expr[ind+1])
            ind += 2
    else:
        prods = []
        while ind < len(expr):
            if expr[ind] == '+':
                val += int(expr[ind+1])
            elif expr[ind] == '*':
                prods.append(val)
                val = int(expr[ind+1])
            ind += 2
        prods.append(val)
        val = np.prod(prods)

    return val


suma = 0
sumb = 0
with open('inputs/day18') as f:
    for line in f:
        suma += evaluate_expression(line.rstrip(), mode=1)
        sumb += evaluate_expression(line.rstrip(), mode=2)


print(f'a) {suma}')
print(f'b) {sumb}')
