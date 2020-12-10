import numpy as np


def contains_bag(rules, bags):
    number_of_bags = 0
    if 'shiny gold' in bags:
        number_of_bags = 1
    else:
        for bag in bags:
            number_of_bags += contains_bag(rules, rules[bag])
    if number_of_bags > 0:
        return 1
    else:
        return 0

def count_combinations(adapter_list):
    combinations_dict = {}
    
    
    combinations_dict[adapter_list[0]] = 1
    combinations_dict[adapter_list[1]] = 1
    
    # It most be reach by the adapter befor 
    combinations_dict[adapter_list[2]] = 1
    #Check if it works with the first one too
    if adapter_list[2] - adapter_list[0] <= 3:
        combinations_dict[adapter_list[2]] += 1

    for adapter_ind in range(3, len(adapter_list)):
        adapter = adapter_list[adapter_ind] 
        combinations_dict[adapter] = 0
        
        for prev_adapter in adapter_list[adapter_ind-3:adapter_ind]:
            if adapter - prev_adapter <= 3:
                combinations_dict[adapter] += combinations_dict[prev_adapter]
    
    return combinations_dict[adapter_list[-1]]

def main():
    adapter_list = np.genfromtxt('testdata.csv', delimiter=',')

    adapter_list = np.genfromtxt('data.csv', delimiter=',')


    adapter_list.sort()
    adapter_list = np.append(0, adapter_list)
    adapter_list = np.append(adapter_list, adapter_list[-1]+3)
    volt_diff = np.diff(adapter_list)
    _ , counts = np.unique(volt_diff, return_counts=True)

    print('The product of the differences: %i' %(counts[0]*counts[1]))

    combinations = count_combinations(adapter_list)
    print('Total number of combinations: %i' %combinations)


if __name__ == "__main__": main()