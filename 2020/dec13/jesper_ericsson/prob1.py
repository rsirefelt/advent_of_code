import numpy as np

def read_tabell(filename):
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        earliest_departure = int(data_lines[0].rstrip())
        bus_ids = data_lines[1].rstrip().split(',')

    return earliest_departure, bus_ids

def main():
    earliest_departure, bus_ids = read_tabell('testdata.csv')
    earliest_departure, bus_ids = read_tabell('data.csv')

    # Part 1
    print(earliest_departure)
    print(bus_ids)

    earliest_bus = earliest_departure +1000000000
    earliest_bus_id = 0
    for bus_id in bus_ids:
        if not bus_id == 'x':
            bus_id = int(bus_id)
            bus_depature = np.ceil(earliest_departure/bus_id) * bus_id

            if bus_depature < earliest_bus:
                earliest_bus = bus_depature
                earliest_bus_id = bus_id
    wait_time = earliest_bus - earliest_departure

    print('Part1, Product of waittime and bus id: %i' %(wait_time * earliest_bus_id))

    # # Part2
    diff_id_list = []
    max_id = 0
    max_id_diff =0
    for time_diff,bus_id in enumerate(bus_ids):
        if not bus_id == 'x':
            bus_id = int(bus_id)
            diff_id_list.append((time_diff, bus_id))
            if bus_id > max_id:
                max_id = bus_id
                max_id_diff = time_diff
    
    # Print values for C++ implementation
    print('Max id: ' , max_id)
    print('Max id diff: ' , max_id_diff)
    diffs, reduced_bus_ids = zip(*diff_id_list)
    print('Diffs: ' +str( diffs))
    print('Bus Ids: ' +str( reduced_bus_ids))

    # Took too long time to solve. Implemented the solver in C++ instead.

    # t = (100000000000000 // max_id) * max_id - max_id_diff
    # # t = 0
    # while True:
    #     all_true = True
    #     for diff,bus_id in diff_id_list:
    #         if not (t + diff)% bus_id == 0:
    #             all_true = False
    #             break
        
    #     if all_true:
    #         print(t)
    #         break

    #     t += max_id
    # distance_2 = loop_instructions2(instructions)
    # print('Part2, The manhatan distance is: %i' %distance_2)


if __name__ == "__main__": main()