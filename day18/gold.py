from collections import deque
from heapq import heappop, heappush


def search(target, maze):
    ty, tx = target

    visited = set()
    paths = {}

    nodes = deque()
    nodes.append((ty, tx, 0, ()))

    while len(nodes) > 0:
        y, x, steps, other = nodes.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))

        if maze[y][x].islower() and target != (y, x):
            paths[maze[y][x]] = (steps, other)

        for _y, _x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dy = y + _y
            dx = x + _x

            if maze[dy][dx] != '#':
                if maze[dy][dx].isupper():
                    more_keys = tuple(set(list(other) + [maze[dy][dx].lower()]))
                    nodes.append((dy, dx, steps + 1, more_keys))
                else:
                    nodes.append((dy, dx, steps + 1, other))
    return paths


def solve(maze):
    distances = {}

    # prepare pairwise distances
    keys = 0
    current_bot = '0'
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c].islower():
                distances[maze[r][c]] = (r, c)
                keys += 1
            elif maze[r][c] == '@':
                distances[current_bot] = (r, c)
                current_bot = chr(ord(current_bot) + 1)

    # pairwise paths (a, b) => (steps, keys in-between)
    paths = {}
    for c in distances:
        for k, v in search(distances[c], maze).items():
            paths[c, k] = v

    # dijkstra to find the optimum order for the keys
    states = [(0, (('0', '1', '2', '3'), tuple()))]
    seen = set()
    solution = None

    while len(states) > 0 and solution is None:
        dist, node = heappop(states)
        if node in seen:
            continue
        seen.add(node)

        sources, keys_found = node
        if len(keys_found) == keys:
            solution = dist
            continue
        for source in sources:
            valid_targets = [k for k in paths.keys() if k[0] == source]
            for ui, v in valid_targets:
                (w, T) = paths[ui, v]
                if len(set(T) - set(keys_found)) == 0 and v not in keys_found:
                    other_keys = {x for x in sources if x != source}
                    other_keys.add(v)

                    new_found = set(keys_found)
                    new_found.add(v)

                    new_state = ((dist + w), (tuple(other_keys), tuple(new_found)))
                    heappush(states, new_state)

    return solution


def main():

    with open('input') as in_f:
        maze = [list(line.strip()) for line in in_f]

    maze[39][39:42] = ['@', '#', '@']
    maze[40][39:42] = ['#', '#', '#']
    maze[41][39:42] = ['@', '#', '@']

    solution = solve(maze)

    print(solution)


if __name__ == "__main__":
    main()
