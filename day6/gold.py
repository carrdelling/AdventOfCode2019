from collections import defaultdict


def solve(data):

    childs = defaultdict(set)
    parent = {}

    # build tree
    for a, b in data:
        childs[a].add(b)
        parent[b] = a

    # YOU path
    you = set()
    current = 'YOU'
    while current != 'COM':
        current = parent[current]
        you.add(current)

    # SAN path
    san = set()
    current = 'SAN'
    while current != 'COM':
        current = parent[current]
        san.add(current)

    path = (san - you) | (you - san)

    solution = len(path)

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip().split(')') for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
