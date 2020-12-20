""" Advent of Code 2020 Day 18 """
import abc
import operator


def lexer(s):
    for c in s:
        if c == " ":
            continue
        yield c
    while True:
        yield "\0"


class Node:

    operators = {"+": operator.add, "*": operator.mul}

    def __init__(self, left, right, name):
        self.left = left
        self.right = right
        self.name = name

    def __str__(self, node=None):
        if node is None:
            node = self
        if node.left is None:
            s = ""
        else:
            s = "("
        if isinstance(node.left, Node):
            s += self.__str__(node.left)
        elif isinstance(node.left, str):
            s += node.left
        if node.name:
            s += f" {node.name} "
        if isinstance(node.right, Node):
            s += node.__str__(node.right)
        elif isinstance(node.right, str):
            s += node.left

        if node.right is not None:
            s += ")"
        return s

    def evaluate(self, node=None):
        if node is None:
            node = self
        if node.name in self.operators:
            return self.operators[node.name](
                node.evaluate(node.left), node.evaluate(node.right)
            )
        else:
            return int(node.name)


class BaseParser(abc.ABC):
    def __init__(self):
        self.lexer = None
        self.current = None

    def accept(self, c):
        if isinstance(c, str):
            if self.current == c:
                self.current = next(self.lexer)
                return c
        elif isinstance(c, (list, tuple)):
            if self.current in c:
                idx = c.index(self.current)
                self.current = next(self.lexer)
                return c[idx]

        return False

    def expect(self, c):
        acc = self.accept(c)
        if not acc:
            raise ValueError(f"Unexpected character: {self.current}, expected: {c}")
        return acc

    @abc.abstractmethod
    def last(self):
        """Parsing method for the operator evaluated last. """
        pass

    def digit(self):
        if self.accept("("):
            rh = self.last()
            if self.expect(")"):
                return rh
        d = self.current
        if d.isdigit():
            self.current = next(self.lexer)
            return Node(None, None, d)
        else:
            raise ValueError(f"Invalid digit {d}")

    def parse(self, s):
        self.lexer = lexer(s)
        self.current = next(self.lexer)
        tree = self.last()
        return tree


class SimpleParser(BaseParser):
    """BNF grammar
    <expr>  ::= <expr> + <digit> | <expr> * <digit> | <digit>
    <digit> ::= 0-9 | (<expr>)
    """

    def last(self):
        """Replace if->while and rh=last -> rh=digit
        to go from right to left associate. """
        lh = self.digit()
        node = None
        while op := self.accept(["+", "*"]):
            rh = self.digit()
            if node is None:
                node = Node(lh, rh, op)
            else:
                node = Node(node, rh, op)
        if node is None:
            node = lh
        return node


class AdvancedParser(BaseParser):
    """BNF grammar
    <factor> ::= <factor> * <term> | <term>
    <term> ::= <term> + <digit> | <digit>
    <digit> ::= 0-9 | (<factor>)
    """

    def last(self):
        lh = self.term()
        node = None
        while op := self.accept("*"):
            rh = self.term()
            if node is None:
                node = Node(lh, rh, op)
            else:
                node = Node(node, rh, op)
        if node is None:
            node = lh
        return node

    def term(self):
        lh = self.digit()
        node = None
        while op := self.accept("+"):
            rh = self.digit()
            if node is None:
                node = Node(lh, rh, op)
            else:
                node = Node(node, rh, op)
        if node is None:
            node = lh
        return node


def load_input(input_file):
    with open(input_file, "r") as fp:
        expressions = fp.read().splitlines()

    return expressions


if __name__ == "__main__":
    expressions = load_input("./input_day18.txt")

    # Part I
    parser = SimpleParser()
    res = 0
    for expr in expressions:
        tree = parser.parse(expr)
        res += tree.evaluate()
    print(res)

    # Part II
    parser = AdvancedParser()
    res = 0
    for expr in expressions:
        tree = parser.parse(expr)
        res += tree.evaluate()
    print(res)
