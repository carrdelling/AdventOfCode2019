from src.intcode import IntCode


def solve(program):

    m = IntCode(program, [0] * 10000)

    outputs = m.run()

    tiles = list(zip(outputs[::3], outputs[1::3], outputs[2::3]))
    max_score = -1
    for t in tiles:
        if t[0] == -1 and t[1] == 0:
            score = t[2]
            max_score = max(max_score, score)

    return max_score


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    # start the game
    program[0] = 2

    # konami code
    program[1432:1474] = [3] * 42

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
