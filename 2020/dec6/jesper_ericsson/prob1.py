import re

def read_answers(filename):
    group_answer = [set()]
    group_ind = 0
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:

            if string.rstrip() == '':
                group_answer.append(set())
                group_ind += 1
            else:
                for letter in string.rsplit()[0]:
                   group_answer[group_ind].add(letter)
    return group_answer

def sum_of_answers(group_answers):
    sum_answers = 0
    for answers in group_answers:
            sum_answers += len(answers)
    return sum_answers


def main():
    group_answers = read_answers('testdata.csv')
    # group_answers = read_answers('data.csv')

    sum_answers = sum_of_answers(group_answers)
    print('Part1 sum of group answers: %i' %sum_answers)

if __name__ == "__main__": main()