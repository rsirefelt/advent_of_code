def main():
    #with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        num_lines = len(data_lines)

        for i_line in range(num_lines):
            string_new = data_lines[i_line]
            for j_line in range(i_line, num_lines):
                string_old = data_lines[j_line]
                num_eq = 0

                for i_char in range(len(string_old)):
                    if string_new[i_char] != string_old[i_char]:
                        num_eq +=1 
                        if num_eq > 1:
                            break
                if num_eq == 1:
                    out_string = ''
                    for i_char in range(len(string_old)):
                        if string_new[i_char] == string_old[i_char]:
                            out_string += string_new[i_char]
                    print(out_string)
                    return


if __name__ == "__main__": main()
	