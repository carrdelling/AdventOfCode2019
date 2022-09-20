from collections import defaultdict


def solve(data):

    w = 25
    t = 6

    l = len(data)
    n = l / (w*t)

    layers = defaultdict(list)

    l_ = 0
    r_ = 0
    c_ = 0

    for c in data:

        layers[l_].append(c)

        c_ += 1
        if c_ >= w:
            c_ = 0
            r_ += 1
            if r_ >= t:
                r_ = 0
                l_ += 1

    stacked = [d for idx, d in sorted(layers.items())]

    image = {}

    for i in range(t):
        for j in range(w):
            ii = (i*w) + j

            for s in stacked:
                v = s[ii]

                if v in {'0', '1'}:
                    image[(i, j)] = v
                    break

    contents = []
    for i in range(t):
        row = []
        for j in range(w):
            if j % 5 != 4:
                row.append(image[(i, j)])
            if j % 5 == 3:
                row.append(' ')
        contents.append(''.join(row))

    print('\n'.join(contents))

    return 0


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solve(data)


if __name__ == "__main__":

    main()
