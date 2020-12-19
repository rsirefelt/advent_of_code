import string, re

class I(int):
    def __add__(self, other):
        return I(int(self) * int(other))
    def __sub__(self, other):
        return I(int(self) + int(other))
    def __mul__(self, other):
        return I(int(self) + int(other))

def calc_expr1(expr):
    trans = str.maketrans('*+', '+-')
    return eval(re.sub(r'(\d)', r'I(\1)', expr).translate(trans))

def calc_expr2(expr):
    trans = str.maketrans('*+', '+*')
    return eval(re.sub(r'(\d)', r'I(\1)', expr).translate(trans))

lines = open('input').readlines()
print(sum(map(calc_expr1, lines)))
print(sum(map(calc_expr2, lines)))
