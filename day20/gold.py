from collections import defaultdict, deque

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_neighbors(x, y):

    for i, d in enumerate(DIRS):
        yield (x + d[0], y + d[1]), i + 1


def parse_portals(g):

    portals = defaultdict(list)
    reverse = {}

    for (x, y), c in g.items():
        if c in '.# ':
            continue

        pos = None
        sl = None
        fl = c

        for n, _ in get_neighbors(x, y):
            if n not in g:
                continue

            # entry
            if g[n] == '.':
                pos = n

            # exit portal
            elif g[n] not in '.# ':
                sl = g[n]

        if pos is None or sl is None:
            continue

        signature = fl + sl if fl < sl else sl + fl

        portals[signature].append(pos)
        reverse[pos] = signature

    return portals, reverse


def solve(labyrinth):

    portals, reverse_portals = parse_portals(labyrinth)

    w = max(k[0] for k in labyrinth)
    h = max(k[1] for k in labyrinth)

    aa = portals['AA'][0]

    states = deque()

    initial_state = (aa[0], aa[1], 0, 0)
    states.append(initial_state)

    visited = {(aa[0], aa[1], 0)}

    while states:
        x, y, d, layer = states.popleft()

        # exit !!
        if layer == 0 and (x, y) == portals['ZZ'][0]:
            return d
        if labyrinth[(x, y)] == '#':
            continue

        if layer < 0:
            continue

        for n, _ in get_neighbors(x, y):

            current_layer = layer

            # portals
            if labyrinth[n] not in '#. ':
                lp = portals[reverse_portals[(x, y)]]
                if len(lp) < 2:
                    continue

                # outer layer
                if x < 3 or x > w - 3 or y < 3 or y > h - 3:
                    current_layer -= 1
                # inner layer
                else:
                    current_layer += 1

                if lp[0] == (x, y):
                    n = lp[1]
                else:
                    n = lp[0]

            if (n[0], n[1], current_layer) not in visited:
                visited.add((n[0], n[1], current_layer))
                states.append((n[0], n[1], d + 1, current_layer))


def main():

    lab = {}
    with open('input') as in_f:
        for y, l in enumerate(in_f.read().split("\n")):
            for x, c in enumerate(l):
                lab[(x, y)] = c

    solution = solve(lab)

    # > 540
    print(solution)


if __name__ == "__main__":

    main()
