from src.intcode import IntCode


class Droid:

    def __init__(self, _program):

        self.controller = IntCode(list(_program))
        self.steps = 0
        self.blocks = set()

        self.x = 0
        self.y = 0

        self.visited = set()

    def action(self, movement):

        self.controller.inputs.append(movement)
        outputs = self.controller.run_block()
        self.controller.outputs = []

        assert len(outputs) == 1, f"More than one output {len(outputs)}"

        sensor = outputs[0]
        self.steps += 1

        if sensor == 0:
            self.blocks.add(movement)
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


def solve(program):

    states = []
    min_steps = 9999999
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
            print(len(states), current_steps, min_steps)
        if d.steps > min_steps:
            continue

        if s == 2:
            min_steps = min(min_steps, d.steps)
            continue

        if s < 2:

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

                nd = make_copy(d)
                ns = nd.action(i)
                states.append((nd, i, ns))

    return min_steps


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
