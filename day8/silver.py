from collections import defaultdict, Counter

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

    min_0 = w * t
    signature = 0
    for idx, layer in layers.items():
        pix = Counter(layer)
        c0 = pix['0']

        if c0 < min_0:
            min_0 = c0
            signature = pix['1'] * pix['2']

    return signature


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
