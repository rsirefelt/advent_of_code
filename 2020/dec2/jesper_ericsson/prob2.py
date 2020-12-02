def main():
    valid_passwords = 0
    input_data = []
    # with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            # print(string)
            input_data.append(string.rstrip().replace('-',' ').replace(': ',' ').split(' '))

    for pos1, pos2, letter, password in input_data:
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1
        correct1 = password[pos1] == letter
        correct2 = password[pos2] == letter

        if (correct1 and not correct2) or (correct2 and not correct1):
            valid_passwords += 1

    print(valid_passwords)

if __name__ == "__main__": main()