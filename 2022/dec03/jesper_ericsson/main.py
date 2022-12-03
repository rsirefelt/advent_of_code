import os


def get_prio(item):
    if item == item.upper():
        return ord(item) - 64 + 26
    else:
        return ord(item) - 96


def prob1(rucksacks):
    tot_prio = 0
    for rucksack in rucksacks:
        rucksack = rucksack.rstrip()
        middle = int(len(rucksack) / 2)
        compart1 = rucksack[:middle]
        compart2 = rucksack[middle:]
        common_item = set(compart1).intersection(compart2).pop()
        tot_prio += get_prio(common_item)

    print(f"Total prio prob 1: {tot_prio}")


def prob2(rucksacks):
    tot_prio = 0
    # print(rucksacks)
    num_rucksacks = len(rucksacks)
    for rucksack_ind in range(0, num_rucksacks, 3):
        common_item = (
            set(rucksacks[rucksack_ind].rstrip())
            .intersection(rucksacks[rucksack_ind + 1].rstrip())
            .intersection(rucksacks[rucksack_ind + 2].rstrip())
            .pop()
        )
        tot_prio += get_prio(common_item)

    print(f"Total prio prob 2: {tot_prio}")


def main():
    dir = os.path.dirname(__file__)
    filename = dir + "/testdata.csv"
    filename = dir + "/data.csv"

    with open(filename, "r") as f:
        rucksacks = f.readlines()

    prob1(rucksacks)
    prob2(rucksacks)


if __name__ == "__main__":
    main()
