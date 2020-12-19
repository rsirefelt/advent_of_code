import re


def extract_expr_idx(line):
    open_ = -1
    for i, c in enumerate(line):
        if c == "(":
            open_ = i
        elif open_ != -1 and c == ")":
            close = i
            break

    if open_ != -1:
        return [open_, close]
    else:
        return None


def calc_expr1(expr):
    val = int(re.match(r"(\d+)", expr).groups()[0])
    for exp in re.finditer(r"(\+|\*)(\d+)", expr):
        if exp.groups()[0] == "*":
            val *= int(exp.groups()[1])
        else:
            val += int(exp.groups()[1])
    return val


def calc_expr2(expr):
    while a := re.search(r"(\d+)\+(\d+)", expr):
        val = int(a.groups()[0]) + int(a.groups()[1])
        expr = expr.replace(expr[a.start(0) : a.end(0)], str(val), 1)

    while a := re.search(r"(\d+)\*(\d+)", expr):
        val = int(a.groups()[0]) * int(a.groups()[1])
        expr = expr.replace(expr[a.start(0) : a.end(0)], str(val), 1)

    return val


def sum_expressions(calc_expr):
    values = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace(" ", "").rstrip()
            while expr_idx := extract_expr_idx(line):
                val = calc_expr(line[expr_idx[0] + 1 : expr_idx[1]])
                line = line.replace(line[expr_idx[0] : expr_idx[1] + 1], str(val), 1)
            values.append(calc_expr(line))

    return sum(values)


print(f"1) Sum of resulting values {sum_expressions(calc_expr1)}")
print(f"2) Sum of resulting values {sum_expressions(calc_expr2)}")
