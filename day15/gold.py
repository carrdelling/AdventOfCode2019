from src.intcode import IntCode
from collections import defaultdict


class Droid:

    MAP = defaultdict(int)

    def __init__(self, _program):

        self.controller = IntCode(list(_program))
        self.steps = 0
        self.blocks = set()

        self.x = 0
        self.y = 0

        self.visited = set()
        Droid.MAP[(self.x, self.y)] = 1

    def action(self, movement):

        self.controller.inputs.append(movement)
        outputs = self.controller.run_block()
        self.controller.outputs = []

        assert len(outputs) == 1, f"More than one output {len(outputs)}"

        sensor = outputs[0]
        self.steps += 1

        if sensor == 0:
            self.blocks.add(movement)
            if movement == 1:
                Droid.MAP[(self.x-1, self.y)] = sensor
            if movement == 2:
                Droid.MAP[(self.x+1, self.y)] = sensor
            if movement == 3:
                Droid.MAP[(self.x, self.y-1)] = sensor
            if movement == 4:
                Droid.MAP[(self.x, self.y+1)] = sensor
        else:
            if movement == 1:
                self.x -= 1
            if movement == 2:
                self.x += 1
            if movement == 3:
                self.y -= 1
            if movement == 4:
                self.y += 1

            self.visited.add((self.x, self.y))
            Droid.MAP[(self.x, self.y)] = sensor

        return sensor


def make_copy(old):

    d = Droid([])
    d.controller.program = list(old.controller.program)
    d.controller.ip = old.controller.ip
    d.controller.relative_base = old.controller.relative_base
    d.steps = old.steps
    d.blocks = set(old.blocks)

    d.x = old.x
    d.y = old.y

    d.visited = set(old.visited)

    return d


def print_map():

    x_values = {x[0] for x in Droid.MAP.keys()}
    y_values = {y[1] for y in Droid.MAP.keys()}
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    for y in range(max_y, min_y-1, -1):
        row = []
        for x in range(max_x, min_x, -1):
            row.append(Droid.MAP[(x, y)])
        print("".join({'0': ' ', '1': '1', '2': '2', '3': '3'}[x] for x in map(str, row)))


def solve(program):

    states = []
    current_steps = 0

    for i in range(1, 5):

        d = Droid(program)
        s = d.action(i)
        states.append((d, i, s))

    while len(states) > 0:

        current = states[0]
        states = list(states[1:])
        d, last, s = current

        if d.steps > current_steps:
            current_steps = d.steps
            print(len(states), current_steps, len(Droid.MAP))

        for i in range(1, 5):
            if i in d.blocks:
                continue

            target = [d.x, d.y]
            if i == 1:
                target[0] -= 1
            if i == 2:
                target[0] += 1
            if i == 3:
                target[1] -= 1
            if i == 4:
                target[1] += 1

            if tuple(target) in d.visited:
                continue
            if tuple(target) in Droid.MAP:
                continue

            nd = make_copy(d)
            ns = nd.action(i)
            states.append((nd, i, ns))

    print_map()

    # flow the map
    oxygen = -1
    changed = True

    def _neighbours(p):
        yield p[0] - 1, p[1]
        yield p[0] + 1, p[1]
        yield p[0], p[1] - 1
        yield p[0], p[1] + 1

    sources = [k for k, v in Droid.MAP.items() if v == 2]

    while changed:
        changed = False
        new_sources = []
        for s in sources:
            for n in _neighbours(s):
                if Droid.MAP[n] == 1:
                    Droid.MAP[n] = 3
                    changed = True
                    new_sources.append(n)

        sources = list(new_sources)
        oxygen += 1

    print_map()

    return oxygen


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
