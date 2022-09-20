from collections import defaultdict


def solve(data):

    childs = defaultdict(set)

    # build tree
    for a, b in data:
        childs[a].add(b)

    # compute depth
    depth = {'COM': 0}

    visited = set()
    reachable = ['COM']

    while reachable:

        current = reachable.pop()
        current_d = depth[current]

        for c in childs[current]:
            depth[c] = current_d + 1

            if c not in visited:
                reachable.append(c)

        visited.add(current)

    # sum all depths
    solution = sum(depth.values())

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip().split(')') for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
