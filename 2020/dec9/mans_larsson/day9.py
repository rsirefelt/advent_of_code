import numpy as np

nums = []
with open('inputs/day9') as f:
    for line in f:
        nums.append(int(line.rstrip()))

nums = np.array(nums)
not_in_previous = None
for i in range(25, len(nums)):
    previous = nums[i-25:i]
    in_previous = False
    for prev_num in previous:
        if nums[i] - prev_num in previous:
            in_previous = True
    if not in_previous:
        not_in_previous = nums[i]

print(f'a) {not_in_previous}')

contiguous_nums = None
for i in range(len(nums)):
    for j in range(i+2, len(nums)):
        sum = nums[i:j].sum()
        if sum == not_in_previous:
            contiguous_nums = nums[i:j]
        elif sum > not_in_previous:
            break
print(f'b) {contiguous_nums.min() + contiguous_nums.max()}')
