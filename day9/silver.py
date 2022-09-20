from src.intcode import IntCode


def solve(program):

    m = IntCode(program, [1])
    output = m.run()

    return output[0]


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
