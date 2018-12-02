

def main():
    twos = 0
    threes = 0
    #with open('testdata.csv', 'r') as f:
    with open('data.csv', 'r') as f:
        data_lines = f.readlines()
        for string in data_lines:
            letter_dict = {}
            for letter in string:
                if letter in letter_dict:
                    letter_dict[letter] +=1
                else:
                    letter_dict[letter] = 1
                
            if 2 in letter_dict.values():
                twos += 1
            if 3 in letter_dict.values():
                threes += 1
            
        print(twos * threes)

if __name__ == "__main__": main()
	