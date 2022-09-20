from collections import defaultdict
from src.intcode import IntCode


rotation = {
    (0, -1): {0: (-1, 0), 1: (1, 0)},
    (0, 1): {0: (1, 0), 1: (-1, 0)},
    (-1, 0): {0: (0, 1), 1: (0, -1)},
    (1, 0): {0: (0, -1), 1: (0, 1)}
}


def print_hull(hull):

    x_values = {x[0] for x in hull.keys()}
    y_values = {y[1] for y in hull.keys()}
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    for y in range(max_y, min_y-1, -1):
        row = []
        for x in range(max_x, min_x, -1):
            row.append(hull[(x, y)])
        print("".join({'0': ' ', '1': '1'}[x] for x in map(str, row)))


def solve(program):

    # input {0: black, 1: white}
    # output1 {0: black, 1: white}
    # output2 {0: left, 1: right}

    m = IntCode(program, [1])

    hull = defaultdict(int)
    position = 0, 0
    orient = (0, 1)

    while not m.halted:
        _ = m.run_block()

        if m.halted:
            continue

        output = m.run_block()
        color, direction = output

        # paint
        hull[position] = color

        # rotate
        orient = rotation[orient][direction]

        # move one
        position = (position[0] + orient[0], position[1] + orient[1])

        # clean output
        m.outputs = []

        # feed new input
        current_color = hull[position]
        m.inputs.append(current_color)

    painted = len(hull)

    print_hull(hull)

    return painted


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    _ = solve(program)


if __name__ == "__main__":

    main()
