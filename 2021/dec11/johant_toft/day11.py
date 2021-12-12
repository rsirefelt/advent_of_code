#

def load_input(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def neighbours(matrix, x, y):
    neighbours = []
    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            if nx == x and ny == y:
                continue
            if nx < 0 or nx >= len(matrix[0]):
                continue
            if ny < 0 or ny >= len(matrix):
                continue
            neighbours.append((nx, ny))
    return neighbours


def step(matrix):
    # Step through the matrix and trigger any octopus that at level 9
    # Mark it as triggered this step.
    # When triggered it will increment its 8 neighbours

    # Loop through matrix

    all_triggered = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            # increase all energy levels by 1
            matrix[y][x] += 1

    def one_step():
        triggered_queue = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                # Check if energy level is 9
                if matrix[y][x] > 9:
                    # Add to triggered queue
                    matrix[y][x] = 0
                    triggered_queue.append((x, y))
                    # Update neighbours
                    for n in neighbours(matrix, x, y):
                        matrix[n[1]][n[0]] += 1
                        if matrix[n[1]][n[0]] > 9:
                            triggered_queue.append(n)
        return triggered_queue

    while True:
        triggered_queue = one_step()
        all_triggered.update(triggered_queue)
        if len(triggered_queue) == 0:
            break

    # Set all triggered to zero
    for t in all_triggered:
        matrix[t[1]][t[0]] = 0
    return all_triggered


def print_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            print(matrix[y][x], end='')
        print('')
    print('')


def main():
    input = load_input('input.txt')

    matrix = []
    for line in input:
        matrix.append([int(x) for x in line])

    num_triggered = 0
    for i in range(20000):
        num_triggered += len(step(matrix))
        # Check if matrix is zero
        if sum([sum(x) for x in matrix]) == 0:
            print('Part 2:', i)
            break
        if i == 99:
            print('Part 1:', num_triggered)

    print(num_triggered)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
