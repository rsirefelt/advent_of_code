import regex as re


def task(task=1):
    count = 0
    bag_dict = {}
    with open("input") as f:
        lines = list(f.readlines())

        for line in lines:
            line = line.rstrip()
            current_bag, contains = line.split(" contain ")
            # bags --> bag to have everything uniform.
            current_bag = current_bag[:-1]

            # Parse bags, (no other will automatically be parsed as [])
            different_bags = re.findall("([0-9] [a-z ]*)[.,]", contains)

            # Change all bags --> bag
            different_bags = [
                (int(bag[0]), bag[2:-1]) if bag[-1] == "s" else (int(bag[0]), bag[2:])
                for bag in different_bags
            ]
            bag_dict[current_bag] = different_bags

    # Need to loop through again, as all contained bags need to be entered
    if task == 1:
        for bag in bag_dict.keys():
            # Check if current bag contains gold
            count += task1(bag, bag_dict)
    else:
        count = task2("shiny gold bag", bag_dict)
        # Remove the shiny gold bag itself
        count -= 1

    print(count)


def task1(current_bag, bag_dict):
    bags_to_check = bag_dict[current_bag]
    sum_ = 0
    for (count, bag) in bags_to_check:

        if bag == "shiny gold bag":
            sum_ += 1
        else:
            sum_ += task1(bag, bag_dict)
    return sum_ >= 1


def task2(current_bag, bag_dict):
    sum_ = 1
    for count, color in bag_dict[current_bag]:
        sum_ += count * task2(color, bag_dict)
    return sum_


if __name__ == "__main__":
    task(1)
    task(2)
