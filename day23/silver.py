from src.intcode import IntCode


class Computer:

    def __init__(self, program, _id):

        self.id = _id
        self.m = IntCode(program)
        self.m.inputs.append(_id)

    def epoch(self):

        output = self.m.run_network()
        self.m.outputs = []

        # process the messages
        buffer = []

        for idx in range(0, len(output), 3):
            message = (output[idx], output[idx+1], output[idx+2])
            buffer.append(message)

        return buffer

    def receive(self, x=None, y=None):

        if x is None:
            self.m.inputs.append(-1)
        else:
            self.m.inputs.append(x)
            self.m.inputs.append(y)


def solve(program):

    network = []

    # build the network
    for idx in range(50):
        network.append(Computer(list(program), idx))

    counter = 0
    destinations = {}
    while True:
        # run an epoch

        new_messages = []
        for idx in range(50):
            messages = network[idx].epoch()

            for m in messages:
                new_messages.append(m)

        # send new inputs
        seen = set()

        for addr, x, y in new_messages:

            if addr == 255:
                print(counter)
                return y

            seen.add(addr)
            network[addr].receive(x, y)

            destinations[addr] = destinations.get(addr, 0) + 1

        for idx in range(50):
            if idx not in seen:
                network[idx].receive()

        counter += 1


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solution = solve(program)

    print(solution)


if __name__ == "__main__":

    main()
