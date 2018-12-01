import csv
from collections import defaultdict


def main():
    sum = 0
    seen = set()
    seen.add(0)
    while True:
        #with open('testdata.csv', 'r') as f:
        with open('data.csv', 'r') as f:

        # reader = csv.reader(f)
            for line in f:
                data_line = line.rstrip().split(', ')
                for int_string in data_line:
                    print(sum)
                    sum += int(int_string)
                    if sum not in seen:
                        seen.add(sum)
                    else:
                        print('Summa: ', sum)
                        return


    print('End: ', sum)

if __name__ == "__main__": main()
	