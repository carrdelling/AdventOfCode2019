from src.intcode import IntCode


def solve(program):

    m = IntCode(program)

    assembly = [
        'NOT B J',
        'NOT C T',
        'OR T J',
        'AND H J',
        'NOT A T',
        'OR T J',
        'AND D J',
        'RUN'
    ]

    code = []

    for ins in assembly:
        for c in ins:
            code.append(ord(c))
        code.append(10)

    m.inputs += code

    outputs = m.run()

    cout = ''.join(list(map(chr, outputs[:-1])))

    print(cout)

    return outputs[-1]


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
