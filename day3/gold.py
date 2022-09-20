
def solve(a, b):

    a_grid = {}
    b_grid = {}

    # first wire
    current = 0, 0
    signal = 0
    for step in a:
        _dir, length = step[0], int(step[1:])

        change = {'U': (1, 0),
                  'D': (-1, 0),
                  'L': (0, -1),
                  'R': (0, 1),
                  }[_dir]

        for _ in range(length):
            signal += 1
            current = current[0] + change[0], current[1] + change[1]
            a_grid[current] = min(signal, a_grid.get(current, 9E99))

    # second wire
    current = 0, 0
    signal = 0
    for step in b:
        _dir, length = step[0], int(step[1:])
        change = {'U': (1, 0),
                  'D': (-1, 0),
                  'L': (0, -1),
                  'R': (0, 1),
                  }[_dir]

        for _ in range(length):
            signal += 1
            current = current[0] + change[0], current[1] + change[1]
            b_grid[current] = min(signal, b_grid.get(current, 9E99))

    # signals
    locs = {x for x in a_grid.keys()} & {x for x in b_grid.keys()}
    solution = min(a_grid[l] + b_grid[l] for l in locs)

    return solution


def main():

    with open('input') as in_f:
        first = in_f.readline().strip().split(',')
        second = in_f.readline().strip().split(',')

    solution = solve(first, second)

    print(solution)


if __name__ == "__main__":

    main()
