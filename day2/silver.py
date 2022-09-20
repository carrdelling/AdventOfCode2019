from src.intcode import IntCode


def solve(program):

    # silver changes
    program[1] = 12
    program[2] = 2

    machine = IntCode(program)

    machine.run()

    return machine.program[0]


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
