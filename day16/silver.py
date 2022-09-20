

def solve(d):

    iterations = 100

    for _ in range(iterations):
        new_d = []
        for idx in range(len(d)):
            l = idx + 1
            c = idx
            acum = 0
            while c < len(d):
                acum += sum(d[c:c+l])

                c += 2*l

                acum -= sum(d[c:c + l])

                c += 2 * l

            acum = acum * -1 if acum < 0 else acum
            t = acum % 10
            new_d.append(t)
        d = list(new_d)

    return ''.join(map(str, d[:8]))


def main():

    with open('input') as in_f:
        data = [int(x) for x in in_f.readline().strip()]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
