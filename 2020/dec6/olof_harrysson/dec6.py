with open("input.txt") as f:
  lines = f.read().split('\n\n')
  lines[-1] = lines[-1].rstrip('\n')  # Remove last newline

# Part1
answers = [''.join(set(line.replace('\n', ''))) for line in lines]
answer = len(''.join(answers))
print(answer)

# Part2
from functools import reduce
sum_common = 0
for group in lines:
  common = reduce(lambda common, x: set(common).intersection(set(x)),
                  group.split('\n'))
  sum_common += len(common)

print(sum_common)
