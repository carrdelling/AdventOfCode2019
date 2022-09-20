from src.intcode import IntCode
from itertools import product
from collections import defaultdict


def solve(program):

    m = IntCode(program)

    assembly = [
        'NOT A J',
        'NOT B T',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'WALK'
    ]

    code = []

    for ins in assembly:
        for c in ins:
            code.append(ord(c))
        code.append(10)

    m.inputs += code

    outputs = m.run()

    print(list(map(chr, outputs[:-1])))

    return outputs[-1]


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
