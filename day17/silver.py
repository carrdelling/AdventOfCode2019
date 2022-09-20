from src.intcode import IntCode
from collections import defaultdict


def solve(program):

    m = IntCode(program)

    output = m.run()

    space = ''.join([chr(x) for x in output])
    print(space)
    spacemap = defaultdict(int)

    x, y = 0, 0
    for c in output:
        if c != 10:
            spacemap[(x, y)] = c
            y += 1
        else:
            x += 1
            y = 0

    intersections = []
    for (x, y), v in list(spacemap.items())[:]:
        if v != 35:
            continue

        if all([spacemap[(x-1, y)] == 35, spacemap[(x+1, y)] == 35,
                spacemap[(x, y+1)] == 35, spacemap[(x, y+1)] == 35,]):
            intersections.append((x, y))

    alignment = sum(x * y for x, y in intersections)

    return alignment


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
