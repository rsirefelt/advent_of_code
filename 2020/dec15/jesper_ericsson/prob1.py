def naive_solutuion(list_num, end_num):
    for current_ind in range((len(list_num)-1),end_num -1):
        if list_num[current_ind] in list_num[:current_ind]:
            last_ind = next(i for i in reversed(range(current_ind)) if list_num[i] == list_num[current_ind])
            list_num.append(current_ind - last_ind)
        else:
            list_num.append(0)
    return list_num[-1]

def better_solution(list_num, end_num):
    dict_index = {}
    for ind, num in enumerate(list_num):
        dict_index[num] = ind

    next_num = 0
    in_len = len(dict_index)
    for current_ind in range((in_len),end_num-1):
        if next_num in dict_index:
            ind_diff = current_ind - dict_index[next_num]
            dict_index[next_num] = current_ind
            next_num = ind_diff
        else:            
            dict_index[next_num] = current_ind
            next_num = 0
    return next_num

def main():
    list_num = [7,12,1,0,16,2]

    # Part 1
    last_num = naive_solutuion(list_num.copy(), 2020)
    print('The 2020th num is: %i' %last_num)

    # Part 2
    last_num = better_solution(list_num, 30000000)
    print('The 30000000th num is: %i' %last_num)


if __name__ == "__main__": main()