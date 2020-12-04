import re

def read_answers(filename):
    group_answer = [{}]
    group_ind = 0
    group_sizes = [0]
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:

            if string.rstrip() == '':
                group_answer.append({})
                group_sizes.append(0)
                group_ind += 1
            else:
                group_sizes[group_ind] += 1
                for letter in string.rsplit()[0]:
                #    print(letter)
                   group_answer[group_ind][letter] = group_answer[group_ind].get(letter,0) + 1
    return zip(group_answer, group_sizes) 


def sum_of_answers(group_answers_size):
    sum_answers = 0
    for answers, size in group_answers_size:
            # print(answers)
            for answer_key in answers:
                # print(answer_key)
                if answers[answer_key] == size:
                    sum_answers+= 1
    return sum_answers


def main():
    group_answers_size = read_answers('testdata.csv')
    group_answers_size = read_answers('data.csv')

    sum_answers = sum_of_answers(group_answers_size)
    print('Part2 valid passwords: %i' %sum_answers)

if __name__ == "__main__": main()