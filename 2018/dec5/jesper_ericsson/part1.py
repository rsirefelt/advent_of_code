
def main():
    input = []

    # with open('testdata.csv', 'r') as f:
    with open('input.txt', 'r') as f:
        for line in f:
            data_line = line.rstrip().lstrip()
        
        index = 0
        while index+1 < len(data_line):
            if (data_line[index] == data_line[index+1].upper() or\
                data_line[index] == data_line[index+1].lower()) and not\
                data_line[index] == data_line[index+1]:

                data_line = data_line[:index] + data_line[index+2:]
                index -= 1
                if index < 0:
                    index = 0
            else:
                index += 1
                
        print(len(data_line))

if __name__ == "__main__": main()
	
