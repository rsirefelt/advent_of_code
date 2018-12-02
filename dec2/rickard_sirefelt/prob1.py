from collections import defaultdict

two_letter_count = 0
three_letter_count = 0
with open("dec2/rickard_sirefelt/input.txt", 'r') as f:
    for line in f:
        char_dict = defaultdict(int)
        for char in line:
            char_dict[char] += 1

        found_two = False
        found_three = False
        for char, count in char_dict.items():    
            if count == 2 and not found_two:
                two_letter_count += 1
                found_two = True
            elif count == 3 and not found_three:
                three_letter_count += 1
                found_three = True

print(two_letter_count * three_letter_count)
