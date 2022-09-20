from collections import defaultdict


def solve(a, b):

    grid = defaultdict(int)

    # first wire
    current = 0, 0
    for step in a:
        _dir, length = step[0], int(step[1:])

        change = {'U': (1, 0),
                  'D': (-1, 0),
                  'L': (0, -1),
                  'R': (0, 1),
                  }[_dir]

        for _ in range(length):
            current = current[0] + change[0], current[1] + change[1]
            grid[current] += 1

    # second wire
    current = 0, 0
    for step in b:
        _dir, length = step[0], int(step[1:])
        change = {'U': (1, 0),
                  'D': (-1, 0),
                  'L': (0, -1),
                  'R': (0, 1),
                  }[_dir]

        for _ in range(length):
            current = current[0] + change[0], current[1] + change[1]
            grid[current] += 2

    # intersections
    solution = min(abs(k[0]) + abs(k[1]) for k, v in grid.items() if v == 3)

    return solution


def main():

    with open('input') as in_f:
        first = in_f.readline().strip().split(',')
        second = in_f.readline().strip().split(',')

    solution = solve(first, second)

    print(solution)


if __name__ == "__main__":

    main()
