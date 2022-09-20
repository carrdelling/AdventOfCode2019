from src.intcode import IntCode


def solve(program):

    m = IntCode(program, [0])
    outputs = m.run()

    tiles = list(zip(outputs[::3], outputs[1::3], outputs[2::3]))
    blocks = sum(1 for x in tiles if x[2] == 2)

    return blocks


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
