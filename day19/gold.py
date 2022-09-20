from src.intcode import IntCode


def check_point(x, y, program):

    m = IntCode(program, inputs=[x, y])
    outputs = m.run()

    return outputs[0]


def solve(program):

    # we assume the beam has the same shape as in the example
    x = 0
    y = 0

    while check_point(x + 99, y, program) == 0:
        y += 1
        while check_point(x, y + 99, program) == 0:
            x += 1

    solution = x * 10000
    solution += y

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
