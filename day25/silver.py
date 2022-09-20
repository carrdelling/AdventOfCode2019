from src.intcode import IntCode


def solve(program):

    instructions = [
        'south',
        'west',
        'south',
        'take shell',
        'north',
        'north',
        'take weather machine',
        'west',
        'south',
        'east',
        'take candy cane',
        'west',
        'north',
        'east',
        'south',
        'east',
        'east',
        'south',
        'take hypercube',
        'south',
        'south',
        'inv',
        'east',
        'inv'
    ]

    """
    notes:
    
    A loud, robotic voice says "Analysis complete! You may proceed." and you enter the cockpit.
    Santa notices your small droid, looks puzzled for a moment, realizes what has happened, and radios your ship directly.
    "Oh, hello! You should be able to get in by typing 4722720 on the keypad at the main airlock."

    """

    code = []
    for ins in instructions:
        for c in ins:
            code.append(ord(c))
        code.append(10)

    game = IntCode(program, inputs=code)

    try:
        game.run()
        screen = ''.join(chr(x) for x in game.outputs)
        print(screen)
        print('*' * 80)
    except:
        screen = ''.join(chr(x) for x in game.outputs)
        print(screen)
        print('*' * 80)


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')
        program = [int(n) for n in data]

    solve(program)


if __name__ == "__main__":

    main()
