import regex as re


def task(task_=1):
    with open("input") as f:
        valid_count = 0
        for line in f:
            pattern = re.findall("([0-9]*)-([0-9]*) ([a-z]): (.*)", line)[0]
            lower_lim, upper_lim, letter, string_ = pattern
            lower_lim = int(lower_lim)
            upper_lim = int(upper_lim)

            if task_ == 1:
                count = string_.count(letter)
                if count >= lower_lim and count <= upper_lim:
                    valid_count += 1
            else:
                pos_1 = letter == string_[lower_lim - 1]
                pos_2 = letter == string_[upper_lim - 1]
                if pos_1 + pos_2 == 1:
                    valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    task()
    task(2)
