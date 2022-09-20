
class IntCode:

    N_PARAMETERS = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 1,
        99: 0
    }

    def __init__(self, program, inputs=None):

        MEM_SIZE = 10000

        self.ip = 0
        self.relative_base = 0
        self.program = list(program) + [0] * MEM_SIZE
        self.inputs = [x for x in inputs] if inputs is not None else []
        self.outputs = []
        self.halted = False

    def __repr__(self):
        msg = f'***\n{self.ip}\n' + ','.join(map(str, self.outputs)) + '\n' + ','.join(map(str, self.inputs)) + '\n'
        return msg

    def run(self):

        if self.halted:
            return None

        opcode = -1
        while opcode != 99:
            opcode = self.run_one()

        if opcode == 99:
            self.halted = True

        return self.outputs

    def run_block(self):

        if self.halted:
            return None

        opcode = -1
        while opcode not in {99, 4}:
            opcode = self.run_one()

        if opcode == 99:
            self.halted = True

        return self.outputs

    def run_network(self):

        if self.halted:
            return None

        opcode = -1
        while opcode not in {99, 3}:
            opcode = self.run_one()

        if opcode == 99:
            self.halted = True

        return self.outputs

    def run_one(self):

        # parse opcode and parameters
        opcode, parameters = self.parse_instruction()

        # print(f"IP is {self.ip}, opcode is ")

        # apply operation

        # <END> op
        if opcode == 99:
            return 99

        elif opcode in {1}:
            # print(f"Performing {opcode} with values {parameters}")
            aa = parameters[0]
            bb = parameters[1]
            v = aa + bb
            # print(f"Storing {v} into {parameters[2]}")
            self.program[parameters[2]] = v

        elif opcode in {2}:
            # print(f"Performing {opcode} with values {parameters}")
            aa = parameters[0]
            bb = parameters[1]
            v = aa * bb
            # print(f"Storing {v} into {parameters[2]}")
            self.program[parameters[2]] = v

        elif opcode in {3}:
            # print(f"Writing input {self.inputs[0]} into address {parameters[0]}")
            self.program[parameters[0]] = self.inputs[0]
            self.inputs = self.inputs[1:]

        elif opcode in {4}:
            # print(f"Outputting {parameters[0]}")
            self.outputs.append(parameters[0])

        elif opcode in {5}:
            if parameters[0] != 0:
                # print(f"Jumping to {parameters[1]}")
                self.ip = parameters[1]
            else:
                pass
                # print(f"Not jumping {parameters[0]}")

        elif opcode in {6}:
            if parameters[0] == 0:
                # print(f"Jumping to {parameters[1]}")
                self.ip = parameters[1]
            else:
                pass
                # print(f"Not jumping {parameters[0]}")

        elif opcode in {7}:
            if parameters[0] < parameters[1]:
                self.program[parameters[2]] = 1
                # print(f"{parameters[0]} is lower than {parameters[1]}")
            else:
                self.program[parameters[2]] = 0
                # print(f"{parameters[0]} is NOT lower than {parameters[1]}")

        elif opcode in {8}:
            if parameters[0] == parameters[1]:
                self.program[parameters[2]] = 1
                # print(f"{parameters[0]} is equal than {parameters[1]}")
            else:
                self.program[parameters[2]] = 0
                # print(f"{parameters[0]} is NOT equal than {parameters[1]}")

        elif opcode in {9}:
            self.relative_base += parameters[0]
        else:
            # panic
            assert False, f"Wrong opcode {opcode}"

        return opcode

    def parse_opcode(self):

        opcode = self.program[self.ip]
        real_op = opcode % 100

        self.ip += 1

        return opcode, real_op

    def parse_instruction(self):

        # read next int, parse as opcode
        opcode, op = self.parse_opcode()

        # modes
        modes = str(opcode)[:-2] if opcode > 99 else ''
        modes = {i: x for i, x in enumerate(modes[::-1])}

        params = []

        n_params = self.N_PARAMETERS.get(op, 0)
        for i in range(n_params):
            v = self.program[self.ip]
            self.ip += 1

            m = modes.get(i, '0')

            # literal mode
            if i == (n_params - 1) and op in {1, 2, 7, 8}:
                if m == '2':
                    params.append(v + self.relative_base)
                else:
                    params.append(v)
            if i == 0 and op in {3}:
                if m == '2':
                    params.append(v + self.relative_base)
                else:
                    params.append(v)

            # interpreted mode
            if m == '0':
                params.append(self.program[v])
            elif m == '1':
                params.append(v)
            elif m == '2':
                params.append(self.program[v + self.relative_base])
            else:
                assert False, f"Wrong parameter mode {i} {opcode}"

        # print(f"op: {op} params: {params}")

        return op, params


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    m = IntCode(program, list([1] * 5))
    output = m.run()

    print(output)


if __name__ == "__main__":

    main()
