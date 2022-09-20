from collections import defaultdict
from itertools import product

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_neighbors(x, y):

    for i, d in enumerate(DIRS):
        yield x + d[0], y + d[1]


def evolve(planet):

    new_planet = defaultdict(lambda: '.')
    for x, y in product(range(5), repeat=2):
        bugs = 0

        for nx, ny in get_neighbors(x, y):
            bugs += 1 if planet[(nx, ny)] == '#' else 0

        if planet[(x, y)] == '#':
            new_planet[(x, y)] = '#' if bugs == 1 else '.'

        if planet[(x, y)] == '.':
            new_planet[(x, y)] = '#' if bugs in {1, 2} else '.'

    return new_planet


def biodiversity(planet):

    score = sum(2 ** ((x*5) + y)
                for x, y in product(range(5), repeat=2)
                if planet[(x, y)] == '#')
    return score


def print_planet(planet):

    draw = []
    for x in range(5):
        row = []
        for y in range(5):
            row.append(planet[(x, y)])
        draw.append(''.join(row))

    print('\n'.join(draw))


def solve(planet):

    national_geographic = set()
    national_geographic.add(biodiversity(planet))

    solution = None
    while solution is None:

        planet = evolve(planet)

        bio = biodiversity(planet)

        if bio in national_geographic:
            solution = bio
        national_geographic.add(bio)

    return solution


def main():

    planet = defaultdict(lambda: '.')
    with open('input') as in_f:
        for x, line in enumerate(in_f):
            for y, c in enumerate(line.strip()):
                if c == '#':
                    planet[(x, y)] = c

    solution = solve(planet)

    print(solution)


if __name__ == "__main__":

    main()
