group_answers = []
group_sizes = []
answers = ''
group_size = 0
with open('inputs/day6') as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            group_answers.append(answers)
            group_sizes.append(group_size)
            answers = ''
            group_size = 0
        else:
            answers += line
            group_size += 1
if len(answers) != 0:
    group_answers.append(answers)
    group_sizes.append(group_size)

count = 0
for answer in group_answers:
    count += len(set(answer))

print(f'a) {count}')

count = 0
for group_size, answer in zip(group_sizes, group_answers):
    for char in set(answer):
        if answer.count(char) == group_size:
            count += 1

print(f'b) {count}')
