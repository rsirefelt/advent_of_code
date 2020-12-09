import numpy as np

def find_first_error(number_list, check_length):
    for ind in range (check_length, len(number_list)):
        is_in_previous = False

        for check_num in number_list[ind - check_length:ind]:
            if number_list[ind] - check_num in number_list[ind - check_length:ind]:
                is_in_previous = True
                break

        if not is_in_previous:
            return(number_list[ind])

def find_continues_numbers(number_list, wanted_sum):
    list_length = len(number_list)
    for ind in range(list_length):
        for sum_size in range(2,list_length-ind):
            if np.sum(number_list[ind:ind+sum_size]) == wanted_sum:
                min_num = np.min((number_list[ind:ind+sum_size]))
                max_num = np.max((number_list[ind:ind+sum_size]))
                return min_num + max_num


def main():
    number_list = np.genfromtxt('testdata.csv', delimiter=',')
    check_length = 5
    number_list = np.genfromtxt('data.csv', delimiter=',')
    check_length = 25

    first_error = find_first_error(number_list, check_length)
    print('First non matching num: %i' %first_error)

    continues_sum = find_continues_numbers(number_list, first_error )
    print('Sum of the continues numbers: %i' %continues_sum)

if __name__ == "__main__": main()