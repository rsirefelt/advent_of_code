def main():
    valid_passwords = 0
    input_data = []
    # with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            input_data.append(string.rstrip().replace('-',' ').replace(': ',' ').split(' '))

    for min_num, max_num, letter, password in input_data:
        num_of_letter = password.count(letter)
        if num_of_letter >= int(min_num) and num_of_letter <= int(max_num):
            valid_passwords += 1

    print(valid_passwords)

if __name__ == "__main__": main()
	