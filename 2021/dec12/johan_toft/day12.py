import sys


def load_data(filename):
    with open(filename) as f:
        data = f.read()
    return [(x.split('-')[0], x.split('-')[1]) for x in data.splitlines()]



def main():
    data = load_data('real_input.txt')

    all_connections = {}

    for start, end in data:
        if start not in all_connections:
            all_connections[start] = []
        if end not in all_connections:
            all_connections[end] = []
        all_connections[start].append(end)
        all_connections[end].append(start)
    print(all_connections)

    # Keep track of all upper
    all_upper = set()
    for key in all_connections:
        if key.isupper():
            all_upper.add(key)

    # Explore all possible paths

    # Check if valid path

    def valid_path(path):
        # Must only contain every non capital letter once

        # Check if all letters are unique
        lower_case_letters = set()
        upper_case_letters = set()
        for letter in path:
            if letter.islower() and letter not in lower_case_letters:
                lower_case_letters.add(letter)
            elif letter.islower():
                return False
            elif letter.isupper():
                upper_case_letters.add(letter)
        upper_ok = len(upper_case_letters) == len(all_upper)
        if path[0] == 'start' and path[-1] == 'end':
            return upper_ok
        else:
            return False

    def valid_lower(path):
        # Must only contain every non capital letter once
        lower_case_letters = set()
        for letter in path:
            if letter.islower() and letter not in lower_case_letters:
                lower_case_letters.add(letter)
            elif letter.islower():
                return False
        return True

    def explore_path(path, small_visited_twice, paths=set()):
        if path[-1] == 'end':
            return path
        for next_node in all_connections[path[-1]]:

            # next node cannot be start
            if next_node == 'start':
                continue

            if (next_node.islower() and next_node not in path or not small_visited_twice) or next_node.isupper():
                new_path = path + [next_node]

                # If this small was visited before, trigger condition
                if next_node in path and next_node.islower():
                    next_small_visited_twice = True
                else:
                    next_small_visited_twice = small_visited_twice

                full_path = explore_path(new_path, next_small_visited_twice)
                if full_path and not isinstance(full_path, set):
                    paths.add(",".join(full_path))
        return paths

    paths = explore_path(['start'], False)

    print(len(paths))


if __name__ == '__main__':
    main()
