from src.intcode import IntCode
from itertools import permutations


def amplification(program, thrusters):

    output = 0

    while thrusters:
        inputs = [thrusters.pop(), output]
        machine = IntCode(program, inputs)
        output = machine.run()[0]

    return output


def solve(program):

    scores = [amplification(program, list(order)) for order in permutations([0, 1, 2, 3, 4])]
    solution = max(scores)

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
