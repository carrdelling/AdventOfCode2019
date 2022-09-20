from itertools import product

from src.intcode import IntCode


def solve(initial_program):

    target = 19690720
    solution = -1

    for n, v in product(range(100), repeat=2):
        program = initial_program[:]
        program[1] = n
        program[2] = v

        pc = IntCode(program)
        pc.run()
        output = pc.program[0]

        if output == target:
            solution = n * 100 + v
            break

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
