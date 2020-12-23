import copy


class Cup:
    def __init__(self, val, next_cup=None):
        self.val = val
        self.next = next_cup


def action(current_cup_id, status, steps):
    current_cup = status[current_cup_id]
    for _ in range(steps):

        # 1 step
        step_1 = current_cup.next
        # 2 more steps
        step_3 = step_1.next.next

        target = current_cup.val - 1

        moved = False
        while not moved:

            if target in [step_1.val, step_1.next.val, step_3.val]:
                target -= 1

            elif target < 0:
                target = max(status.keys())
            else:
                if target in status:
                    target = status[target]
                    moved = True
                else:
                    target -= 1

        # Save the original cup, next to target
        temp = target.next
        # Place step 1 next to target
        target.next = step_1

        # Set previous next of step 3, to currents next (effectively skipping 1-3)
        current_cup.next = step_3.next

        # Place step 3 before original cup next to target
        step_3.next = temp

        current_cup = current_cup.next

    return status


def score(status):
    answer = []
    cup = status[1].next
    for _ in range(len(status)):
        answer.append(str(cup.val))
        cup = cup.next
    return "".join(answer[:-1])


def gen_data_1(input_):
    status = {}

    first_cup_id = input_[0]
    prev_cup = Cup(first_cup_id)
    for val in input_[1:]:

        # Link cups together
        new_cup = Cup(val)
        prev_cup.next = new_cup
        status[prev_cup.val] = prev_cup
        prev_cup = new_cup

    # Add last cup
    prev_cup.next = status[first_cup_id]
    status[prev_cup.val] = prev_cup

    return first_cup_id, status


def gen_data_2(input_):
    status = {}

    first_cup_id = input_[0]
    prev_cup = Cup(first_cup_id)
    for val in input_[1:]:
        # Link cups together
        new_cup = Cup(val)
        prev_cup.next = new_cup
        status[prev_cup.val] = prev_cup
        prev_cup = new_cup

    # Add cups from 10 to 1 million (9 th element is not yet added)
    for idx in range(10, 1000000 + 1):

        # Link cups together
        new_cup = Cup(idx)
        prev_cup.next = new_cup
        status[prev_cup.val] = prev_cup
        prev_cup = new_cup

    # Add last cup linking to first
    prev_cup.next = status[first_cup_id]
    status[prev_cup.val] = prev_cup

    return first_cup_id, status


if __name__ == "__main__":
    input_ = [int(c) for c in "467528193"]

    # Task 1
    first_cup, status = gen_data_1(input_)
    res_1 = action(first_cup, status, 100)
    print(f"Result task 1: {score(res_1)}")

    # Task 2
    first_cup, status = gen_data_2(input_)
    res_2 = action(first_cup, status, 10000000)

    score = res_2[1].next.val * res_2[1].next.next.val
    print(f"Result task 2: {score}")
