from collections import defaultdict
from itertools import product


def get_neighbors(x, y, m):

    # top neighbours
    if x == 0:
        yield 1, 2, m-1

    if x in {1, 2, 4}:
        yield x-1, y, m

    if x == 3:
        if y == 2:
            for i in range(5):
                yield 4, i, m + 1
        else:
            yield x-1, y, m

    # bottom neighbours
    if x == 4:
        yield 3, 2, m-1

    if x in {0, 2, 3}:
        yield x+1, y, m

    if x == 1:
        if y == 2:
            for i in range(5):
                yield 0, i, m + 1
        else:
            yield x+1, y, m

    # left neighbours
    if y == 0:
        yield 2, 1, m - 1

    if y in {1, 2, 4}:
        yield x, y-1, m

    if y == 3:
        if x == 2:
            for i in range(5):
                yield i, 4, m + 1
        else:
            yield x, y-1, m

    # right neighbours
    if y == 4:
        yield 2, 3, m-1

    if y in {0, 2, 3}:
        yield x, y+1, m

    if y == 1:
        if x == 2:
            for i in range(5):
                yield i, 0, m + 1
        else:
            yield x, y+1, m


def evolve(planet):

    new_planet = defaultdict(lambda: '.')
    with_bugs = {k[2] for k, v in planet.items() if v == '#'}

    for m in range(min(with_bugs) - 1, max(with_bugs) + 2):
        for x, y in product(range(5), repeat=2):

            if (x, y) == (2,2):
                continue

            bugs = 0

            for nx, ny, nm in get_neighbors(x, y, m):
                bugs += 1 if planet[(nx, ny, nm)] == '#' else 0

            if planet[(x, y, m)] == '#':
                new_planet[(x, y, m)] = '#' if bugs == 1 else '.'

            if planet[(x, y, m)] == '.':
                new_planet[(x, y, m)] = '#' if bugs in {1, 2} else '.'

    return new_planet


def solve(planet):

    minutes = 200

    for _ in range(minutes):
        planet = evolve(planet)

    bugs = sum(1 for v in planet.values() if v == '#')

    return bugs


def main():

    planet = defaultdict(lambda: '.')
    with open('input') as in_f:
        for x, line in enumerate(in_f):
            for y, c in enumerate(line.strip()):
                if c == '#':
                    planet[(x, y, 0)] = c

    solution = solve(planet)

    print(solution)


if __name__ == "__main__":

    main()
