from src.intcode import IntCode
from itertools import permutations


def amplification(program, thrusters):

    output = 0
    count = 0

    machines = []

    for i in range(5):
        m = IntCode(program, [thrusters[i % 5]])
        machines.append(m)

    stop = False
    max_score = 0
    while not stop:

        idx = count % 5
        machines[idx].inputs.append(output)

        opcode = -1
        while opcode not in {99, 4}:
            opcode = machines[idx].run_one()

        if machines[idx].outputs:
            output = machines[idx].outputs.pop()


        output = machines[idx].outputs.pop() if machines[idx].outputs else None

        if output is None:
            stop = True
        elif idx == 4:
            max_score = max(max_score, output)
        count += 1

    return max_score


def solve(program):

    scores = [amplification(program, list(order)) for order in permutations([5, 6, 7, 8, 9])]
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
