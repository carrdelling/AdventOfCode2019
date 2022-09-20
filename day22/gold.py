

def solve(rules):

    size = 119315717514047
    shuffles = 101741582076661
    pos = 2020

    a, b = 1, 0

    for action, value in rules:

        if 'new' in action:
            a = -a % size
            b = (size - 1 - b) % size
            continue

        if 'cut' in action:
            b = (b-value) % size
            continue

        if 'increment' in action:
            a = a*value % size
            b = b*value % size
            continue

    r = (b * pow(1 - a, size - 2, size)) % size

    solution = ((pos - r) * pow(a, shuffles*(size-2), size) + r) % size

    return solution


def main():

    rules = []
    with open('input') as in_f:
        for line in in_f:
            chunks = line.strip().split(' ')
            pre = ' '.join(chunks[:-1])
            post = int(chunks[-1]) if chunks[-1] != 'stack' else -1
            rule = (pre, post)
            rules.append(rule)

    solution = solve(rules)

    print(solution)


if __name__ == "__main__":

    main()
