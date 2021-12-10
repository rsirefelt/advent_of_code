from collections import deque


def parse_input(file_path='./input_day10.txt'):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    return lines


class SyntaxChecker:
    pairs = {'<': '>', '[': ']', '{': '}', '(': ')'}
    error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    def __init__(self):
        self.expected = deque()

    def check_line(self, line):
        self.expected.clear()
        for char in line:
            if char in self.pairs:
                self.expected.appendleft(self.pairs[char])
            else:
                expect = self.expected.popleft()
                if char != expect:
                    # print(f'Expected {expect}, got {char}')
                    return char 
        return list(self.expected)

    def score_corrupted_lines(self, lines):
        score = 0
        for line in lines:
            output = self.check_line(line)
            if isinstance(output, str):
                score += self.error_scores[output]
        return score

    def score_autocompletion(self, lines):
        scores = []
        for line in lines:
            output = self.check_line(line)
            if isinstance(output, list):
                score = 0
                for char in output:
                    score *= 5
                    score += self.completion_scores[char]
                scores.append(score)

        winner = sorted(scores)[len(scores)//2]
        print(sorted(scores))
        return winner


if __name__ == '__main__':
    lines = parse_input()

    checker = SyntaxChecker()

    # Part I
    print(checker.score_corrupted_lines(lines))

    # Part II
    print(checker.score_autocompletion(lines))
