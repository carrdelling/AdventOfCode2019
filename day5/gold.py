from src.intcode import IntCode


def solve(initial_program):

    inputs = [5]

    machine = IntCode(initial_program, inputs)
    solution = machine.run()

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    for s in solution:
        print(s)


if __name__ == "__main__":

    main()
