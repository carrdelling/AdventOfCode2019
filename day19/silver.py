from src.intcode import IntCode
from itertools import product
from collections import defaultdict


def solve(program):

    space = defaultdict(int)
    for x, y in product(range(50), repeat=2):
        m = IntCode(program, inputs=[x, y])
        outputs = m.run()
        space[(x, y)] = outputs[0]

    in_range = sum(space.values())

    return in_range


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
