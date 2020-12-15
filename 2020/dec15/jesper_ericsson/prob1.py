
def main():
    list_num = [7,12,1,0,16,2]
    list_num = [3,2,1]

    # Part 1
    for current_ind in range((len(list_num)-1),2019):
        if list_num[current_ind] in list_num[:current_ind]:
            last_ind = next(i for i in reversed(range(current_ind)) if list_num[i] == list_num[current_ind])
            list_num.append(current_ind - last_ind)
        else:
            list_num.append(0)
    
    # print(list_num)

    print('The 2020th num is: %i' %list_num[-1])
    list_num = [7,12,1,0,16,2]

    dict_index = {}
    for ind, num in enumerate(list_num):
        dict_index[num] = ind

    next_num = 0
    in_len = len(dict_index)
    for current_ind in range((in_len),30000000-1):
        if next_num in dict_index:
            ind_diff = current_ind - dict_index[next_num]
            dict_index[next_num] = current_ind
            next_num = ind_diff

        else:
            
            dict_index[next_num] = current_ind
            next_num = 0

    print('The 30000000th num is: %i' %next_num)


if __name__ == "__main__": main()